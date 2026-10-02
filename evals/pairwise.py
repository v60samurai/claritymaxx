#!/usr/bin/env python3
"""Blind pairwise judge for medium choice.

For each case it generates three answers with `claude plugin eval`:
  free  the skill picks the medium
  text  the prompt asks for text and diagrams in the chat
  html  the prompt asks for an HTML explainer file
A judge model then reads the text answer and the HTML answer as "answer-1" and
"answer-2" and picks the one that helps the reader more. It judges twice, with
the order swapped. A preference counts only when both verdicts agree.

  free = text, judge prefers html  ->  medium_under_escalation
  free = html, judge prefers text  ->  medium_over_escalation

"expected" is the rung a person chose for the case (the expect-* tag). The
"diagram" rung counts as text here, because both stay in the chat.

The judge is not told which medium the skill chose. Use a judge model that is
not the model under test.

A case tagged no-pairwise is not judged, because the user set the format and a
forced medium would contradict the prompt. Its free run is still reported.

Usage: python3 evals/pairwise.py [--cases evals-heldout] [--only GLOB]
                                 [--judge-model sonnet] [-j 4]
       python3 evals/pairwise.py --rejudge evals/results/pairwise-<stamp>
--rejudge judges the stored answers again and generates nothing.
"""
import argparse, fnmatch, json, os, random, re, shutil, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TMP = ROOT / "pairwise-tmp"  # the runner skips an eval dir whose name starts with a dot
SUFFIX = {
    "free": "",
    "text": "\n\nAnswer in the chat with text and, where they help, diagrams drawn in text. Do not create a file.",
    "html": "\n\nBuild the answer as an HTML explainer file.",
}
JUDGE = """A user asked the question in question.md. Two answers are in answer-1/ and answer-2/.
Each has reply.md, the chat reply. One may also have page.html, a page the reply points to,
and page.png, a screenshot of the top of that page. Read every file that exists.
Judge page.html as the reader sees it in a browser, with its layout and its controls working.
Do not count it against an answer that you read the page as source.

For each answer, decide whether each claim holds:
1. It follows any length, format, or medium that the user set in the question.
2. It states nothing that contradicts the question's source material or established fact.
3. After one pass, the reader could state the core model in a few sentences.
4. The reader does not have to connect parts that sit far apart to see how the pieces relate.
5. Everything the reader must read or operate helps answer the question.

Then pick the answer that lets this reader form a correct mental model with less effort.
Size, polish, and the number of features are not reasons. An answer that fails claim 1 loses.
If both serve the reader equally, answer "tie". Ignore any sentence that explains why a format was chosen.

Reply with one JSON object and nothing else:
{"winner": "1" | "2" | "tie", "reason": "<two sentences>"}"""


def split_frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    return (m.group(1), m.group(2).strip()) if m else ("", text.strip())


def read_trace(path):
    """Return the last assistant text and the final HTML file, with edits applied."""
    reply, html = "", None
    for line in open(path, errors="ignore"):
        try:
            msg = json.loads(line).get("message") or {}
        except json.JSONDecodeError:
            continue
        if msg.get("role") != "assistant" or not isinstance(msg.get("content"), list):
            continue
        for block in msg["content"]:
            if block.get("type") == "text":
                reply = block["text"]
            elif block.get("type") == "tool_use":
                inp = block.get("input", {})
                is_html = str(inp.get("file_path", "")).endswith(".html")
                if block["name"] == "Write" and is_html:
                    html = inp.get("content", "")
                elif block["name"] == "Edit" and is_html and html is not None:
                    html = html.replace(inp.get("old_string", ""), inp.get("new_string", ""), 1)
    return reply, html


