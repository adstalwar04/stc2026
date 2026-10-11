# CLAUDE.md: STC India Annual Summit 2026 - AI Workshop

This repo holds a hands-on workshop for technical communicators: skills, agents, hooks, plugins, and MCP, taught in VS Code with GitHub Copilot Free and a free Atlassian site. One use case runs through it: updating Brightside Co.'s "How to request time off" page.

This file is on the public repo's `main` branch and documents all three repos. Read it before changing anything.

## Where things live

The workshop is split across **one public repo and two private repos**, so the facilitator and participant material is not visible to everyone.

| Repo / branch | Visibility | Folder it holds | Audience | Purpose |
|---|---|---|---|---|
| `adstalwar04/stc2026`, branch `main` | Public | `1_prerequisites/`, `README.md`, `CLAUDE.md`, `.gitignore` | Participants, before the session | Setup guides and the Atlassian content participants create. Entry point and this file. |
| `adstalwar04/stc2026`, branch `gh-pages` | Public | `0_promo/`, root `index.html` | Public marketing | The single-slide promo page, served by GitHub Pages. |
| `adstalwar04/stc2026-participants`, branch `main` | **Private** | `2_participants/`, root `README.md` | Registered attendees | Handout, starter workspace, finished module files, plugin, cheat sheet. Access is by invitation (repo collaborators). |
| `adstalwar04/stc2026-facilitator`, branch `main` | **Private** | `3_facilitator/`, root `README.md` | Facilitator only | Run sheets, session listing, trust-challenge reveal. |

**Live promo page:** https://adstalwar04.github.io/stc2026/ (GitHub Pages, served from the root of `gh-pages`).

Notes:

- `gh-pages` is an **orphan branch**: it shares no history with `main`. Do not merge it into `main`.
- The public repo had `participants` and `Facilitator` branches earlier. They were moved to the private repos above and deleted from the public repo. Commits made public before the move may stay reachable by SHA, so assume the reveal was seen. Do not recreate those branches in the public repo.
- Docs refer to `1_prerequisites/`, `2_participants/`, and `3_facilitator/` as sibling folders. Because they are now in different repos, a working copy needs all three side by side in one folder. The two private repos' READMEs say so. `3_facilitator/seed_atlassian.py` reads `1_prerequisites/atlassian_seed/`.
- GitHub Pages is on and serves `gh-pages`. A push to that branch republishes the page in about a minute.
- To let an attendee see participant material, add them as a collaborator on `stc2026-participants`. Never add attendees to `stc2026-facilitator`.

## What each folder contains

### `stc2026`, branch `main` (public)

- `README.md`: the attendee-facing entry point: the title, the workshop page link, the order of the prerequisite guides, and a pointer to the `participants` branch. It deliberately has no folder map and does not mention the `Facilitator` branch.
- `1_prerequisites/README.md`: the order of the three guides (about 90 minutes in total).
- `1_prerequisites/SETUP_GUIDE.md`: install VS Code and Python 3, sign in to Copilot Free, trust the workspace, check settings, troubleshoot.
- `1_prerequisites/ATLASSIAN_SETUP.md`: free Atlassian site, Jira project `BRT`, Confluence space `BRT`, connect the Atlassian MCP server.
- `1_prerequisites/PREREQUISITE_CREATE_CONFLUENCE_AND_JIRA.md`: two paste-in prompts that make the AI create 3 Confluence pages and 4 Jira tickets, plus a manual route.
- `1_prerequisites/check_setup.py`: tests the participant's computer. Run from the workshop root.
- `1_prerequisites/atlassian_seed/content/`: Markdown for the 3 pages and the Jira tickets.
- `1_prerequisites/atlassian_seed/confluence_pages/`, `jira/issues.json`: the same content as Confluence storage HTML and JSON. Used by the facilitator's seed script.
- `1_prerequisites/atlassian_seed/screenshots/`: 4 mock portal screenshots. `_screenshot_src/` holds the HTML they were rendered from.

### `stc2026`, branch `gh-pages` (public)

