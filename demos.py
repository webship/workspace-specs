import os, sys; sys.path.insert(0, os.environ['S'] + '/specs'); from _sites import *
p = 'demos'
sites_plugin(p, 'Demos', 'demos-site-builder', 'demos-build', 'demos-build-a-demo',
 "Demos are demo sites and default content, built to be shown: a demo is installed, has its accounts, answers at an address that can be given out, and is backed up before it is shown.",
 "A demo is kept while it is shown: back it up with `bash cmd-tools-backup-demo.sh mysite` before a change, and remove it only when asked.",
 "Use this agent to build a demo site in the `demos/` folder of the Webship Workspace, get it ready to be shown (installed, default accounts, an extra address, a backup) and check it with Webship-js, with the `cmd-*.sh` commands the Demos folder ships (the Drupal, Drupal CMS, Webship, Webships and Cucumber builders, `cmd-tools-hostnames.sh`, `cmd-tools-backup-demo.sh`, `cmd-tools-testing.sh`, `cmd-tools-clone.sh`). It works in containers only and never on the host. Invoke for \"build a demo\", \"spin up a Webship demo\", \"give the demo another address\", \"back up the demo before the meeting\", or \"remove the demo\".",
 """bash cmd-webship11-0-x-project.sh mysite --install --add-users
bash cmd-drupalcms2-x-project.sh mysite --install --add-users
bash cmd-drupal11-recommended-project.sh mysite --install --add-users --profile umami""",
 "How work is done in the `demos/` folder of the Webship Workspace — which `cmd-*.sh` builds a demo site, the flags of each command, how a demo gets its accounts and an address to give out, how it is checked with Webship-js and backed up before it is shown, and the settings keys of the folder. Use when asked to \"build a demo\", \"which builder is there for a Webship demo\", \"add an address to the demo\", \"back up the demo\", or when a command of `demos/` is about to be run.",
 """1. **Build** the demo, installed and with its accounts:
   `bash cmd-webship11-0-x-project.sh mysite --install --add-users`. The name is the folder, the
   container project and the address (`https://mysite.ddev.site`). A builder deletes a project of
   the same name first.
2. **Give it the address it is shown at**, when the name is not it:
   `bash cmd-tools-hostnames.sh mysite --add staging --start`.
3. **Check it** before it is shown: `bash cmd-tools-testing.sh mysite`, then
   `bash cmd-tools-testing.sh mysite --run`.
4. **Back it up** before the showing and before any change: `bash cmd-tools-backup-demo.sh mysite`
   (the folder and the database, into `backups/demos/`).
5. **Remove** it only when asked: `bash cmd-tools-remove.sh mysite`.""",
 "Build a demo site in the demos/ folder of the Webship Workspace with one of the folder's builders, installed and with its default accounts, say where it answers, and back it up.",
 '<builder or family> <name> [flags of the builder]',
 """
Build a demo in `~/workspace/demos` from: `$ARGUMENTS`

The arguments are the text typed after the command: the first word names the builder, the second
the demo, and what follows is passed to the builder as it is. With no name, stop and ask for one.
The workspace is container-based (DDEV by default): the builder runs the site in its own
container, and nothing is run on the host for it.

## 1. Find the builder

```bash
cd ~/workspace/demos
grep -H "^# workspace-name:" cmd-*-project.sh
```

The first word is a builder's file name, or enough of it to pick one: `webship` is
`cmd-webship11-0-x-project.sh`, `drupalcms` is `cmd-drupalcms2-x-project.sh`, `drupal11` is
`cmd-drupal11-recommended-project.sh`. When it fits more than one, list them and ask.

## 2. Make sure the name is free

```bash
ls -d ~/workspace/*/<name> 2>/dev/null
ddev list | grep -w <name>
```

A builder deletes a project of the same name first. If the name is taken, stop and ask.

## 3. Build, installed and with its accounts

```bash
bash cmd-webship11-0-x-project.sh --help
bash cmd-webship11-0-x-project.sh <name> --install --add-users
```

With the builder that was picked and the flags that were typed; a demo is always built with
`--install`, and with `--add-users` where the builder has it. Run it once. If it fails, show the
line that failed and stop.

## 4. Say where it answers, and back it up

```bash
bash cmd-tools-hostnames.sh <name>
bash cmd-tools-backup-demo.sh <name>
```

Report the builder, the address (`https://<name>.ddev.site`), that the default accounts are there
(never print a password), and where the backup is (`backups/demos/`). For an extra address or a
check with Webship-js, hand over to the `demos-site-builder` agent; the `demos-workflow` skill
lists every command of the folder.
""",
 "Build a demo site in the demos folder, get it ready to be shown and back it up.",
 """
Build a demo named <name> in the demos folder with <builder> and get it ready to be shown
# ~/workspace/demos · https://<name>.ddev.site · container-based (DDEV by default)
# <builder> is a cmd-*-project.sh of the folder, for example cmd-webship11-0-x-project.sh
# the builder deletes a project of the same name first: stop if <name> is a site somebody still needs
# nothing on the host: no composer, drush, npm or mysql outside the site's container

1. bash <builder> --help
   tell me the flags it takes
2. bash <builder> <name> --install --add-users
3. bash cmd-tools-hostnames.sh <name>
   tell me the address the demo answers at
4. bash cmd-tools-testing.sh <name>
   bash cmd-tools-testing.sh <name> --run
   the demo is checked with Webship-js before it is shown
5. bash cmd-tools-backup-demo.sh <name>
   the folder and the database, into backups/demos/

If a command fails, show the line that failed and stop. Do not retry with other flags.
Report the address, the result of the run and where the backup is. Never print a password.
The demo stays: remove it only when I ask, with: bash cmd-tools-remove.sh <name>
""",
 {'demos-site-builder': "Builds a demo site in `demos/` and gets it ready to be shown: installed, default accounts, an address, a check with Webship-js, a backup",
  'demos-workflow': "How work is done in `demos/`: build, address, check, back up; every builder and tool with its flags, the settings keys",
  'demos-build': "`/demos-build <builder> <name>`: builds the demo installed and with its accounts, says where it answers and backs it up",
  'demos-build-a-demo': "A new session that builds a demo, checks it with Webship-js and backs it up before it is shown"},
 extra_rules="""- **A demo is kept.** Back it up before a change (`bash cmd-tools-backup-demo.sh <name>`), and
  remove it only when asked. Never print the password of an account when you report.
- **Check a demo before it is shown**: the front page answers, and its Webship-js suite passes.""")
