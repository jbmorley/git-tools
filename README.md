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
- `dt` – alias for `difftool`
- `up` – fetch and rebase onto `origin/main`
   ```bash
   git fetch origin -p
   git rebase origin/main
   ```
- `ups` – fetch and rebase onto `origin/main` using autostash
   ```bash
   git fetch origin -p
   git rebase origin/main --autostash
   ```
