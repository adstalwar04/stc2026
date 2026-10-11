# Setup guide: VS Code + GitHub Copilot Free

**Time:** 30 minutes (45 if you also install Python), plus about 40 minutes for the two Atlassian guides.
**Cost:** $0. Copilot Free needs a GitHub account and no credit card.
**You finish with:** VS Code signed in to Copilot, the workshop folder open, and a passing `check_setup.py`.

Do this at least one day before the workshop. Sign-in and corporate-policy problems take longest to fix.

> Facts about plans, limits, and preview features come from the official GitHub and VS Code docs as of October 2026. They change often. Re-check the three items marked **[verify]** the day before.

---

## Step 0: Check what your employer allows (5 minutes)

On a work laptop, three things can block this workshop:

| Check | How | If blocked |
|---|---|---|
| You can install software | Try the VS Code download in Step 1 | Ask IT for "VS Code" and "Python 3". Both are common approved tools. |
| GitHub Copilot is allowed | Ask IT, or try Step 3 | Use a personal laptop, or follow the "No Copilot" path at the end. |
| MCP servers and preview features are allowed | Try Module 4 and 5 | Facilitator demos these; you still do Modules 1, 2, 3. |

**Privacy rule:** the workshop uses only the fictional Brightside material. Never paste real company content into a free AI tool unless your employer allows it.

---

## Step 1: Install VS Code (5 minutes)

Download from <https://code.visualstudio.com/download> and install with the defaults.

- **Windows:** run the installer. Tick "Add to PATH" if offered.
- **macOS:** drag Visual Studio Code to Applications. Then open it, press `Cmd+Shift+P`, and run **Shell Command: Install 'code' command in PATH**.
- **Version:** use the latest stable release. Check with **Help > About**. Update with **Help > Check for Updates**. Agent, skills, hooks, and plugin features change monthly, and older versions miss them.

---

## Step 2: Install Python 3 (10 minutes)

The workshop's hooks and MCP server are small Python scripts. They use only the standard library. You install nothing else.

1. Open a terminal (Windows: PowerShell. macOS: Terminal).
2. Run `python3 --version` (macOS) or `python --version` (Windows).
3. If you see `Python 3.9` or newer, skip to Step 3.
4. Otherwise install it:
   - **Windows:** download from <https://www.python.org/downloads/>. On the first screen, **tick "Add python.exe to PATH"**. Then reopen PowerShell.
   - **macOS:** `brew install python`, or download the macOS installer from python.org.

**Windows trap:** if `python` opens the Microsoft Store, Windows is showing a placeholder. Install from python.org, or turn the alias off in **Settings > Apps > Advanced app settings > App execution aliases**.

---

## Step 3: Sign in to Copilot Free (5 minutes)

1. Create a GitHub account at <https://github.com/signup> if you do not have one.
2. Open VS Code. Select the **Chat** icon in the title bar, or press `Ctrl+Alt+I` (Windows/Linux) or `Ctrl+Cmd+I` (macOS).
3. Select **Sign in** (or **Set up Copilot**) and follow the browser prompts. Accept **Copilot Free** when offered.
4. Return to VS Code. The chat box should accept a message.

**[verify]** Copilot Free limits: 2,000 inline suggestions and about 50 chat requests per month, plus a base allowance of AI credits that chat and agent use draw from. Lighter models use the allowance more slowly. Check <https://github.com/features/copilot/plans>.

**Do not waste your requests.** Send at most 3 test messages before the workshop. Workshop sessions are paired so two people share one account's requests.

### Smoke test (counts as 1 request)

1. In the chat box, open the mode picker and choose **Agent**.
2. Open the model picker and choose the lightest model listed.
3. Send: `Reply with the single word: ready`
4. You see the reply `ready`.

---

## Step 4: Get the workshop folder (2 minutes)

1. Copy the workshop folder (the one that holds `1_prerequisites` and `2_participants`) to your computer, for example `Documents/STC India Annual Summit 2026 - AI Workshop`.
2. Open a terminal in the workshop folder and run the checker:

```
python3 1_prerequisites/check_setup.py      # macOS / Linux
python 1_prerequisites/check_setup.py       # Windows
```

3. Read the output. Fix every `FAIL` using the arrow hint under it. `WARN` lines are optional.
4. Note the line that starts `In your .vscode/mcp.json, set "command" to`. You use it in Module 4.

---

## Step 5: Open the workspace and trust it (2 minutes)

1. In VS Code choose **File > Open Folder** and select `2_participants/brightside_workspace`.
2. When VS Code asks "Do you trust the authors?", choose **Yes, I trust the authors**.
   Hooks and workspace MCP servers do not run in Restricted Mode, so this step matters.
3. Open `source_material/02_policy_update.md` to confirm you see the Brightside policy text.

