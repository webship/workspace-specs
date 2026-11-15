import os, sys; sys.path.insert(0, os.environ['S'] + '/specs'); from _folder import *
p = 'specs'
RULES = """- **The stages are gates.** An analysis needs a story, a canvas needs an analysis; each one is read
  and edited by a person before the next is asked for.
- **The story is written by the person who asks**, never generated.
- **When reality diverges, fix the spec first**, then the code: `-a drift` says whether the canvas
  still describes the tree.
- **A spec lives in the Specs folder**, never inside the project it is about.
- The workspace is container-based (DDEV by default): a spec that describes it says so."""
folder_plugin(p, 'Specs', ('specs-author', 'specs-start', 'specs-design-a-change'),
 "Specs are structured prompts and specifications: a change is designed as an artifact (a story, an analysis, a REASONS Canvas) that is reviewed, versioned and kept in step with the code.",
 "Use this agent to design a change as a spec in the `specs/` folder of the Webship Workspace with `cmd-spdd.sh` — start the spec for a target, help with the story the person writes, draft the analysis and the REASONS Canvas when their gate is passed, review a spec against the checklist, read it as one document, check whether the canvas still matches the tree — and to keep the shared specs in step with `cmd-tools-specs.sh`. Invoke for \"start a spec for this change\", \"review this spec\", \"draft the analysis\", \"has the code drifted from the canvas\", or \"list the specs\".",
 """
## What an item is here

One spec is a folder: `~/workspace/specs/<workspace>/<project>/NNN-topic/`, with `01-story.md`
(the ask: problem, definition of done, acceptance criteria), `02-analysis.md` (what exists, what
the change touches, what could go wrong), `03-canvas.md` (the REASONS Canvas, the contract the
change is made from) and `spec.yml` (the stage, the links, the commit the canvas was last true
for). `<workspace>/<project>` is the target: the project the change is for, by its folder.

## One spec, stage by stage

```bash
bash cmd-spdd.sh                                              # the specs: number, target, stage, topic
bash cmd-spdd.sh dev/mysite "say what the change is"          # start one: the folder, spec.yml and an empty 01-story.md
bash cmd-spdd.sh 001 --spdd-action show                       # where it is and which files it has
bash cmd-spdd.sh 001 --spdd-action review                     # what is mechanically missing, and what a reviewer must still judge
bash cmd-spdd.sh 001 --spdd-action analysis                   # draft 02-analysis.md: only once the story is written
bash cmd-spdd.sh 001 --spdd-action canvas                     # draft 03-canvas.md: needs an analysis
bash cmd-spdd.sh 001 --spdd-action read                       # the whole spec as one document
bash cmd-spdd.sh 001 --spdd-action drift                      # does the canvas still describe the tree
bash cmd-spdd.sh 001 --spdd-action sync                       # record that it does again, after the spec was fixed
bash cmd-spdd.sh dev/mysite --spdd-action constitution        # what the product is and is not: one per target
```

A spec is named by its number, its slug, or `<workspace>/<project>/NNN-slug`. The story is written
by the person who asks: help with its questions, do not fill it in. The command does not always
notice a story that is still the empty template, so holding that gate is your job: never ask for
an analysis of a story nobody wrote. `analysis` and `canvas` hand
the draft to the AI CLI on this machine (Claude Code by default) and take a minute; when no CLI
is found the prompt is written to a file beside the spec instead.

## The shared specs

```bash
bash cmd-tools-specs.sh                         # the shared templates and constitutions: here, changed, not here yet
bash cmd-tools-specs.sh --list-remote           # what the shared repository carries
bash cmd-tools-specs.sh --diff                  # what taking the shared copy would change
bash cmd-tools-specs.sh --pull                  # take it; your copy is backed up first when it differs
bash cmd-tools-specs.sh --share                 # how to propose one of yours: creates nothing
```
""", RULES,
 "How work is done in the `specs/` folder of the Webship Workspace — what a spec is there (a folder per change: story, analysis, REASONS Canvas, `spec.yml`), the stages and their gates, every action of `cmd-spdd.sh`, how the shared specs are kept in step with `cmd-tools-specs.sh`, and the settings keys of the folder. Use when asked to \"start a spec\", \"what stage is this spec at\", \"review the spec\", \"check the canvas for drift\", or when a command of `specs/` is about to be run.",
 """1. **Start** the spec for its target: `bash cmd-spdd.sh dev/mysite "say what the change is"`. It
   makes `~/workspace/specs/dev/mysite/NNN-topic/` with `spec.yml` and an empty `01-story.md`.
2. **The person writes the story**: the problem, the scope, the definition of done, the acceptance
   criteria.
3. **Review**: `bash cmd-spdd.sh 001 --spdd-action review`.
4. **Analysis**, once the story is written: `bash cmd-spdd.sh 001 --spdd-action analysis`. Read it
   and edit it.
5. **Canvas**, once the analysis is right: `bash cmd-spdd.sh 001 --spdd-action canvas`.
6. **Make the change from the canvas**, in the target's own folder.
7. **Keep it true**: `bash cmd-spdd.sh 001 --spdd-action drift`; fix the spec first, then
   `bash cmd-spdd.sh 001 --spdd-action sync`.""",
 ("Start a spec for a change in the specs/ folder of the Webship Workspace with cmd-spdd.sh: name the target, start the spec, show where the story is to be written, and say what the next gate is.", '<workspace>/<project> <what the change is>', """
Start a spec in `~/workspace/specs` from: `$ARGUMENTS`

The arguments are the text typed after the command: the first word is the target, as
`<workspace>/<project>` (the folder of the project the change is for, for example `dev/mysite`),
and what follows is the change, in one sentence. With no target or no sentence, stop and ask for
what is missing. The workspace is container-based (DDEV by default).

## 1. Look at what is there

```bash
cd ~/workspace/specs
bash cmd-spdd.sh
```

If a spec for the same change exists, say so and stop: one change, one spec.

## 2. Start it

```bash
bash cmd-spdd.sh <workspace>/<project> "<what the change is>"
```

It prints the folder of the spec and the path of `01-story.md`.

## 3. Hand the story over

The story is written by the person who asks, not generated. Show the path of `01-story.md` and
its four parts: the problem, the scope (in and out), the definition of done, the acceptance
criteria. Offer to ask the questions that fill them; do not fill them in from guesses.

## 4. Say what comes next

```bash
bash cmd-spdd.sh <number> --spdd-action review
bash cmd-spdd.sh <number> --spdd-action analysis
```

`review` says what is still missing; `analysis` is asked for only once the story is written. For the
later stages, hand over to the `specs-author` agent; the `specs-workflow` skill has every action.
"""),
 ("Design a change as a spec in the specs folder, stage by stage, before any code is written.", """
Design the change <change> for <workspace>/<project> as a spec, stage by stage
# ~/workspace/specs · one folder per change · container-based (DDEV by default)
# <workspace>/<project> is the folder of the project the change is for, for example dev/mysite
# no code is written in this session: the spec is the work

1. bash cmd-spdd.sh
   tell me whether a spec for this change exists already
2. bash cmd-spdd.sh <workspace>/<project> "<change>"
   tell me where 01-story.md is
3. ask me the questions of the story, one part at a time: the problem, the scope in and out,
   the definition of done, the acceptance criteria; write my answers into 01-story.md
4. bash cmd-spdd.sh <number> --spdd-action review
   tell me what is still missing
5. when I say the story is right: bash cmd-spdd.sh <number> --spdd-action analysis
   show me the analysis, and what in it contradicts the story

Stop after the analysis and wait for me: the canvas is asked for only when the analysis is right.
"""),
 {'specs-author': "Designs a change as a spec in `specs/` with `cmd-spdd.sh`, stage by stage and gate by gate; reviews, reads and checks a spec for drift; keeps the shared specs in step",
  'specs-workflow': "How work is done in `specs/`: what a spec is, the stages and their gates, every action of `cmd-spdd.sh`, the shared specs, the settings keys",
  'specs-start': "`/specs-start <workspace>/<project> <what the change is>`: starts the spec, hands the story over and says what the next gate is",
  'specs-design-a-change': "A new session that designs a change as a spec: story by questions, review, analysis, then waits"},
 tools_extra={'cmd-spdd.sh': "One spec, stage by stage: `<spec or target> [what the change is]`. `--spdd-action` is `list`, `story`, `analysis`, `canvas`, `review`, `read`, `drift`, `sync`, `show` or `constitution`; with a target and a sentence it starts a spec, with nothing it lists them",
              'cmd-tools-specs.sh': "Keeps the shared specs (the templates and the product constitutions) in step with the shared repository; with no flag it says what is here, changed, or not here yet"},
 settings_extra=[(['presentation.label', 'presentation.subtitle', 'presentation.noun', 'presentation.kind'], "How the page reads: `Specs`, one item is a `spec`, laid out as a list of `files`")],
 run=["bash cmd-spdd.sh", "bash cmd-spdd.sh dev/demo1 'say hello on the front page' | tail -7", "bash cmd-spdd.sh", "bash cmd-spdd.sh 001 --spdd-action show", "bash cmd-spdd.sh 001 --spdd-action review | head -12", "ls _defaults 2>&1 | head -3"], what='design changes as specs in')
