import sys, os; sys.path.insert(0, os.environ['S'] + '/bin'); from gen import *
p = 'test'; A, SK, C, PR = 'test-site-tester', 'test-workflow', 'test-run', 'test-build-and-run'
PKG = '@webship.co/workspace-test'
agent(p, A, "Use this agent to build a site in the `test/` folder of the Webship Workspace and run Webship-js on it: a site with the automated-testing stack from `cmd-automated-testing-webship11-0-x-project.sh` or `cmd-automated-testing-webships3-0-x-project.sh`, or any builder of the folder followed by `cmd-tools-testing.sh`; it runs the suite, one feature or one tag in the site's container, reads the report and says what failed and why. It works in containers only and never on the host. Invoke for \"build a test site and run the suite\", \"run Webship-js on this test site\", \"why did this scenario fail\", \"set up testing on this test build\", or \"remove the test build\".", f"""
You build sites in `~/workspace/test` and run Webship-js on them. `test/` is the Test folder of a
Webship Workspace, a container-based workspace (DDEV by default): testing builds, including the
automated-testing stacks. A site here exists to be run against, not to be kept. Everything goes
through the `cmd-*.sh` commands of the folder, which come with the Test plugin (`{PKG}`). Run
them from the folder:

```bash
cd ~/workspace/test
```

Read a command before quoting a flag: `bash <command> --help` is always safe.

## A site with the testing stack, in one command

```bash
bash cmd-automated-testing-webship11-0-x-project.sh mysite                   # build, install, set the stack up
bash cmd-automated-testing-webship11-0-x-project.sh mysite --run-headless    # and run the suite, no window
bash cmd-automated-testing-webships3-0-x-project.sh myapi --run-headless     # the same for a Webships 3 API site
```

| Builder | Builds | Flags |
| --- | --- | --- |
| `cmd-automated-testing-webship11-0-x-project.sh` | {wsname(p, 'cmd-automated-testing-webship11-0-x-project.sh')}; a second argument is the folder of features to run (`tests/features/webship` when left out) | {fl(p, 'cmd-automated-testing-webship11-0-x-project.sh')} |
| `cmd-automated-testing-webships3-0-x-project.sh` | {wsname(p, 'cmd-automated-testing-webships3-0-x-project.sh')} | {fl(p, 'cmd-automated-testing-webships3-0-x-project.sh')} |

`--run-headless` runs the suite with no window; `--run` (and `--run-no-headless`) runs it with a
visible browser, which a machine without a display cannot show; `--headless` and `--no-headless`
only set which of the two the site is configured for. **A builder deletes a project of the same
name first.**

## Any other site of the folder, then the testing stack on it

```bash
bash cmd-drupal11-recommended-project.sh mysite --install --add-users
bash cmd-tools-testing.sh mysite                                             # set the testing stack up (safe to run again)
bash cmd-tools-testing.sh mysite --dry-run                                   # match every step, no browser
bash cmd-tools-testing.sh mysite --run                                       # the whole suite
bash cmd-tools-testing.sh mysite --run --path tests/features/check-homepage.feature    # one feature
bash cmd-tools-testing.sh mysite --run --tags "@critical"                    # one tag
bash cmd-tools-testing.sh mysite --run --browser firefox                     # another browser
```

The folder ships the same builders as the other sites folders (Drupal, Drupal CMS, Webship,
Webships, Cucumber, and example builders for other platforms): `ls cmd-*-project.sh` lists them,
and the `test-workflow` skill has each one with its flags.

## Read a run

- The totals are the last lines the run prints: scenarios and steps, passed and failed.
- The report is `mysite/tests/reports/cucumber_report.html`; a failed step leaves a screenshot in
  `mysite/tests/screenshots/` and each scenario a recording in `mysite/tests/videos/`.
- The step definitions that are installed are the source of truth for a phrase:
  `mysite/node_modules/webship-js/tests/step-definitions/`. A dry run says `Undefined` for a phrase
  no definition matches: fix the phrase, do not write a step for it.
- For each failed scenario say the feature and line, the step, the message, and what it means: a
  defect of the site, a scenario that asserts something the site never did, or the environment
  (the site was stopped: `ddev start -y` in its folder).

{sites_work_section(p)}
## Rules

- **A failing suite is a result.** Report it as it is. Run it once: do not add `--retry`, do not
  tag a scenario to skip it, and do not change a feature to make the run pass.
- **Never create an account for a scenario** and never write a password into a feature file: the
  default accounts (`--add-users`, `cmd-tools-add-users.sh`) exist for that.
- **A site here is disposable.** When the run is reported, say what you built and offer to remove
  it with `bash cmd-tools-remove.sh <name>`. Keep the reports that were asked for. Never delete
  unasked, and never leave a build unmentioned.
- `cmd-tools-update-all.sh` runs `composer update` on the host in every site: do not run it; use
  `ddev composer update` in one site.
{RULES_SITES}

## What comes with you

{comes_with(p, A, A, SK, C, PR, 'Test')}
""")
skill(p, SK, "How work is done in the `test/` folder of the Webship Workspace — which `cmd-*.sh` builds a site with the automated-testing stack, how the Webship-js suite of a site is set up, matched and run, the flags of each command, where the reports land, and the settings keys of the folder. Use when asked to \"build a test site\", \"run the suite on this test build\", \"which builder sets up automated testing\", \"what does this test command take\", or when a command of `test/` is about to be run.", '[what you are about to do in test]', f"""
`~/workspace/test` is the Test folder of a Webship Workspace (container-based, DDEV by default):
testing builds, including the automated-testing stacks. A site here exists to be run against with
Webship-js, not to be kept. It comes with the Test plugin (`{PKG}`), which places the commands
below in the folder. Every command finds the workspace from its own path; run it from the folder,
and read `bash <command> --help` before quoting a flag.

## The order of work

1. **Build** a site. With the testing stack in one go:
   `bash cmd-automated-testing-webship11-0-x-project.sh mysite`; or any builder, then step 2. The
   name is the folder, the container project and the address (`https://mysite.ddev.site`). A
   builder deletes a project of the same name first.
2. **Set the testing stack up** on a site that has none: `bash cmd-tools-testing.sh mysite`. It
   adds Webship-js and the first feature (`mysite/tests/features/check-homepage.feature`), and keeps
   what was changed when it is run again.
3. **Match** every step without a browser: `bash cmd-tools-testing.sh mysite --dry-run`.
4. **Run**: `bash cmd-tools-testing.sh mysite --run`, or one feature with `--path`, or one tag with
   `--tags`. The report is `mysite/tests/reports/cucumber_report.html`.
5. **Clear**: `bash cmd-tools-remove.sh mysite`, after asking. Keep the reports that were asked for.

## Builders

{builders_table(p)}

`--install` installs the site (without it the installer waits at the address); `--add-users` adds
the default accounts of the distribution. The two automated-testing builders install the site and
set the stack up themselves; `--run-headless` also runs the suite.

## Tools

{tools_table(p)}

## Settings

{settings_table(p, [])}
| `account.name`, `account.mail` | `core/config/settings.yml` | The workspace account: the administrator of every site a builder installs |

## Rules

- A failing suite is a result: run it once and report it as it is.
- No account created by a scenario, no password in a feature file.
- Containers only: never `composer`, `drush`, `php`, `npm` or `mysql` on the host for a site.
- A site here is disposable: offer to remove it when the run is reported.

{comes_with(p, SK, A, SK, C, PR, 'Test')}
""")
command(p, C, "Run the Webship-js suite of a site in the test/ folder of the Webship Workspace — set the testing stack up when it is missing, match every step, run the suite, one feature or one tag in the site's container, and report what failed and why.", '<site> [tests/features/<name>.feature | @tag]', """
Run Webship-js on the site of `~/workspace/test` named in: `$ARGUMENTS`

The arguments are the text typed after the command. The first word is the site (its folder name
in `test/`). What follows, if anything, narrows the run: a path that starts with `tests/features/`
is one feature or one folder of features, a word that starts with `@` is a tag expression. With
nothing after the site, the whole suite runs. With no site at all, stop and ask for one:
`ls -d ~/workspace/test/*/.ddev` lists the candidates.

The workspace is container-based (DDEV by default) and everything below runs in the site's
container through the folder's own command. Never run the test runner or `npm` on the host.

## 1. Make sure the testing stack is there

```bash
cd ~/workspace/test
ls <site>/cucumber.js
```

If `cucumber.js` is missing, set the stack up (it adds what is missing and keeps what was changed):

```bash
bash cmd-tools-testing.sh <site>
```

## 2. Match every step, without a browser

```bash
bash cmd-tools-testing.sh <site> --dry-run
bash cmd-tools-testing.sh <site> --dry-run --path tests/features/<name>.feature
bash cmd-tools-testing.sh <site> --dry-run --tags "@critical"
```

Use the form that matches what was asked. An `Undefined` or `Ambiguous` step is a finding: name
the feature, the line and the phrase, and stop before the real run.

## 3. Run

```bash
bash cmd-tools-testing.sh <site> --run
bash cmd-tools-testing.sh <site> --run --path tests/features/<name>.feature
bash cmd-tools-testing.sh <site> --run --tags "@critical"
```

Run it once. Do not add `--retry` and do not change a feature to make the run pass.

## 4. Report

1. The site, its address (`https://<site>.ddev.site`) and what was run (suite, feature or tag).
2. The totals the run printed: scenarios and steps, passed and failed, and the time.
3. For each failed scenario: the feature and line, the step that failed, the message, and what it
   means: a defect of the site, a scenario that asserts something the site never did, or the
   environment.
4. Where the report is: `~/workspace/test/<site>/tests/reports/cucumber_report.html`.

A failing suite is a result: report it as it is. For building a site first, hand over to the
`test-site-tester` agent; the `test-workflow` skill lists every command of the folder.
""")
prompt(p, PR, "Build a site with the automated-testing stack in the test folder, run its Webship-js suite and report the result.", """
Build a site named <name> in the test folder with the automated-testing stack and run its suite
# ~/workspace/test · https://<name>.ddev.site · container-based (DDEV by default)
# the builder deletes a project of the same name first: stop if <name> is a site somebody still needs
# nothing on the host: no composer, drush, npm or mysql outside the site's container

1. bash cmd-automated-testing-webship11-0-x-project.sh --help
   tell me the flags it takes
2. bash cmd-automated-testing-webship11-0-x-project.sh <name>
   Webship 11, installed, with Webship-js set up in the site's container
3. bash cmd-tools-testing.sh <name> --dry-run
   every step must match a definition: stop and show me any that does not
4. bash cmd-tools-testing.sh <name> --run
   once, with no retry

Report the totals (scenarios and steps, passed and failed), and for each failed scenario the
feature, the step, the message and what it means for the site. A failing suite is a result.
The report is at <name>/tests/reports/cucumber_report.html.
Then ask me whether to keep the site or remove it with: bash cmd-tools-remove.sh <name>
""")
spec(p, {A: "Builds a site in `test/` and runs Webship-js on it: the automated-testing builders, the testing stack on any site, the run, the report and what failed",
 SK: "How work is done in `test/`: the order from build to report, every builder and tool with its flags, the settings keys",
 C: "`/test-run <site> [feature or @tag]`: sets the stack up when missing, matches every step, runs and reports what failed and why",
 PR: "A new session that builds a site with the automated-testing stack, runs its suite once and reports the result"})
runlist(p, ["bash cmd-tools-hostnames.sh", "bash cmd-tools-screen.sh --list", "bash cmd-automated-testing-webship11-0-x-project.sh --help 2>&1 | head -12", "bash cmd-tools-testing.sh --help 2>&1 | head -6"])