You work in `brightside_workspace` for the whole workshop. The `solution` folder holds finished copies. Peek only if you are stuck.

---

## Step 6: Check four settings (3 minutes)

Open Settings (`Ctrl+,` or `Cmd+,`), search for each name, and confirm:

| Setting | Expected | Used in |
|---|---|---|
| `chat.useHooks` | On (default) | Module 5 |
| `chat.plugins.enabled` | On | Module 6 **[verify]** |
| `chat.mcp.autostart` | `newAndOutdated` (default) | Module 4 |
| `chat.useClaudeHooks` | Off (default). Leave it off. | Avoids loading unrelated hooks |

If a setting is greyed out with a "managed by your organization" note, your employer controls it. Tell the facilitator which one.

---

## Step 7: Know where things are (2 minutes)

You work with these places all day:

| What | Where |
|---|---|
| Chat view | Right side, or `Ctrl+Alt+I` / `Ctrl+Cmd+I` |
| Mode picker | Bottom of the chat box: Ask, Edit, Agent, plus your custom agents |
| Model picker | Next to the mode picker |
| Tools picker | Tools icon in the chat box ("Configure Tools") |
| Command Palette | `Ctrl+Shift+P` / `Cmd+Shift+P` |
| Chat customizations | Gear icon in the Chat view, or Command Palette > type `Chat:` |
| MCP servers | Command Palette > `MCP: List Servers` |

---

## Step 8: Set up Atlassian (40 minutes, two separate guides)

Module 4 connects VS Code to a free Jira and Confluence site that holds the workshop's reference pages and tickets. Follow `ATLASSIAN_SETUP.md` (create a free account with a **personal** email and connect VS Code), then `PREREQUISITE_CREATE_CONFLUENCE_AND_JIRA.md` (create the Confluence pages and Jira tickets with an AI prompt).

If you cannot, or your employer blocks it, skip this step. You watch the Atlassian parts and keep everything else.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| No Chat icon | Copilot extension hidden or old VS Code | Update VS Code. Extensions view > search "GitHub Copilot Chat" > Install. |
| "Sign in" loops | Browser blocked the callback | Use **Accounts** (bottom-left person icon) > Sign in with GitHub. Allow the pop-up. |
| Chat says you reached a limit | Free quota used | Pair with a neighbour for the rest of the session. Resets monthly. |
| Agent mode missing from the picker | Organization policy | Ask IT whether "agent mode" is enabled for your Copilot plan. |
| MCP server shows an error | `python3` not found | Put the command from `check_setup.py` into `.vscode/mcp.json`. Run **MCP: List Servers** > **Show Output**. |
| Hook never fires | Restricted Mode, or hooks off | Trust the workspace. Check `chat.useHooks`. |
| Hook script fails on Windows | `python` is the Store alias | See the Windows trap in Step 2. |
| Atlassian server will not sign in | Work SSO or a blocked pop-up | Use a private browser window and the throwaway account. See `ATLASSIAN_SETUP.md`. |
| Skill does not appear after `/` | Wrong folder name | The folder name must equal `name:` in `SKILL.md`, all lowercase, hyphens only. |

---

## No Copilot? Fallback paths

- **Personal laptop:** the cleanest fix. Use a personal GitHub account.
- **Another IDE:** Cursor supports skills, agents, hooks, and MCP. Its free tier is smaller, so you mostly watch. Copy the contents of `2_participants/solution/.github` to Cursor's equivalent folders; see `2_participants/CONCEPT_CHEATSHEET.md`.
- **Gemini API key:** Google AI Studio issues a free key. Some editors accept it as a bring-your-own-key model.
- **Watch-and-follow:** the facilitator demos every module. You read the files in `2_participants/solution/` and still leave with working knowledge.

---

## Facilitator: try it yourself first (60 minutes)

Run the full workshop alone before you teach it. This is the quickest way to find what breaks on your version.

1. Complete Steps 0 to 7 above.
2. Open `3_facilitator/WORKSHOP_GUIDE.md`. Do Modules 1 to 6 in order, using the "Check" line at the end of each one.
3. Also do `ATLASSIAN_SETUP.md` on a **fresh** free site. Confirm the Atlassian MCP server connects on the Free plan; Atlassian's public pages do not say.
4. Keep a list of: any menu name that differs, any setting that was missing, any tool name that did not resolve in the Tools picker.
5. Update the **[verify]** items and the `tools:` line in `2_participants/solution/.github/agents/doc-reviewer.agent.md` to match what your Tools picker shows.
6. Do the trust challenge in `3_facilitator/WORKSHOP_GUIDE.md` last. It needs the work from every module.

Request budget for a full solo run: about 30 chat requests. On Copilot Free, spread a rehearsal over two sessions, or use a paid or trial Copilot account for rehearsal only.
