import os, sys; sys.path.insert(0, os.environ['S'] + '/specs'); from _folder import *
p = 'docs'
RULES = """- **Edit in place.** A document is one markdown file in the folder; change that file, do not write
  a second copy beside it, and do not move it into a project.
- **Docs hold what stays true.** What happened on a day is a worklog, not a document: it belongs
  in the Worklogs folder.
- **Back up before a rewrite**: `bash cmd-tool-backup-doc.sh <name>`.
- **Nothing private in a document**: no password, no token, no personal path; an address is an
  example address.
- The workspace is container-based (DDEV by default): say so when a document describes it."""
folder_plugin(p, 'Docs', ('docs-writer', 'docs-write', 'docs-write-a-document'),
 "Docs are markdown documents, edited in place: reference material that stays true, each with whatever was generated from it (a PDF, an HTML render, a screenshot) beside the source.",
 "Use this agent to write or edit a markdown document in place in the `docs/` folder of the Webship Workspace: a new reference document, a change to one that exists, a check that what it says is still true, a backup before a rewrite with `cmd-tool-backup-doc.sh`. It edits the file where it is and never copies it elsewhere. Invoke for \"write a doc about this\", \"update the doc, this changed\", \"is this document still true\", \"tidy this markdown\", or \"back up this doc\".",
 """
## What an item is here

A markdown document, `~/workspace/docs/<name>.md`, plus whatever has been generated from it: a
PDF, an HTML render, a screenshot. The generated files sit beside the source and the folder's page
lists them with it. A documentation project (a folder with its own git checkout) can live here
too.

```bash
ls *.md                                         # the documents
ls <name>.*                                     # one document and what was generated from it
```

## Write or change a document

1. Read the document first, all of it, and what it links to in the folder.
2. Check what it says against the thing itself: run the command it shows with `--help`, open the
   file it names. A document that is no longer true is worse than none.
3. Change the file in place. Keep its headings and its voice; a new document gets a short
   lowercase name with hyphens, and a first heading that says what it is.
4. Say what you changed, section by section, and what you could not check.

## The commands of the folder

```bash
bash cmd-tool-backup-doc.sh my-document                           # the document as an archive, into backups/docs/
bash cmd-tool-git-change-filemode-to-false.sh my-docs-project     # a documentation project: git stops reporting permission changes
```

`cmd-tool-backup-doc.sh` takes the name with or without `.md`. The other command is for a folder
with a git checkout, not for a single file.
""", RULES,
 "How work is done in the `docs/` folder of the Webship Workspace — what a document is there (a markdown file edited in place, with what was generated from it beside it), how one is written, changed and checked against what it describes, how it is backed up, the two commands of the folder and its settings keys. Use when asked to \"write a doc\", \"update this document\", \"where do the docs live\", \"back up a doc\", or when a file of `docs/` is about to be changed.",
 """1. **Find** the document: `ls ~/workspace/docs/*.md`. One subject, one document: change the one
   that exists before writing a new one.
2. **Back it up** before a rewrite: `bash cmd-tool-backup-doc.sh my-document`.
3. **Check** every command, flag and path the document names against the thing itself.
4. **Edit in place**: `~/workspace/docs/my-document.md`. What was generated from it (a PDF, an
   HTML render) is generated again from the folder's page, not edited by hand.
5. **Say what changed**, and what could not be checked.""",
 ("Write or change a markdown document in place in the docs/ folder of the Webship Workspace: read it, check what it says against the thing itself, edit the file where it is, and say what changed.", '<name> [what it should say or what changed]', """
Write or change the document of `~/workspace/docs` named in: `$ARGUMENTS`

The arguments are the text typed after the command: the first word is the document (its file name
in `docs/`, with or without `.md`), and what follows says what it should say, or what changed.
With no name, stop and ask for one: `ls ~/workspace/docs/*.md` lists the documents. The workspace
is container-based (DDEV by default): say so where the document describes it.

## 1. Find it

```bash
cd ~/workspace/docs
ls <name>.md 2>/dev/null
```

If the file is there, this is a change: read all of it first. If it is not, this is a new
document: look for one on the same subject before writing a second (`grep -il "<subject>" *.md`).

## 2. Back it up, when it exists

```bash
bash cmd-tool-backup-doc.sh <name>
```

## 3. Check before writing

Every command, flag and path the document will name is checked against the thing itself: run the
command with `--help`, open the file. Write nothing from memory.

## 4. Write in place

Edit `~/workspace/docs/<name>.md`. Keep the headings and the voice of a document that exists; a
new one opens with a heading that says what it is, then one paragraph on what it is for. No
password, no token, no personal path; addresses are example addresses.

## 5. Report

The file, what changed section by section, what was checked and how, and what could not be
checked. For a longer piece of work, hand over to the `docs-writer` agent; the `docs-workflow`
skill says how documents are kept in this folder.
"""),
 ("Write a reference document in the docs folder, checked against the thing it describes.", """
Write the document <name> in the docs folder, about <subject>
# ~/workspace/docs/<name>.md · a markdown file edited in place · container-based (DDEV by default)
# docs hold what stays true: what happened on a day is a worklog, not a document

1. ls ~/workspace/docs/*.md
   tell me whether a document on <subject> exists already; if one does, change it instead
2. read what the document is about: the commands, the files, the settings
   run each command with --help and open each file before naming it
3. write ~/workspace/docs/<name>.md
   a heading that says what it is, one paragraph on what it is for, then what a reader does, in order
4. read it once more against what you checked
   every command, flag and path in it exists

No password, no token, no personal path; addresses are example addresses.
Report the file, its sections, what you checked and what you could not check.
"""),
 {'docs-writer': "Writes and edits the markdown documents of `docs/` in place, checks what they say against the thing itself, backs one up before a rewrite",
  'docs-workflow': "How work is done in `docs/`: what a document is, find, back up, check, edit in place; the two commands, the settings keys",
  'docs-write': "`/docs-write <name> [what it should say]`: finds or starts the document, checks before writing, edits the file in place and says what changed",
  'docs-write-a-document': "A new session that writes a reference document, checked against what it describes"},
 tools_extra={'cmd-tool-git-change-filemode-to-false.sh': "Sets `core.fileMode` to false in one documentation project (a folder with a git checkout): `<project>`"},
 run=["echo '# Demo document' > demo-document.md && bash cmd-tool-backup-doc.sh demo-document && ls ../backups/docs | sed 's/--.*/--<time>.tar.gz/' ; rm -f demo-document.md"], what='write and edit the documents of')
