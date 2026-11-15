---
name: specs-workflow
description: How work is done in the `specs/` folder of the Webship Workspace — what a spec is there (a folder per change: story, analysis, REASONS Canvas, `spec.yml`), the stages and their gates, every action of `cmd-spdd.sh`, how the shared specs are kept in step with `cmd-tools-specs.sh`, and the settings keys of the folder. Use when asked to "start a spec", "what stage is this spec at", "review the spec", "check the canvas for drift", or when a command of `specs/` is about to be run.
argument-hint: '[what you are about to do in specs]'
---

# specs-workflow

`~/workspace/specs` is the Specs folder of a Webship Workspace (container-based, DDEV by default).
Specs are structured prompts and specifications: a change is designed as an artifact (a story, an analysis, a REASONS Canvas) that is reviewed, versioned and kept in step with the code. It comes with the Specs plugin (`@webship.co/workspace-specs`), which places the commands below in the folder. Every command finds the workspace from its own path; run it from the folder, and read `bash <command> --help` before quoting a flag.

## The order of work

1. **Start** the spec for its target: `bash cmd-spdd.sh dev/mysite "say what the change is"`. It
   makes `~/workspace/specs/dev/mysite/NNN-topic/` with `spec.yml` and an empty `01-story.md`.
2. **The person writes the story**: the problem, the scope, the definition of done, the acceptance
   criteria.
3. **Review**: `bash cmd-spdd.sh 001 --spdd-action review`.
4. **Analysis**, once the story is written: `bash cmd-spdd.sh 001 --spdd-action analysis`. Read it
   and edit it.
5. **Canvas**, once the analysis is right: `bash cmd-spdd.sh 001 --spdd-action canvas`.
6. **Make the change from the canvas**, in the target's own folder.
7. **Keep it true**: `bash cmd-spdd.sh 001 --spdd-action drift`; fix the spec first, then
   `bash cmd-spdd.sh 001 --spdd-action sync`.

## Commands

| Command | What it does | Flags |
| --- | --- | --- |
| `cmd-spdd.sh` | One spec, stage by stage: `<spec or target> [what the change is]`. `--spdd-action` is `list`, `story`, `analysis`, `canvas`, `review`, `read`, `drift`, `sync`, `show` or `constitution`; with a target and a sentence it starts a spec, with nothing it lists them | `--spdd-action` |
| `cmd-tools-specs.sh` | Keeps the shared specs (the templates and the product constitutions) in step with the shared repository; with no flag it says what is here, changed, or not here yet | `--diff` `--list-remote` `--pull` `--share` |

## Settings

| Key | File | What it says |
| --- | --- | --- |
| `doc.name` | `core/config/workspace.specs.settings.yml` | The folder under the workspace root: `specs` |
| `type` | `core/config/workspace.specs.settings.yml` | `files`: the page is a list of documents, edited in place |
| `presentation.label`, `presentation.subtitle`, `presentation.noun`, `presentation.kind` | `core/config/workspace.specs.settings.yml` | How the page reads: `Specs`, one item is a `spec`, laid out as a list of `files` |
| `assistant.name`, `assistant.placeholder` | `core/config/workspace.specs.settings.yml` | What the assistant is called on this page; `default` takes the workspace's |
| `workspaces` | `core/config/settings.yml` | The active folders; `specs` is on it once the plugin is activated |

## Rules

- **The stages are gates.** An analysis needs a story, a canvas needs an analysis; each one is read
  and edited by a person before the next is asked for.
- **The story is written by the person who asks**, never generated.
- **When reality diverges, fix the spec first**, then the code: `-a drift` says whether the canvas
  still describes the tree.
- **A spec lives in the Specs folder**, never inside the project it is about.
- The workspace is container-based (DDEV by default): a spec that describes it says so.

The Specs plugin places these beside this one, each in the workspace folder of its kind: the agent `specs-author` (`ai-agents/`), the command `/specs-start` (`ai-commands/`) and the prompt `specs-design-a-change` (`ai-prompts/`).
