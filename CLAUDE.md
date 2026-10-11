# CLAUDE.md: STC India Annual Summit 2026 - AI Workshop

This repo holds a hands-on workshop for technical communicators: skills, agents, hooks, plugins, and MCP, taught in VS Code with GitHub Copilot Free and a free Atlassian site. One use case runs through it: updating Brightside Co.'s "How to request time off" page.

The repo is **private**. Each part of the workshop lives on its own branch so you can share a branch with the right audience. Read this file before changing anything.

## Branch map

| Branch | Folder it holds | Audience | Purpose |
|---|---|---|---|
| `main` | `1_prerequisites/`, `README.md`, `CLAUDE.md`, `.gitignore` | Participants, before the session | Setup guides and the Atlassian content participants create. Also the entry point (`README.md`) and this file. |
| `gh-pages` | `0_promo/`, root `index.html` | Public marketing | The single-slide promo page. `index.html` redirects to `0_promo/workshop_promo.html`. |
| `participants` | `2_participants/` | Participants, during the session | Handout, starter workspace, finished module files, plugin, cheat sheet. |
| `Facilitator` | `3_facilitator/` | Facilitator only | Run sheets, session listing, trust-challenge reveal. **Never merge into another branch.** |

Notes on the branches:

- `participants`, `gh-pages`, and `Facilitator` are **orphan branches**: they share no history with `main` and contain only their folder. Do not merge them into each other or into `main`.
- The branch name is `Facilitator` with a capital F, as requested.
- GitHub Pages on a private repo needs a paid GitHub plan. If Pages is off, the promo page still opens locally as a file.

## What each folder contains

### `main`

- `README.md`: the project title, the four-folder map, who gets what, and a quick path for the facilitator.
- `1_prerequisites/README.md`: the order of the three guides (about 90 minutes in total).
- `1_prerequisites/SETUP_GUIDE.md`: install VS Code and Python 3, sign in to Copilot Free, trust the workspace, check settings, troubleshoot.
- `1_prerequisites/ATLASSIAN_SETUP.md`: free Atlassian site, Jira project `BRT`, Confluence space `BRT`, connect the Atlassian MCP server.
- `1_prerequisites/PREREQUISITE_CREATE_CONFLUENCE_AND_JIRA.md`: two paste-in prompts that make the AI create 3 Confluence pages and 4 Jira tickets, plus a manual route.
- `1_prerequisites/check_setup.py`: tests the participant's computer. Run from the workshop root.
- `1_prerequisites/atlassian_seed/content/`: Markdown for the 3 pages and the Jira tickets.
- `1_prerequisites/atlassian_seed/confluence_pages/`, `jira/issues.json`: the same content as Confluence storage HTML and JSON. Used by the facilitator's seed script.
- `1_prerequisites/atlassian_seed/screenshots/`: 4 mock portal screenshots. `_screenshot_src/` holds the HTML they were rendered from.

### `gh-pages`

- `index.html`: redirect to the promo page.
- `0_promo/workshop_promo.html`: **the built page. One self-contained file**: mascots and logo are embedded, so it needs no internet.
- `0_promo/README.md`: what viewers can do and how to rebuild.
- `0_promo/_build/promo_template.html`: **the source to edit**. Never edit `workshop_promo.html` by hand.
- `0_promo/_build/build_promo.py`: embeds the images into the template and writes `workshop_promo.html`. Needs Python 3 and Pillow.
- `0_promo/_build/mascots/`, `stc_india_logo.svg`: the source images (the mascots are 8 PNGs, about 8 MB).

### `participants`

- `2_participants/PARTICIPANT_HANDOUT.md`: the two-hour run sheet for participants. Generated from the facilitator run sheet with the facilitator notes removed.
- `2_participants/brightside_workspace/`: the starter project (source material and the stale page).
- `2_participants/apply_module.py`: copies one module's finished files into a workspace. Modules 1, 2, 3, 4, 4a, 5.
- `2_participants/solution/`: every finished file (instructions, skill, agents, hooks, MCP server, final page). It is a complete, working workspace.
- `2_participants/plugin/brightside-docs-kit/`: the same pieces packaged as a Claude-format plugin that VS Code reads.
- `2_participants/CONCEPT_CHEATSHEET.md`: the same ideas in other AI tools.

