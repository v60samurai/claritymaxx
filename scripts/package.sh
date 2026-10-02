#!/bin/sh
# Builds the two upload archives in dist/ from the committed files.
#   claritymaxx-plugin.zip   Customize > Plugins > Add > Upload plugin
#   explain-skill.zip        Customize > Skills, upload a skill
set -eu
cd "$(dirname "$0")/.."
rm -rf dist && mkdir dist
git archive --format=zip -o dist/claritymaxx-plugin.zip HEAD .claude-plugin/plugin.json skills README.md LICENSE
git archive --format=zip --prefix=explain/ -o dist/explain-skill.zip HEAD:skills/explain
unzip -l dist/claritymaxx-plugin.zip
unzip -l dist/explain-skill.zip
