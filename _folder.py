import sys, os; sys.path.insert(0, os.environ['S'] + '/bin'); from gen import *

def folder_plugin(p, title, names, purpose, agent_desc, agent_body, rules, skill_desc, order, cmd, pr, summaries,
                  tools_extra=None, settings_extra=(), settings_rows='', run=(), builders=False, skill_more='', what='works in'):
    """names = (agent, command, prompt); cmd = (description, hint, body); pr = (sentence, text)."""
    k = key(p); A, C, PR = names; SK = f'{k}-workflow'; PKG = pkg(p)['name']
    has_cmds = bool(cmds(p))
    through = (f"Everything goes through the `cmd-*.sh` commands of the folder, which come with the {title} plugin\n(`{PKG}`). Run them from the folder:" if has_cmds
               else f"The folder comes with the {title} plugin (`{PKG}`); it ships no `cmd-*.sh` of its own: the work is done\non the folder's page of the dashboard and on the files themselves. The folder is:")
    agent(p, A, agent_desc, f"""
You {what} `~/workspace/{k}`, the {title} folder of a Webship Workspace: a container-based
workspace (DDEV by default). {purpose} {through}

```bash
cd ~/workspace/{k}
```
{chr(10) + 'Read a command before quoting a flag: `bash <command> --help` is always safe.' + chr(10) if has_cmds else ''}
{agent_body.strip()}

## Rules

{rules.strip()}
- **Never restart the dashboard** or anything shared to make your own work go through.
- Say what you ran and what it printed. If a command fails, show the line that failed; do not
  retry with other flags until something passes.

## What comes with you

{comes_with(p, A, A, SK, C, PR, title)}
""")
    tables = ''
    if builders: tables += f"## Builders\n\n{builders_table(p, builders if isinstance(builders, dict) else None)}\n\n"
    if has_cmds: tables += f"## Commands\n\n{tools_table(p, tools_extra)}\n\n"
    skill(p, SK, skill_desc, f'[what you are about to do in {k}]', f"""
`~/workspace/{k}` is the {title} folder of a Webship Workspace (container-based, DDEV by default).
{purpose} It comes with the {title} plugin (`{PKG}`){', which places the commands below in the folder. Every command finds the workspace from its own path; run it from the folder, and read `bash <command> --help` before quoting a flag' if has_cmds else ', which places the folder, its settings file and its docs; it ships no `cmd-*.sh` of its own'}.

## The order of work

{order.strip()}

{tables}{skill_more.strip() + chr(10) + chr(10) if skill_more else ''}## Settings

{settings_table(p, settings_extra)}{chr(10) + settings_rows.strip() if settings_rows else ''}

## Rules

{rules.strip()}

{comes_with(p, SK, A, SK, C, PR, title)}
""")
    command(p, C, *cmd)
    prompt(p, PR, *pr)
    spec(p, summaries)
    runlist(p, list(run))
