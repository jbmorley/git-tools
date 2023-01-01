# Git Tools

## Overview

## Installation

1. Clone the repository:

   ```bash
   mkdir -p ~/Projects
   cd ~/Projects
   git clone git@github.com:jbmorley/git-tools.git
   ```

2. Update the submodules:

   ```
   git submodule update --init
   ```

3. Include the Git Tools configuration file in your local Git configuration. For example, if you've cloned this repository to `~/Projects/git-tools`, then you would add the following section to yout `~/.gitconfig`:

   ```
   [include]

       path = ~/Projects/git-tools/config
   ```

### Updates

```bash
git update-git-tools
```

## Commands

Git Tools adds the following additional git commands, many of which are simply shorter forms to avoid the need to type too much:

- `br` – alias for `branch`
  ```bash
  git branch
  ```
- `ci` – alias for `commit`
  ```bash
  git commit
  ```
- `co` – alias for `checkout`
  ```bash
  git checkout
  ```
- `d` – alias for `diff`
  ```bash
  git diff
  ```
- `dc` – show the cached changes
  ```bash
  git diff --cached
  ```
- `del` – interactive delete branch
- `dt` – alias for `difftool`
  ```bash
  git difftool
  ```
- `gt-install` – install Git Tools dependencies
- `gt-install-directory` – echo Git Tools install directory
- `gt-update` – update Git Tools installation
- `list-aliases` – list all aliases
- `pf` – force push with lease
  ```bash
  git push --force-with-lease
  ```
- `s` – alias for `status`
  ```bash
  git status
  ```
- `sha` – alias for `rev-parse HEAD`
  ```bash
  git rev-parse HEAD
  ```
- `sl`
- `sla`
- `st` – alias for `status`
  ```bash
  git status
  ```
- `unstage` – unstage the current changes
  ```bash
  git reset HEAD --
  ```
- `up` – fetch and rebase onto `origin/main`
   ```bash
   git fetch origin -p
   git rebase origin/main --autostash
   ```