### `Facilitator`

- `3_facilitator/WORKSHOP_2HR.md`: the 2-hour run sheet with facilitator notes.
- `3_facilitator/WORKSHOP_GUIDE.md`: the 3.5-hour full edition, with the concept detail and a 3-hour cut.
- `3_facilitator/SESSION_LISTING.md`: website text (synopsis, audience level, objectives, prerequisites).
- `3_facilitator/trust_challenge_evidence.md` and `reveal_comment.md`: the late-label twist. Keep sealed from participants.
- `3_facilitator/seed_atlassian.py`: optional script that builds the Atlassian content through the API. It reads `1_prerequisites/atlassian_seed/` from the main branch layout.

## Rules for changing things

1. **Keep the facts in sync.** The same facts appear in `source_material/` (workspace and solution copies), the Markdown pages in `atlassian_seed/content/`, the Confluence HTML, the screenshots, and the final page. Change all of them together.
2. **Keep the numbers in sync.** The 2-hour agenda totals 120 minutes and the full agenda 210. Request budgets (17 and 29 per pair, plus about 2 for the prerequisite) appear in `WORKSHOP_2HR.md`, `PARTICIPANT_HANDOUT.md`, and `Facilitator/README.md`. `SESSION_LISTING.md` and the promo page state about 90 minutes of prerequisites.
3. **`PARTICIPANT_HANDOUT.md` mirrors `WORKSHOP_2HR.md`.** Edit the run sheet first, then regenerate or edit the handout to match, removing the facilitator voice.
4. **The skill, agents, and hooks exist twice**: in `solution/.github/` and in `plugin/brightside-docs-kit/`. Keep them equal. The plugin's reviewer agent has no handoff on purpose.
5. **Paths matter.** Docs refer to `1_prerequisites/`, `2_participants/`, and `3_facilitator/` by those names and to commands like `python3 ../apply_module.py 1`. Do not rename folders without updating every doc and script (`check_setup.py` and `seed_atlassian.py` locate files relative to the workshop root).
6. **Never leak the reveal.** `trust_challenge_evidence.md` and `reveal_comment.md` stay on `Facilitator` only. Do not copy them to `main` or `participants`.
7. **Do not commit** `.DS_Store`, `__pycache__`, or tokens. No real company data anywhere: the workshop is fictional.
8. **Use the GitHub noreply address for commits** (set repo-local `user.name` and `user.email`). Do not use a work email.

## Known unknowns (verify before each run)

- Whether the Atlassian Rovo MCP server works on the Atlassian **Free** plan, and which URL is current (`https://mcp.atlassian.com/v2/mcp`; older `.../v1/mcp/authv2` also appears in Atlassian docs).
- Copilot Free limits (about 50 chat requests a month) and which models are available.
- VS Code preview features: hooks (`.github/hooks/*.json`), agent plugins (`chat.pluginLocations`), and the exact tool names for the reviewer agent's `tools:` list.
- The two paste-in Atlassian prompts were written but not run against a live site. `seed_atlassian.py` was tested only against a local mock of the Atlassian APIs.

## What was tested

- `check_setup.py`, `apply_module.py` (all modules), the hook scripts, and the local MCP server pass on macOS with Python 3.9.
- The promo page was checked in headless Chrome at four desktop sizes and a phone width.
- Not tested: anything that needs a signed-in Copilot session or a live Atlassian site.

## Promo page: how to change it

1. Check out `gh-pages`.
2. Edit `0_promo/_build/promo_template.html`.
3. Run `python3 0_promo/_build/build_promo.py`.
4. Commit the template and the rebuilt `workshop_promo.html` together.

The page has a white header band (STC India logo, summit name, date, venue, and a **Reserve a seat** button linking to `https://stcindia.org/events/2026/annual-summit/register`) and a white footer band (Hands-on Workshop by Amandeep Singh Talwar, with a LinkedIn link). Event: STC India Annual Summit 2026, 4 and 5 December 2026, The Chancery Pavilion, Bengaluru.
