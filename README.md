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
- `del` – interactive delete branch
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
- `gt-install` – install Git Tools dependencies
- `gt-install-directory` – echo Git Tools install directory
- `gt-update` – update Git Tools installation
- `list-alias` – list all aliases
- `pf` – force push with lease
  ```bash
  git push --force-with-lease
  ```
- `s` – alias for `status`
  ```bash
  git status
  ```
- `st` – alias for `status`
  ```bash
  git status
  ```