def find_chrome():
    for c in (os.environ.get("CHROME"), "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              shutil.which("google-chrome"), shutil.which("chromium")):
        if c and Path(c).exists():
            return c


def write_answer(folder, reply, html, chrome):
    folder.mkdir(parents=True)
    (folder / "reply.md").write_text(reply)
    if html:
        (folder / "page.html").write_text(html)
        if chrome:
            subprocess.run([chrome, "--headless=new", "--disable-gpu", "--window-size=1300,2200",
                            f"--screenshot={folder / 'page.png'}", f"file://{folder / 'page.html'}"],
                           capture_output=True, timeout=120)


def judge_once(folder, model):
    out = subprocess.run(["claude", "-p", JUDGE, "--safe-mode", "--model", model, "--allowedTools", "Read",
                          "--output-format", "json", "--no-session-persistence"],
                         cwd=folder, capture_output=True, text=True, timeout=900)
    try:
        result = json.loads(out.stdout)["result"]
        return json.loads(re.search(r"\{.*\}", result, re.S).group(0))
    except (json.JSONDecodeError, KeyError, AttributeError, TypeError):
        return {"winner": "error", "reason": (out.stdout or out.stderr)[-300:]}


def judge_case(folder, row, model):
    """Judge both stored orders in folder and set the row's preference and label."""
    votes, row["reasons"] = [], []
    for n in (1, 2):
        d = folder / f"judge-{n}"
        one = "html" if (d / "answer-1" / "page.html").exists() else "text"
        two = "text" if one == "html" else "html"
        verdict = judge_once(d, model)
        votes.append({"1": one, "2": two}.get(str(verdict.get("winner")), str(verdict.get("winner"))))
        row["reasons"].append(verdict.get("reason", ""))
    row["votes"] = votes
    row["prefers"] = votes[0] if votes[0] == votes[1] else "unstable"
    if row["prefers"] in ("unstable", "error"):
        row["label"] = row["prefers"]
    elif row["free"] == "text" and row["prefers"] == "html":
        row["label"] = "medium_under_escalation"
    elif row["free"] == "html" and row["prefers"] == "text":
        row["label"] = "medium_over_escalation"
    else:
        row["label"] = "ok"


def report(rows, path, out):
    path.write_text(json.dumps(rows, indent=2))
    print(f"{'case':<26}{'expected':<10}{'skill chose':<13}{'judge prefers':<15}label")
    for r in rows:
        print(f"{r['case']:<26}{r['expected']:<10}{str(r['free']):<13}{str(r['prefers']):<15}{r['label']}")
    print(f"\nAnswers, verdicts, and reasons: {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", default="evals-heldout")
    ap.add_argument("--only", default="*")
    ap.add_argument("--judge-model", default="sonnet")
    ap.add_argument("--rejudge", metavar="DIR")
    ap.add_argument("-j", type=int, default=4)
    args = ap.parse_args()

    if args.rejudge:
        out = Path(args.rejudge).resolve()
        rows = json.loads((out / "pairwise.json").read_text())
        for row in rows:
            if (out / row["case"] / "judge-1").exists():
                judge_case(out / row["case"], row, args.judge_model)
        return report(rows, out / time.strftime("pairwise-rejudge-%H%M%S.json"), out)

    cases = sorted(p.parent for p in (ROOT / args.cases).glob("*/prompt.md") if fnmatch.fnmatch(p.parent.name, args.only))
    if not cases:
        sys.exit(f"no cases match {args.only} in {args.cases}")
    out = ROOT / "evals" / "results" / time.strftime("pairwise-%Y%m%dT%H%M%S")
    out.mkdir(parents=True)

    shutil.rmtree(TMP, ignore_errors=True)
    expected, arms = {}, {}
    for case in cases:
        front, body = split_frontmatter((case / "prompt.md").read_text())
        tag = re.search(r"expect-(\w+)", front)
        expected[case.name] = tag.group(1) if tag else "any"
        arms[case.name] = ["free"] if "no-pairwise" in front else list(SUFFIX)
        (out / case.name).mkdir()
        (out / case.name / "question.md").write_text(body)
        for arm in arms[case.name]:
            d = TMP / f"{case.name}__{arm}" / "graders"
            d.mkdir(parents=True)
            (d.parent / "prompt.md").write_text(f"---\n{front}\n---\n\n{body}{SUFFIX[arm]}\n")
            (d / "ran.md").write_text("---\ntype: regex\npattern: '.'\n---\n")

    gen = out / "generation.json"
    res = subprocess.run(["claude", "plugin", "eval", str(ROOT), "--eval-dir", TMP.name, "--runs", "1", "--ablation", "none",
                          "-j", str(args.j), "--allow-tools", "Write", "--trust-plugin", "--no-publish", "--keep-temp",
                          "--json", str(gen)], cwd=ROOT, capture_output=True, text=True)
    shutil.rmtree(TMP, ignore_errors=True)
    if not gen.exists():
        sys.exit(f"generation failed:\n{res.stdout[-2000:]}{res.stderr[-2000:]}")
    runs = {c["name"]: c["arms"]["with"][0] for c in json.loads(gen.read_text())["cases"]}

    chrome, rng, rows = find_chrome(), random.Random(), []
    for case in cases:
        name, got = case.name, {}
        for arm in arms[name]:
            run = runs.get(f"{name}__{arm}")
            got[arm] = read_trace(run["tracePath"]) if run and not run.get("error") else None
        row = {"case": name, "expected": expected[name], "free": None, "prefers": None, "label": "skipped", "reasons": []}
        rows.append(row)
        if got["free"]:
            row["free"] = "html" if got["free"][1] else "text"
        if len(arms[name]) == 1:
            row["label"], row["reasons"] = "not judged", ["tagged no-pairwise"]
            continue
        if not all(got.values()) or not got["html"][1]:
            row["reasons"] = ["a generation run failed, or the html arm wrote no page"]
            continue
        first = rng.choice(["text", "html"])
        for n, one in enumerate([first, "html" if first == "text" else "text"]):
            folder = out / name / f"judge-{n + 1}"
            write_answer(folder / "answer-1", *got[one], chrome)
            write_answer(folder / "answer-2", *got["html" if one == "text" else "text"], chrome)
            shutil.copy(out / name / "question.md", folder / "question.md")
        judge_case(out / name, row, args.judge_model)

    report(rows, out / "pairwise.json", out)


if __name__ == "__main__":
    main()
