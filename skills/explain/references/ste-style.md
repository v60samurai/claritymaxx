# STE-inspired prose

ASD-STE100 Simplified Technical English is a controlled language for aerospace maintenance documents. It limits vocabulary and sentence form so that a reader cannot take a sentence two ways. Claritymaxx borrows its habits for explanation. It does not apply the standard.

The target is "80% of the way to ASD-STE100". That phrase gives a direction: write almost as plainly as the standard would, and stop where a rule would hurt the explanation. It is a description of style. It is not a score, and no text is "80% compliant".

## The habits

| Habit | In practice |
|-------|-------------|
| One meaning for each word | Choose one term for a thing and keep it. If you call it a "replica" once, it is a "replica" every time. |
| Correct technical terms stay | Use the exact term, define it at first use, then repeat it. Replace a technical term only with a definition, never with a looser word. |
| Familiar words | "use", "start", "before", "about", in place of "utilize", "commence", "prior to", "approximately". |
| Short sentences | One idea for each sentence. About 20 words is a good ceiling for an instruction and 25 for a description. Go longer when a split would separate a condition from the thing it limits. |
| Explicit actor | Say what does the action: "The scheduler retries the job", in place of "The job is retried". |
| Explicit cause and effect | Write the link: "because", "so", "if ... then", "unless". |
| Clear references | Repeat the noun when "it" or "this" could point at two things. |
| Short noun strings | At most three nouns in a row. Break a longer string with "of" or "for". |
| One topic for each paragraph | Start a new paragraph when the topic changes. Use a vertical list for parallel items. |
| Keep the small words | Write "the", "a", and "that". Dropping them saves space and costs clarity. |

## Example

Before:

> Leveraging a write-ahead log, the system ensures durability by persisting mutations prior to their application, which facilitates recovery.

After:

> The database writes each change to a log file before it applies the change to the data files. This log is the write-ahead log (WAL). If the database stops in the middle of a change, it reads the WAL at restart and applies the changes that are missing from the data files.

The second version is longer. It names the actor, keeps the term "write-ahead log", and states the condition under which the log matters. Plain writing is allowed to be longer when the added words carry the model.

## Where to stop

Precision wins over simplicity. If a plain sentence would be wrong, write the precise sentence, then explain it. Keep the conditions, exceptions, and limits that change what the reader would predict.

Explanations also need things the standard restricts: analogies, questions, and words outside its dictionary. Use them when they help.

## The compliance boundary

Say "written in a style inspired by ASD-STE100" or say nothing about the standard. Do not describe output as STE-compliant, STE-conformant, or written "in STE".

Formal compliance means that every word is checked against the dictionary in the standard and every sentence against its writing rules. Claim it only when the user asks for formal compliance and that check has been done against the current issue of the standard. The standard is free on request from its owner at asd-ste100.org. Without the standard in hand, say that the text follows the style and has not been checked.

## About the standard

Read this section, and open `assets/asd-ste100-overview.png` in this skill's folder, only when the user asks about ASD-STE100 itself or asks for stricter controlled language. The image is a one-page map of the standard: its structure, annotated example sentences, verb forms, dictionary entries, and limits. Ordinary explanations do not need it.

Facts checked against asd-ste100.org in October 2026:

- The current issue is Issue 9, dated January 15, 2025. ASD owns it and the Simplified Technical English Maintenance Group (STEMG) maintains it.
- Part 1 holds the writing rules in nine sections: words, multi-word nouns, verbs, sentences, procedural writing, descriptive writing, safety instructions, punctuation and word count, and writing practices. Part 2 is the dictionary of approved and not approved words.
- Limits: 20 words for a procedural sentence, 25 words for a descriptive sentence, 6 sentences for a paragraph, and 3 words for a multi-word noun.
- The first release was the AECMA Simplified English Guide in 1986. It became ASD-STE100 in 2005.

The image uses some older wording. It says "specification" and "noun cluster". Issue 9 says "standard" and "multi-word noun". Check any other detail against the current issue before you state it as fact.
