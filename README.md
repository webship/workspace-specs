# @webship/workspace-specs

The **Specs** workspace of the [Webship Workspace](https://github.com/webship/workspace) dashboard:
the `specs/` folder (type `files`), its settings file (`core/config/workspace.specs.settings.yml`),
its commands and its docs, as a plugin.

## Use it

```bash
cd ~/workspace
bash core/scripts/plugins.sh --require github:webship/workspace-specs
bash core/scripts/plugins.sh --activate specs     # puts `specs` on the workspaces list of settings.yml
bash core/scripts/plugins.sh --install specs      # the folder, its settings file (once), its commands, its docs (once)
```

The settings file and the docs are placed once and never overwritten: they hold what you put there.
`--deactivate` takes the workspace off the list; the folder and its content stay.

## The commands

| Command |
| --- |
| `cmd-spdd.sh` |
| `cmd-tools-specs.sh` |

The bash functions these commands call live in the dashboard's `core/scripts/functions`.
