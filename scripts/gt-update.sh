#!/bin/bash

SCRIPTS_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ROOT_DIRECTORY="${SCRIPTS_DIRECTORY}/.."

cd "$ROOT_DIRECTORY"
git fetch origin -p
git rebase origin/main --autostash

$SCRIPTS_DIRECTORY/gt-install.sh
