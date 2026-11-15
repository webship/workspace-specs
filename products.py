import os, sys; sys.path.insert(0, os.environ['S'] + '/specs'); from _folder import *
p = 'products'
RULES = """- **A product is a real repository.** Never rebuild, reset or remove a checkout; work on a
  branch, and back the checkout up (`bash cmd-tool-backup-product.sh <name>`) before a risky change.
- **Green before a push.** The checks the product declares, then its pipeline on this machine. A red
  job is fixed, never hidden: no skipped check, no job allowed to fail.
- **Containers only** (DDEV by default): never `composer`, `drush`, `php` or `npm` on the host for a
  product; the checks and the pipeline run in containers.
- `bash cmd-tools-reclaim.sh` is a report until `--apply` is added: never add it unasked."""
folder_plugin(p, 'Products', ('products-maintainer', 'products-check', 'products-green-gate'),
 "Products are the distributions, profiles and packages this workspace ships: real repositories, where a build is a product and not an experiment.",
 "Use this agent to work on a product in the `products/` folder of the Webship Workspace — a distribution, profile or package kept as a real git checkout — and bring it to green before a push: its code-quality checks with `cmd-tools-checks.sh`, its GitLab CI pipeline on this machine with `cmd-tools-gitlab-ci-local.sh`, a branch as a git worktree with `cmd-tools-clone.sh`, a backup with `cmd-tool-backup-product.sh`. It works in containers only and never on the host. Invoke for \"run the checks of this product\", \"run the pipeline locally before I push\", \"why is this job red\", \"make a worktree for this branch\", or \"back up this product\".",
 """
## What a product declares, and whether it holds

```bash
bash cmd-tools-checks.sh myproduct --list                  # every check, the script it runs, where it would run: runs nothing
bash cmd-tools-checks.sh myproduct                         # every declared check; one failure does not hide the rest
bash cmd-tools-checks.sh myproduct --only js,css           # some of them: format, js, css, yaml, spelling, types, php, twig, e2e
bash cmd-tools-checks.sh myproduct --skip spelling
bash cmd-tools-checks.sh myproduct --fail-fast             # stop at the first red one
```

`--install` installs the package's dependencies first when they are missing; it is off by default
because an install runs the package's own scripts. `--e2e` adds the browser suite, which needs a
running site.

## The pipeline, on this machine, before a push

```bash
bash cmd-tools-gitlab-ci-local.sh myproduct --doctor       # the runner, the container engine, the access the templates need
bash cmd-tools-gitlab-ci-local.sh myproduct --list         # the jobs and their stages
bash cmd-tools-gitlab-ci-local.sh myproduct                # the whole pipeline
bash cmd-tools-gitlab-ci-local.sh myproduct phpcs          # one job, by its name
bash cmd-tools-gitlab-ci-local.sh myproduct --slim         # the product's own .gitlab-ci-local.yml: the subset that runs locally
bash cmd-tools-gitlab-ci-local.sh myproduct --variable DRUPAL_CORE=11.4.0
```

It ends with GREEN or RED. Green means every job that ran passed: a job that cannot run on this
machine is not a pass, and is gated on the remote pipeline.

## A branch beside the checkout, a backup, a long run

```bash
bash cmd-tools-clone.sh myproduct --to myproduct-fix --worktree --branch fix-the-thing   # one repository, a branch per folder
bash cmd-tool-backup-product.sh myproduct                  # the checkout as an archive, into backups/products/
bash cmd-tools-screen.sh checks-myproduct --run "bash cmd-tools-checks.sh myproduct"
bash cmd-tools-screen.sh checks-myproduct --follow
bash cmd-tools-screen.sh --list
```

A product gets into the folder with `git clone`, in `~/workspace/products`: the folder ships no
builder, and no remove command either.
""", RULES,
 "How work is done in the `products/` folder of the Webship Workspace — how a product (a distribution, profile or package kept as a git checkout) is checked with the code-quality checks it declares, how its GitLab CI pipeline is run on this machine before a push, how a branch gets its own worktree and a checkout its backup, with the flags of each command and the settings keys of the folder. Use when asked to \"run the checks of this product\", \"run the pipeline locally\", \"make a worktree for a branch\", \"back up the product\", or when a command of `products/` is about to be run.",
 """1. **See what the product declares**: `bash cmd-tools-checks.sh myproduct --list`. It runs nothing.
2. **Work on a branch**; for a second branch at the same time,
   `bash cmd-tools-clone.sh myproduct --to myproduct-fix --worktree`.
3. **Run the checks**: `bash cmd-tools-checks.sh myproduct`, or some with `--only`.
4. **Run the pipeline on this machine**: `bash cmd-tools-gitlab-ci-local.sh myproduct --doctor`
   once, then `bash cmd-tools-gitlab-ci-local.sh myproduct` (or `--slim`).
5. **Push when it is green**, and gate on the remote pipeline what could not run here.""",
 ("Run the code-quality checks a product of the products/ folder of the Webship Workspace declares, and say what is red and why, before anything is pushed.", '<product> [checks, comma separated]', """
Check the product of `~/workspace/products` named in: `$ARGUMENTS`

The arguments are the text typed after the command: the first word is the product (its folder
name in `products/`), and a second word is a comma separated list of checks to run instead of
all of them (`format`, `js`, `css`, `yaml`, `spelling`, `types`, `php`, `twig`, `e2e`). With no
product, stop and ask for one: `ls ~/workspace/products` lists the candidates. The workspace is
container-based (DDEV by default); nothing is installed on the host for a check.

## 1. The plan

```bash
cd ~/workspace/products
bash cmd-tools-checks.sh <product> --list
```

It prints every check, the script the package declares for it and where it would run, and runs
nothing. A check that is "not declared" is not a failure: say which are declared.

## 2. Run

```bash
bash cmd-tools-checks.sh <product>
bash cmd-tools-checks.sh <product> --only <checks>
```

Use the second form when checks were named. If the plan says the dependencies are not installed,
say so and ask before adding `--install`: an install runs the package's own scripts.

## 3. Report

For each check: passed, failed or not declared; for a failed one the first lines of what it
printed and the file it points at. Do not fix anything unasked, and never skip a check to make
the run pass. For the pipeline (`cmd-tools-gitlab-ci-local.sh`), hand over to the
`products-maintainer` agent; the `products-workflow` skill lists every command of the folder.
"""),
 ("Bring a product to green before a push: the checks it declares, then its pipeline on this machine.", """
Bring the product <product> of the products folder to green before it is pushed
# ~/workspace/products/<product> · a git checkout · container-based (DDEV by default)
# nothing is pushed, merged, reset or removed in this session

1. bash cmd-tools-checks.sh <product> --list
   tell me which checks the product declares
2. bash cmd-tools-checks.sh <product>
   every declared check; tell me which are red, with the first lines of each
3. bash cmd-tools-gitlab-ci-local.sh <product> --doctor
   stop and tell me if the runner or the container engine is missing
4. bash cmd-tools-gitlab-ci-local.sh <product> --list
5. bash cmd-tools-gitlab-ci-local.sh <product>
   if the whole pipeline cannot run here, say why and run: bash cmd-tools-gitlab-ci-local.sh <product> --slim

Report: the checks (passed, failed, not declared), the pipeline (GREEN or RED, which jobs ran,
which could not run here). A red job is a result: do not hide it, do not allow it to fail.
Then ask me whether to fix what is red.
"""),
 {'products-maintainer': "Works on a product (a real checkout) in `products/` and brings it to green before a push: its checks, its pipeline on this machine, a worktree for a branch, a backup",
  'products-workflow': "How work is done in `products/`: see what is declared, check, run the pipeline locally, push when green; every command with its flags, the settings keys",
  'products-check': "`/products-check <product> [checks]`: prints the plan, runs the declared checks and says what is red and why",
  'products-green-gate': "A new session that runs a product's checks and its pipeline on this machine and reports green or red"},
 run=["bash cmd-tools-screen.sh --list", "bash cmd-tools-gitlab-ci-local.sh --help 2>&1 | head -8", "mkdir -p pkgx && echo '{\"name\":\"pkgx\",\"scripts\":{\"lint:js\":\"echo ok\"}}' > pkgx/package.json && bash cmd-tools-checks.sh pkgx --list ; rm -rf pkgx"], what='work on the products of')
