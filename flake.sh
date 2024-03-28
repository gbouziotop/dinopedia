#!/bin/sh
set -x

git diff origin/main -- "*.py" ":!*/migrations/*" | flake8 --diff