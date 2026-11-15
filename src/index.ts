/**
 * The Specs workspace for Webship Workspace: the `specs/` folder as a plugin.
 *
 * What the package carries is placed by the installer from the manifest (the folder's settings file,
 * its commands, its docs and its AI items, each in the folder of its kind) and listed by --activate; the dashboard draws the workspace from the
 * settings file like any other. Nothing to register at run time yet: this is where the folder's own
 * rail buttons, row menus or assistant context would go.
 */

import type { PluginApi } from '@webship.co/workspace-plugin-api';

export const WORKSPACE_KEY = 'specs';

/** The AI items the installer places, each in the workspace folder of its kind (ai/ in this package). */
export const AGENTS = ['specs-author'];
export const SKILLS = ['specs-workflow'];
export const AI_COMMANDS = ['specs-start'];
export const PROMPTS = ['specs-design-a-change'];

export function register(api: PluginApi): void {
  api.addAssistantContext(() => `The specs/ workspace is the Specs workspace (a plugin, @webship.co/workspace-specs); its commands are the cmd-*.sh scripts in that folder. It comes with AI items for work in this folder: the agent \`specs-author\` (ai-agents/), the skill \`specs-workflow\` (ai-skills/), the command \`/specs-start\` (ai-commands/) and the prompt \`specs-design-a-change\` (ai-prompts/).`);
}
