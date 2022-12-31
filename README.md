# Git Tools

## Overview

## Installation

Include the Git Tools configuration file in your local Git configuration. For example, if you've cloned this repository to `~/Projects/git-tools`, then you would add the following section to yout `~/.gitconfig`:

```
[include]

    path = ~/Projects/git-tools/config
```

## Commands

Git Tools adds the following additional git commands, many of which are simply shorter forms to avoid the need to type too much:

- `br` – alias for `branch`
- `ci` – alias for `commit`
- `co` – alias for `checkout`
- `s` – alias for `status`
- `st` – alias for `status`
  ```bash
  git status
  ```
- `dt` – alias for `difftool`
  ```bash
  git difftool
  ```
- `up` – fetch and rebase onto `origin/main`
   ```bash
   git fetch origin -p
   git rebase origin/main --autostash
   ```
- `sha` – alias for `rev-parse HEAD`
- `hello` – simple hello world for the scripts directory
- `update-git-tools` – update the current installation
- `list-alias` – list all aliases
