import sys, os; sys.path.insert(0, os.environ['S'] + '/bin'); from gen import *

def sites_plugin(p, title, A, C, PR, purpose, keep, agent_desc, build_examples, skill_use, order, cmd_desc, cmd_hint, cmd_body, pr_sentence, pr_text, summaries, extra_rules='', build_note='', tools_extra=None):
    k = key(p); SK = f'{k}-workflow'; PKG = pkg(p)['name']
    has_update_all = 'cmd-tools-update-all.sh' in cmds(p)
    upd = "- `cmd-tools-update-all.sh` runs `composer update` on the host in every site: do not run it; use\n  `ddev composer update` in one site.\n" if has_update_all else ''
    agent(p, A, agent_desc, f"""
You build and look after the sites of `~/workspace/{k}`, the {title} folder of a Webship Workspace:
a container-based workspace (DDEV by default). {purpose} Everything goes through the `cmd-*.sh`
commands of the folder, which come with the {title} plugin (`{PKG}`). Run them from the folder:

```bash
cd ~/workspace/{k}
```

Read a command before quoting a flag: `bash <command> --help` is always safe.

{sites_build_section(p, build_examples, build_note)}
{sites_test_section(p)}
{sites_work_section(p)}
## Rules

{extra_rules.strip()}
{upd}{RULES_SITES}

## What comes with you

{comes_with(p, A, A, SK, C, PR, title)}
""")
    skill(p, SK, skill_use, f'[what you are about to do in {k}]', f"""
`~/workspace/{k}` is the {title} folder of a Webship Workspace (container-based, DDEV by default).
{purpose} It comes with the {title} plugin (`{PKG}`), which places the commands below in the
folder. Every command finds the workspace from its own path; run it from the folder, and read
`bash <command> --help` before quoting a flag.

## The order of work

{order.strip()}

## Builders

{builders_table(p)}

`--install` installs the site (without it the installer waits at the address); `--add-users` adds
the default accounts of the distribution. A builder deletes a project of the same name first.

## Tools

{tools_table(p, tools_extra)}

## Settings

{settings_table(p, [])}
| `account.name`, `account.mail` | `core/config/settings.yml` | The workspace account: the administrator of every site a builder installs |

## Rules

- Containers only: never `composer`, `drush`, `php`, `npm` or `mysql` on the host for a site. In the
  site's folder: `ddev composer …`, `ddev drush …`, `ddev export-db --file=…`, `ddev start -y`,
  `ddev stop` (no `-y`).
- Never write database settings into `settings.php`.
- {keep}

{comes_with(p, SK, A, SK, C, PR, title)}
""")
    command(p, C, cmd_desc, cmd_hint, cmd_body)
    prompt(p, PR, pr_sentence, pr_text)
    spec(p, summaries)
    runlist(p, ["bash cmd-tools-hostnames.sh", "bash cmd-tools-screen.sh --list"])
