import os, sys; sys.path.insert(0, os.environ['S'] + '/specs'); from _sites import *
p = 'sandboxes'
sites_plugin(p, 'Sandboxes', 'sandboxes-site-builder', 'sandboxes-try', 'sandboxes-try-and-clear',
 "Sandboxes are throwaway experiments: a site is built here to try one thing, and nothing here is expected to survive.",
 "A sandbox is cleared when the question is answered, after asking: `bash cmd-tools-remove.sh mysite`.",
 "Use this agent to spin up a throwaway site in the `sandboxes/` folder of the Webship Workspace to try one thing, and to clear it afterwards, with the `cmd-*.sh` commands the Sandboxes folder ships (the Drupal, Drupal CMS, Webship, Webships and Cucumber builders, `cmd-tools-testing.sh`, `cmd-tools-clone.sh`, `cmd-tools-remove.sh`, `cmd-tools-reclaim.sh`). It works in containers only and never on the host. Invoke for \"spin up a quick sandbox\", \"try this module on a throwaway Drupal site\", \"clone this site into sandboxes to experiment\", \"clean up the sandboxes\", or \"remove the sandbox\".",
 """bash cmd-drupal11-recommended-project.sh mysite --install --profile minimal
bash cmd-drupal11-recommended-project.sh mysite --install --require "drupal/token:~1.0" --enable "token"
bash cmd-drupalcms2-x-project.sh mysite --install --add-users""",
 "How work is done in the `sandboxes/` folder of the Webship Workspace — which `cmd-*.sh` builds a throwaway site, the flags of each command, how the experiment is tested with Webship-js, and how a sandbox is removed and its disk reclaimed, with the settings keys of the folder. Use when asked to \"spin up a sandbox\", \"try this on a throwaway site\", \"which builder is there for a quick Drupal site\", \"clean up the sandboxes\", or when a command of `sandboxes/` is about to be run.",
 """1. **Build** the smallest site that answers the question:
   `bash cmd-drupal11-recommended-project.sh mysite --install --profile minimal`, with `--require`
   and `--enable` for the package under trial. The name is the folder, the container project and
   the address (`https://mysite.ddev.site`). A builder deletes a project of the same name first.
2. **Try** the thing, in the site's container: `ddev composer …`, `ddev drush …` in `mysite/`.
3. **Prove** it when it matters: `bash cmd-tools-testing.sh mysite`, then
   `bash cmd-tools-testing.sh mysite --dry-run` and `bash cmd-tools-testing.sh mysite --run`.
4. **Clear**: `bash cmd-tools-remove.sh mysite`, after asking. `bash cmd-tools-remove.sh --orphans`
   and `bash cmd-tools-reclaim.sh` report what was left behind; nothing is removed without `--apply`.""",
 "Spin up a throwaway site in the sandboxes/ folder of the Webship Workspace to try one thing: pick the smallest builder, build, say the address, and offer to remove it when the question is answered.",
 '<what to try> [name]',
 """
Spin up a sandbox in `~/workspace/sandboxes` for: `$ARGUMENTS`

The arguments are the text typed after the command: what is to be tried, in words (a package, a
version, a setting). The last word is the name of the sandbox when it is a single lowercase word
of letters and digits; otherwise choose a short one and say it. The workspace is container-based
(DDEV by default): the builder runs the site in its own container, nothing on the host.

## 1. Choose the smallest builder that answers the question

```bash
cd ~/workspace/sandboxes
grep -H "^# workspace-name:" cmd-*-project.sh
bash cmd-drupal11-recommended-project.sh --help
```

A plain Drupal question: `cmd-drupal11-recommended-project.sh` with `--profile minimal`. A Drupal
CMS question: `cmd-drupalcms2-x-project.sh`. A Webship question: `cmd-webship11-0-x-project.sh`.
Say which one and why.

## 2. Make sure the name is free

```bash
ls -d ~/workspace/*/<name> 2>/dev/null
ddev list | grep -w <name>
```

A builder deletes a project of the same name first. If the name is taken, choose another.

## 3. Build

```bash
bash cmd-drupal11-recommended-project.sh <name> --install --profile minimal
```

With the builder that was chosen; for a package under trial add `--require "<package>"` and
`--enable "<module>"` where the builder has them. Run it once. If it fails, show the line that
failed and stop.

## 4. Report, and offer to clear

The builder, the address (`https://<name>.ddev.site`), what was installed for the trial, and what
was found. Then ask whether to keep the sandbox or remove it:

```bash
bash cmd-tools-remove.sh <name>
```

Never remove unasked. For more than one experiment, hand over to the `sandboxes-site-builder`
agent; the `sandboxes-workflow` skill lists every command of the folder.
""",
 "Spin up a throwaway site in the sandboxes folder, try one thing on it, report, and clear it.",
 """
Try <what> on a throwaway site named <name> in the sandboxes folder, then clear it
# ~/workspace/sandboxes · https://<name>.ddev.site · container-based (DDEV by default)
# the builder deletes a project of the same name first: stop if <name> is a site somebody still needs
# nothing on the host: no composer, drush, npm or mysql outside the site's container

1. bash cmd-drupal11-recommended-project.sh --help
   tell me the flags it takes
2. bash cmd-drupal11-recommended-project.sh <name> --install --profile minimal
   add --require and --enable for the package under trial
3. try <what> in the site's container (ddev composer, ddev drush, in the folder <name>)
   tell me what you ran and what it printed
4. bash cmd-tools-testing.sh <name>
   bash cmd-tools-testing.sh <name> --run
   only if the result is to be proven with Webship-js

Report what was found, in a few lines.
Then ask me whether to keep the sandbox or remove it with: bash cmd-tools-remove.sh <name>
""",
 {'sandboxes-site-builder': "Spins up a throwaway site in `sandboxes/` to try one thing, tests it when it matters, and clears it afterwards",
  'sandboxes-workflow': "How work is done in `sandboxes/`: build small, try, prove, clear; every builder and tool with its flags, the settings keys",
  'sandboxes-try': "`/sandboxes-try <what to try> [name]`: picks the smallest builder, builds the sandbox, reports and offers to remove it",
  'sandboxes-try-and-clear': "A new session that builds a throwaway site, tries one thing on it, reports and clears it"},
 extra_rules="""- **A sandbox is disposable, and still not yours to delete unasked.** When the question is
  answered, say what you built and offer to remove it with `bash cmd-tools-remove.sh <name>`.
- **Build the smallest thing that answers the question**: `--profile minimal` before `standard`,
  one site before two.
- `bash cmd-tools-reclaim.sh` is a report until `--apply` is added: never add it unasked.""")
