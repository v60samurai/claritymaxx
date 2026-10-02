#!/bin/sh
# Builds the two upload archives in dist/ from a commit. Usage: package.sh [ref], default HEAD.
#   claritymaxx-plugin.zip   Customize > Plugins > Add > Upload plugin
#   explain-skill.zip        Customize > Skills, upload a skill
set -eu
cd "$(dirname "$0")/.."
rm -rf dist && mkdir dist
ref="${1:-HEAD}"
git archive --format=zip -o dist/claritymaxx-plugin.zip "$ref" .claude-plugin/plugin.json skills README.md LICENSE
git archive --format=zip --prefix=explain/ -o dist/explain-skill.zip "$ref:skills/explain"
unzip -l dist/claritymaxx-plugin.zip
unzip -l dist/explain-skill.zip
