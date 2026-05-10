# TODO

* Write tooling to manage cports worktrees
    * `git worktree add ~/cports-worktrees/gram add/gram`
    * `ln -s ~/cports/bldroot/ ~/cports-worktrees/gram/bldroot`
    * `ln -s /home/harper/cports/.gram/ ~/cports-worktrees/gram/.gram/`
    * `ln -s /home/harper/cports/etc/config.ini ~/cports-worktrees/gram/etc/config.ini`
    * `ln -s /home/harper/cports/etc/keys ~/cports-worktrees/gram/etc/keys`
    * Write to `/etc/apk/repositories.d/00-local-gram.list`
* Attempt to enable Gram tests
* Remove hard tabs from all of my packages

# Packages pending submission

* user/envycontrol
* user/topiary

# Packages to add

* gitg
* gity
* intelli-shell
* pnpm (needed for vtsls)
* vtsls (typescript LSP implementation)
* basedpyright
* Sublime's standalone VS Code LSPs
  * As of late 2025, Sublime is doing the best job at keeping a standalone version of VSCode's LSPs up-to-date
  * Unfortunately, they use a different Markdown server based on .Net, which would not be straightforward to package
  * https://github.com/sublimelsp/LSP-css
  * https://github.com/sublimelsp/LSP-json
  * https://github.com/sublimelsp/LSP-html
  * https://github.com/sublimelsp/LSP-eslint
* topiary-nushell
* nu-lint
* trivalent (more secure Chromium fork)
* noctalia (once v5 is out)
