# Specs

Structured prompts and specifications.

Part of the **Webship Workspace** (`~/workspace`), a container-based harness (DDEV by default). The rules in the root
`CLAUDE.md` apply here too; what follows is what is specific to this folder.

## What an item is here

A structured prompt: a specification written to be executed rather than read.

## Commands here

```bash
bash cmd-spdd.sh                                      # Spec (Structured-Prompt-Driven Development)
```

Every one locates the workspace from its own path, so there is nothing to export and nothing to
install. `--help` on any of them lists its arguments.

## AI items for this folder

The plugin of this folder (`@webship.co/workspace-specs`) places its own AI items in the AI folders of the
workspace, when they are active:

- `specs-author` (`ai-agents/`): Designs a change as a spec in `specs/` with `cmd-spdd.sh`, stage by stage and gate by gate; reviews, reads and checks a spec for drift; keeps the shared specs in step
- `specs-workflow` (`ai-skills/`): How work is done in `specs/`: what a spec is, the stages and their gates, every action of `cmd-spdd.sh`, the shared specs, the settings keys
- `/specs-start` (`ai-commands/`): `/specs-start <workspace>/<project> <what the change is>`: starts the spec, hands the story over and says what the next gate is
- `specs-design-a-change` (`ai-prompts/`): A new session that designs a change as a spec: story by questions, review, analysis, then waits
