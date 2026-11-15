Design a change as a spec in the specs folder, stage by stage, before any code is written.

The launch line is for Claude Code, the default; the text between the triple quotes can be given to another AI CLI as it is.

```
claude --permission-mode bypassPermissions """
Design the change <change> for <workspace>/<project> as a spec, stage by stage
# ~/workspace/specs · one folder per change · container-based (DDEV by default)
# <workspace>/<project> is the folder of the project the change is for, for example dev/mysite
# no code is written in this session: the spec is the work

1. bash cmd-spdd.sh
   tell me whether a spec for this change exists already
2. bash cmd-spdd.sh <workspace>/<project> "<change>"
   tell me where 01-story.md is
3. ask me the questions of the story, one part at a time: the problem, the scope in and out,
   the definition of done, the acceptance criteria; write my answers into 01-story.md
4. bash cmd-spdd.sh <number> --spdd-action review
   tell me what is still missing
5. when I say the story is right: bash cmd-spdd.sh <number> --spdd-action analysis
   show me the analysis, and what in it contradicts the story

Stop after the analysis and wait for me: the canvas is asked for only when the analysis is right.
"""
```
