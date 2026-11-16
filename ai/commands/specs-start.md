---
description: Start a spec for a change in the specs/ folder of the Webship Workspace with cmd-spdd.sh — name the target, start the spec, show where the story is to be written, and say what the next gate is.
argument-hint: '<workspace>/<project> <what the change is>'
---

# /specs-start

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
