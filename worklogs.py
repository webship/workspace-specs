import os, sys; sys.path.insert(0, os.environ['S'] + '/specs'); from _folder import *
p = 'worklogs'
RULES = """- **A worklog is a record.** It is written once and stays as written: never rewrite one to match
  what is true today. Something that should stay true belongs in the Docs folder.
- **Only what happened.** Every line can be traced to something that was run, changed or decided;
  what was not done, and what failed, is written too.
- **Nothing private**: no password, no token, no personal path; an address is an example address.
- The workspace is container-based (DDEV by default): say so when a worklog describes it."""
folder_plugin(p, 'Worklogs', ('worklogs-recorder', 'worklogs-write', 'worklogs-record-this-session'),
 "Worklogs are dated session worklogs: each one records what happened on a day, and stays as written.",
 "Use this agent to write the dated worklog of a working session in the `worklogs/` folder of the Webship Workspace — what was done, in order, with what was run and what it printed, what was decided and what is left — and to back one up with `cmd-tool-backup-worklog.sh`. It writes a new file for a new day and never rewrites an old one. Invoke for \"write the worklog of this session\", \"record what we did today\", \"what did we do on that day\", or \"back up the worklogs\".",
 """
## What an item is here

One markdown file per session: `~/workspace/worklogs/session-worklog-<date>-<subject>.md`, the
date as `YYYY-MM-DD` and the subject short, lowercase, with hyphens. A worklog records what
happened on a day. **It is not updated**: what should stay true is distilled into a document of
the Docs folder, and the worklog stays as the record.

```bash
ls session-worklog-*.md                         # the worklogs, oldest first by name
grep -l "<word>" *.md                           # which day something was done
```

## Write one

1. Take the facts from what really happened: the commands that were run and what they printed,
   the files that changed (`git status`, `git log` in the folders that were worked in), the issues
   and requests that were opened.
2. Write them in the order they happened, under the day: what was asked, what was done, what was
   found, what was decided and why, what failed, what is left.
3. End with what is left to do and where each thing stands.
4. A second session on the same day and subject adds a section at the end of that day's file; a
   file of another day is never touched.

## The commands of the folder

```bash
bash cmd-tool-backup-worklog.sh session-worklog-2026-01-31-example        # one worklog as an archive, into backups/worklogs/
bash cmd-tool-git-change-filemode-to-false.sh my-worklogs-project         # a folder with a git checkout: git stops reporting permission changes
```

`cmd-tool-backup-worklog.sh` takes the name with or without `.md`. The folder also ships
`cmd-tool-sync-agents.sh`, which copies agent definitions and has nothing to do with worklogs: it
reads the settings of another folder and is not part of the work here. Do not run it.
""", RULES,
 "How work is done in the `worklogs/` folder of the Webship Workspace — what a worklog is there (one dated markdown file per session, never updated), how one is named and written from what really happened, how it is backed up, the commands of the folder and its settings keys. Use when asked to \"write the worklog\", \"record this session\", \"where are the worklogs\", \"back up a worklog\", or when a file of `worklogs/` is about to be written.",
 """1. **Name** the file: `~/workspace/worklogs/session-worklog-<date>-<subject>.md`, the date as
   `YYYY-MM-DD`.
2. **Collect** what happened from what was run and what changed, not from memory.
3. **Write** it in order: asked, done, found, decided, failed, left.
4. **Leave it.** A worklog of another day is never edited; what should stay true goes into a
   document of the Docs folder.
5. **Back up** when asked: `bash cmd-tool-backup-worklog.sh session-worklog-2026-01-31-example`.""",
 ("Write the dated worklog of this session in the worklogs/ folder of the Webship Workspace: what was done, in order, from what was really run and changed, as a new file that is never rewritten.", '<subject> [date as YYYY-MM-DD]', """
Write the worklog of this session in `~/workspace/worklogs` for: `$ARGUMENTS`

The arguments are the text typed after the command: the first words are the subject of the
session, and a last word in the form `YYYY-MM-DD` is the day (today when it is left out). With no
subject, stop and ask for one. The workspace is container-based (DDEV by default): say so where
the worklog describes it.

## 1. Name the file

```bash
cd ~/workspace/worklogs
ls session-worklog-*.md | tail -5
```

The file is `session-worklog-<date>-<subject>.md`, the subject short, lowercase, with hyphens. If
a file of that day and subject exists, add a section at its end; never change what is in it, and
never touch a file of another day.

## 2. Collect what happened

From this session: what was asked, the commands that were run and what they printed, the files
that changed, the issues and requests that were opened, what failed. Check the folders that were
worked in with `git status` and `git log` rather than writing from memory.

## 3. Write

In the order it happened: what was asked, what was done, what was found, what was decided and
why, what failed, what is left. No password, no token, no personal path.

## 4. Report

The file, its sections, and what is left to do. To keep a copy:

```bash
bash cmd-tool-backup-worklog.sh <name>
```

For what should stay true beyond this day, say which document of the Docs folder it belongs in.
The `worklogs-recorder` agent does the same for a longer session; the `worklogs-workflow` skill
says how worklogs are kept in this folder.
"""),
 ("Record this working session as a dated worklog in the worklogs folder.", """
Write the worklog of the session on <subject> in the worklogs folder
# ~/workspace/worklogs/session-worklog-<date>-<subject>.md · container-based (DDEV by default)
# a worklog is a record: a new file for this day, never a change to an older one

1. ls ~/workspace/worklogs/session-worklog-*.md
   tell me whether a worklog of this day and subject exists; if one does, add a section at its end
2. collect what happened: what was asked, what was run and what it printed, which files changed,
   which issues and requests were opened, what failed
   check with git status and git log in the folders that were worked in
3. write the file, in the order it happened: asked, done, found, decided, failed, left
4. read it once more: every line can be traced to something that happened

No password, no token, no personal path; addresses are example addresses.
Report the file and what is left to do.
"""),
 {'worklogs-recorder': "Writes the dated worklog of a session in `worklogs/` from what was really run and changed, as a new file that is never rewritten; backs one up",
  'worklogs-workflow': "How work is done in `worklogs/`: what a worklog is, its name, collect, write, leave it; the commands, the settings keys",
  'worklogs-write': "`/worklogs-write <subject> [date]`: names the file, collects what happened and writes the worklog of the session",
  'worklogs-record-this-session': "A new session that records a working session as a dated worklog"},
 tools_extra={'cmd-tool-git-change-filemode-to-false.sh': "Sets `core.fileMode` to false in one folder with a git checkout: `<project>`",
              'cmd-tool-sync-agents.sh': "Copies agent definitions between an agents folder, the AI CLI and the shared repository. Not about worklogs: it reads the settings of another folder. Do not run it here"},
 run=["echo '# Session worklog' > session-worklog-2026-01-31-example.md && bash cmd-tool-backup-worklog.sh session-worklog-2026-01-31-example && ls ../backups/worklogs | sed 's/--.*/--<time>.tar.gz/' ; rm -f session-worklog-2026-01-31-example.md", "bash cmd-tool-sync-agents.sh --help 2>&1 | head -3"], what='write the worklogs of')
