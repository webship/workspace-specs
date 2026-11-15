import os, sys; sys.path.insert(0, os.environ['S'] + '/specs'); from _sites import *
p = 'projects'
sites_plugin(p, 'Projects', 'projects-site-keeper', 'projects-clone', 'projects-backup-clone-and-test',
 "Projects are client projects: a site built on a distribution rather than the distribution itself, work somebody depends on.",
 "A project is somebody's work: back it up before a change (`bash cmd-tool-backup-project.sh mysite`), try the change on a clone, and never remove or rebuild one unasked.",
 "Use this agent to work on a client project in the `projects/` folder of the Webship Workspace without putting it at risk: back it up, clone it to try a change, run its Webship-js suite, give it another address, or start a new project from a builder, with the `cmd-*.sh` commands the Projects folder ships (`cmd-tool-backup-project.sh`, `cmd-tools-clone.sh`, `cmd-tools-testing.sh`, `cmd-tools-hostnames.sh`, `cmd-tools-checks.sh`, the Drupal, Drupal CMS and Webships builders). It works in containers only and never on the host. Invoke for \"back up this project\", \"clone the project to try an update\", \"run the tests of this project\", \"start a new client project\", or \"what does this project answer at\".",
 """bash cmd-drupal11-recommended-project.sh mysite --install --add-users
bash cmd-drupalcms2-x-project.sh mysite --install --add-users
bash cmd-webships3-0-x-project.sh mysite --add-users""",
 "How work is done in the `projects/` folder of the Webship Workspace — how a client project is backed up, cloned to try a change, tested with Webship-js and checked, which `cmd-*.sh` starts a new project, the flags of each command, and the settings keys of the folder. Use when asked to \"back up this project\", \"clone the project before the update\", \"run the project's tests\", \"start a new client project\", or when a command of `projects/` is about to be run.",
 """1. **Back up first**: `bash cmd-tool-backup-project.sh mysite` (the folder and the database, into
   `backups/projects/`).
2. **Try a change on a clone**, never on the project itself:
   `bash cmd-tools-clone.sh mysite --to mysite2`, or into another folder with
   `--target-workspace`. For a git checkout, `--worktree` makes the clone a branch of the same
   repository.
3. **Test** the clone, then the project: `bash cmd-tools-testing.sh mysite2 --dry-run`,
   `bash cmd-tools-testing.sh mysite2 --run`; `bash cmd-tools-checks.sh mysite2 --list` shows the
   code-quality checks it declares.
4. **Clear the clone**, after asking: `bash cmd-tools-remove.sh mysite2`. The project stays.

A **new** project starts from a builder: `bash cmd-drupal11-recommended-project.sh mysite --install`.
A builder deletes a project of the same name first: never give it the name of a project that exists.""",
 "Clone a client project of the projects/ folder of the Webship Workspace under a new name to try a change on, after backing the project up, and say where the clone answers.",
 '<project> [new name] [folder]',
 """
Clone the project of `~/workspace/projects` named in: `$ARGUMENTS`

The arguments are the text typed after the command: the first word is the project (its folder
name in `projects/`), the second word is the name of the clone (`<project>2` when it is left
out), and a third word is another sites folder to put the clone in. With no project, stop and
ask for one: `ls -d ~/workspace/projects/*/.ddev` lists the candidates. The workspace is
container-based (DDEV by default); nothing is run on the host for a project.

## 1. Back the project up

```bash
cd ~/workspace/projects
bash cmd-tool-backup-project.sh <project>
```

The folder and the database land in `backups/projects/`. If the backup fails, stop.

## 2. Make sure the new name is free

```bash
ls -d ~/workspace/*/<new name> 2>/dev/null
ddev list | grep -w <new name>
```

## 3. Clone

```bash
bash cmd-tools-clone.sh --help
bash cmd-tools-clone.sh <project> --to <new name>
bash cmd-tools-clone.sh <project> --to <new name> --target-workspace <folder>
```

Use the second form when a folder was given. Run it once. If it fails, show the line that failed
and stop: the project itself is not touched by a clone.

## 4. Report

The backup that was written, the clone's folder and address (`https://<new name>.ddev.site`), and
the commands that go on from here:

```bash
bash cmd-tools-testing.sh <new name> --run     # its Webship-js suite, when it has one
bash cmd-tools-remove.sh <new name>            # when the change was tried
```

Never remove or rebuild the project itself. For the change and its tests, hand over to the
`projects-site-keeper` agent; the `projects-workflow` skill lists every command of the folder.
""",
 "Back a client project up, clone it, and run its Webship-js suite on the clone before anything changes on the project.",
 """
Back up the project <project> of the projects folder, clone it as <clone>, and test the clone
# ~/workspace/projects · https://<clone>.ddev.site · container-based (DDEV by default)
# the project itself is never changed, rebuilt or removed in this session
# nothing on the host: no composer, drush, npm or mysql outside a site's container

1. bash cmd-tool-backup-project.sh <project>
   tell me the two files it wrote in backups/projects/
2. bash cmd-tools-clone.sh <project> --to <clone>
3. bash cmd-tools-hostnames.sh <clone>
   tell me the address the clone answers at
4. bash cmd-tools-testing.sh <clone> --dry-run
   bash cmd-tools-testing.sh <clone> --run
   if the clone has no testing stack, say so and ask before setting one up
5. bash cmd-tools-checks.sh <clone> --list
   the code-quality checks the project declares

If a command fails, show the line that failed and stop. Do not retry with other flags.
Report the backup, the address of the clone, and the totals of the run.
Then ask me what to try on the clone, or whether to remove it with: bash cmd-tools-remove.sh <clone>
""",
 {'projects-site-keeper': "Works on a client project in `projects/` without putting it at risk: backup, a clone to try the change on, its Webship-js suite, its addresses; starts a new project from a builder",
  'projects-workflow': "How work is done in `projects/`: back up, clone, test, clear the clone; every command with its flags, the settings keys",
  'projects-clone': "`/projects-clone <project> [new name] [folder]`: backs the project up, clones it and says where the clone answers",
  'projects-backup-clone-and-test': "A new session that backs a project up, clones it and runs the Webship-js suite on the clone"},
 extra_rules="""- **A project is somebody's work.** Back it up before a change
  (`bash cmd-tool-backup-project.sh <name>`), try the change on a clone, and never remove or
  rebuild a project unasked. A builder deletes a project of the same name first: never give it
  the name of a project that exists.
- `bash cmd-tools-remove.sh` refuses a folder with work that is on no remote unless `--force` is
  given: never give it unasked.""")