- `index.html`: redirect to the promo page.
- `0_promo/workshop_promo.html`: **the built page. One self-contained file**: mascots and logo are embedded, so it needs no internet.
- `0_promo/README.md`: what viewers can do and how to rebuild.
- `0_promo/_build/promo_template.html`: **the source to edit**. Never edit `workshop_promo.html` by hand.
- `0_promo/_build/build_promo.py`: embeds the images into the template and writes `workshop_promo.html`. Needs Python 3 and Pillow.
- `0_promo/_build/mascots/`, `stc_india_logo.svg`: the source images (the mascots are 8 PNGs, about 8 MB).

### `stc2026-participants` (private, branch `main`)

- `2_participants/PARTICIPANT_HANDOUT.md`: the two-hour run sheet for participants. Generated from the facilitator run sheet with the facilitator notes removed.
- `2_participants/brightside_workspace/`: the starter project (source material and the stale page).
- `2_participants/apply_module.py`: copies one module's finished files into a workspace. Modules 1, 2, 3, 4, 4a, 5.
- `2_participants/solution/`: every finished file (instructions, skill, agents, hooks, MCP server, final page). It is a complete, working workspace.
- `2_participants/plugin/brightside-docs-kit/`: the same pieces packaged as a Claude-format plugin that VS Code reads.
- `2_participants/CONCEPT_CHEATSHEET.md`: the same ideas in other AI tools.

### `stc2026-facilitator` (private, branch `main`)

- `3_facilitator/WORKSHOP_2HR.md`: the 2-hour run sheet with facilitator notes.
- `3_facilitator/WORKSHOP_GUIDE.md`: the 3.5-hour full edition, with the concept detail and a 3-hour cut.
- `3_facilitator/SESSION_LISTING.md`: website text (synopsis, audience level, objectives, prerequisites).
- `3_facilitator/trust_challenge_evidence.md` and `reveal_comment.md`: the late-label twist. Keep sealed from participants.
- `3_facilitator/seed_atlassian.py`: optional script that builds the Atlassian content through the API. It reads `1_prerequisites/atlassian_seed/` from the main branch layout.

## Rules for changing things

1. **Keep the facts in sync.** The same facts appear in `source_material/` (workspace and solution copies), the Markdown pages in `atlassian_seed/content/`, the Confluence HTML, the screenshots, and the final page. Change all of them together.
2. **Keep the numbers in sync.** The 2-hour agenda totals 120 minutes and the full agenda 210. Request budgets (17 and 29 per pair, plus about 2 for the prerequisite) appear in `WORKSHOP_2HR.md`, `PARTICIPANT_HANDOUT.md`, and `3_facilitator/README.md`. `SESSION_LISTING.md` and the promo page state about 90 minutes of prerequisites.
3. **`PARTICIPANT_HANDOUT.md` mirrors `WORKSHOP_2HR.md`.** Edit the run sheet first, then regenerate or edit the handout to match, removing the facilitator voice.
4. **The skill, agents, and hooks exist twice**: in `solution/.github/` and in `plugin/brightside-docs-kit/`. Keep them equal. The plugin's reviewer agent has no handoff on purpose.
5. **Paths matter.** Docs refer to `1_prerequisites/`, `2_participants/`, and `3_facilitator/` by those names and to commands like `python3 ../apply_module.py 1`. Do not rename folders without updating every doc and script (`check_setup.py` and `seed_atlassian.py` locate files relative to the workshop root).
6. **Do not spread the reveal.** `trust_challenge_evidence.md` and `reveal_comment.md` stay in the private facilitator repo only. Never copy them into the public repo or the participants repo.
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
4. Commit the template and the rebuilt `workshop_promo.html` together, and push. GitHub Pages republishes automatically.

The page has a white header band (STC India logo, summit name, date, venue, and a **Reserve a seat** button linking to `https://stcindia.org/events/2026/annual-summit/register`) and a white footer band (Hands-on Workshop by Amandeep Singh Talwar, with a LinkedIn link). Event: STC India Annual Summit 2026, 4 and 5 December 2026, The Chancery Pavilion, Bengaluru.
