# @webship.co/workspace-specs

The **Specs** workspace of the [Webship Workspace](https://github.com/webship/workspace) dashboard:
the `specs/` folder (type `files`), its settings file (`core/config/workspace.specs.settings.yml`),
its commands and its docs, as a plugin.

## Use it

```bash
cd ~/workspace
bash core/scripts/plugins.sh --require github:webship/workspace-specs
bash core/scripts/plugins.sh --activate specs --with-needs     # puts `specs` on the workspaces list of settings.yml
bash core/scripts/plugins.sh --install specs      # the folder, its settings file (once), its commands, its docs (once)
```

The settings file and the docs are placed once and never overwritten: they hold what you put there.
`--deactivate` takes the workspace off the list; the folder and its content stay.

## What it needs

The AI items land in the four AI folders, so the manifest needs them (`needs`): `ai-agents`, `ai-skills`, `ai-commands`, `ai-prompts`. `--activate specs` and `--install specs` stop while one is missing and name it; with `--with-needs` they are required, activated and installed first.

## The AI items

The plugin carries its own AI items (`ai/` in the package, the manifest's `ai` block), written for the work this folder is for. `--install` places each one in the workspace folder of its kind, when that folder is an active workspace folder; `--uninstall` removes them, and keeps one that was edited in its folder.

| Item | Kind | Lands in | What it is for |
| --- | --- | --- | --- |
| `specs-author` | Agent | `ai-agents/specs-author.md` | Designs a change as a spec in `specs/` with `cmd-spdd.sh`, stage by stage and gate by gate; reviews, reads and checks a spec for drift; keeps the shared specs in step |
| `specs-workflow` | Skill | `ai-skills/specs-workflow/` | How work is done in `specs/`: what a spec is, the stages and their gates, every action of `cmd-spdd.sh`, the shared specs, the settings keys |
| `/specs-start` | Command | `ai-commands/specs-start.md` | `/specs-start <workspace>/<project> <what the change is>`: starts the spec, hands the story over and says what the next gate is |
| `specs-design-a-change` | Prompt | `ai-prompts/specs-design-a-change.md` | A new session that designs a change as a spec: story by questions, review, analysis, then waits |

From its folder an item is installed into the AI CLI (Claude Code by default) like any other: the folder's page on the dashboard, or `bash cmd-tools-ai-items.sh <name> --install` in the AI folder (`--to dev/<project>` for one project). A prompt is not installed: the New screen form lists it as the start of a new session. The body of every item is plain Markdown any AI CLI can follow; Claude Code is the default shape (the frontmatter, the launch line of a prompt). Every command, flag, settings key and path an item names is checked by `tests/items.test.ts`; the shape of the items is the one of the reference, [`docs/plugin-items-pattern.md` of the WordPress plugin](https://github.com/webship/workspace-wordpress/blob/1.0.x/docs/plugin-items-pattern.md).

## The commands

| Command |
| --- |
| `cmd-spdd.sh` |
| `cmd-tools-specs.sh` |

The bash functions these commands call live in the dashboard's `core/scripts/functions`.
