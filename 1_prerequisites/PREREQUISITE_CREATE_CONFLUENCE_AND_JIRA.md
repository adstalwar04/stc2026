# Prerequisite: create the Confluence pages and Jira tickets

**Time:** 20 minutes. **Do it:** at least 24 hours before the workshop.
**You finish with:** 3 Confluence pages (with 4 screenshots) and 1 Jira epic with 3 tickets, all in your own free Atlassian site.

You use your own AI assistant to create them. That is also your first real use of MCP: an AI writing to Jira and Confluence on your behalf.

**Before you start, you need:**

1. A free Atlassian site with Jira project `BRT` and Confluence space `BRT`. See `ATLASSIAN_SETUP.md`, Steps 1 to 3.
2. The Atlassian MCP server connected in VS Code. See `ATLASSIAN_SETUP.md`, Step 4. Check: the Tools picker lists `atlassian` tools.
3. The **workshop folder** open in VS Code: **File > Open Folder** and choose the workshop folder (the one that holds `1_prerequisites` and `2_participants`). Trust the workspace.
4. Chat in **Agent** mode, lightest model.

> **Use a throwaway personal Atlassian account, never a work account.** This step gives the AI permission to create things in your Atlassian site.

**No Atlassian MCP, or it will not connect?** Skip to "Manual route" at the bottom. It takes about 25 minutes and needs no AI.

---

## Part 1: Create the three Confluence pages (6 minutes, 1 chat request)

Paste this into the chat:

```
Use the atlassian tools. Create three Confluence pages in the space with key BRT ("Brightside Time Off") on my Atlassian site.

Create one page for each file in 1_prerequisites/atlassian_seed/content/pages/:
- The page title is the first line of the file, without the "# ".
- The page body is everything after that first line.
- Copy the body exactly as written. Do not rewrite, summarise, shorten, or add anything. Keep the Markdown formatting (headings, lists, tables).
- Lines like [Screenshot: 01_my_requests.png] stay as plain text. I will add the images myself.

Do not create, edit, or delete anything else. When you finish, list each page title with its link.
```

**What happens:** the AI reads three files and asks permission to create each page. Read each approval prompt. Check that it names space `BRT` and one of the three titles, then approve.

**Check:** open Confluence, space `BRT`. You see these three pages:

| Page title |
|---|
| Time Off requests: feature overview |
| Employee Portal reference: Time Off form |
| Documentation plan: Time Off update |

Open each page. Compare it with the file. Headings, lists, and tables should match. If the AI changed any wording, fix it by hand or ask it to `Replace the body of that page with the exact text of <file>.`

---

## Part 2: Add the four screenshots yourself (5 minutes)

AI tools cannot upload images through MCP, so you add them. Open **Employee Portal reference: Time Off form** and choose **Edit**.

For each `[Screenshot: ...]` line:

1. Select the line and delete it.
2. Drag the file from `1_prerequisites/atlassian_seed/screenshots/` onto that spot in the page. Or type `/image` and choose **Upload**.
3. Add alt text if the editor offers it (select the image, then **Add alt text**). Describe it, for example "My Requests page showing 12 days remaining and a Request leave button".

| Replace this line | With this file |
|---|---|
| `[Screenshot: 01_my_requests.png]` | `01_my_requests.png` |
| `[Screenshot: 02_time_off_form.png]` | `02_time_off_form.png` |
| `[Screenshot: 03_request_pending.png]` | `03_request_pending.png` |
| `[Screenshot: 04_status_badges.png]` | `04_status_badges.png` |

Select **Publish**.

**Check:** four screenshots show on the page, each under the right heading.

---

## Part 3: Create the epic and three tickets (6 minutes, 1 chat request)

Paste this into the chat:

```
Use the atlassian tools. In Jira project BRT ("Brightside Time Off") create four issues from the file 1_prerequisites/atlassian_seed/content/jira_tickets.md.

1. First create the Epic.
2. Then create the other three issues (types are named in the file) with the epic as their parent.

For each issue use the Summary exactly as written. Use the Description exactly as written, keeping the headings and bullets. Do not rewrite, summarise, or add anything.

Do not create, edit, or delete anything else. When you finish, list each issue key, type, and summary.
```

**What happens:** the AI reads the file and asks permission to create each issue. Approve each after checking that the project is `BRT`.

**Check:** open Jira, project `BRT`. You see:

| Type | Summary |
|---|---|
| Epic | Time Off requests move to the Employee Portal |
| Story | Update the 'How to request time off' page |
| Task | Verify Time Off menu path and UI labels before release |
| Story | Write the release note for Time Off in the portal |

The three tickets sit under the epic. In the **Backlog** or **Board** view, group by epic, or open the epic and look at **Child issues**.

**If the tickets are not under the epic:** open each ticket, find the **Parent** field, and set it to the epic. This can happen if your project is company-managed rather than team-managed.

---

## Final check (2 minutes)

Paste this into the chat. It uses read tools only:

```
Using the atlassian tools, read the Confluence page "Employee Portal reference: Time Off form" and the Jira epic "Time Off requests move to the Employee Portal" with its child issues. Tell me: (1) how many images the page has, (2) how many child issues the epic has, and (3) the exact button label the first screenshot shows.
```

**Expected:** 4 images (or "4 attachments"), 3 child issues, and the label **Request leave**.

Note that label. It becomes important during the workshop.

---

## What went wrong? (common problems)

| Problem | Fix |
|---|---|
| The AI asks which space or project | Answer `BRT`. If your key is different, use yours and say so. |
| The AI paraphrased the text | Say: `Replace the body with the exact text of <file>.` Or paste it yourself. |
| The page looks flat, with no headings | Use the editor toolbar to apply headings. Or use the manual route for that page. |
| The AI wants to create extra pages or issues | Decline the approval. Repeat the prompt, adding: `Create nothing except what I listed.` |
| Free chat requests are running out | Use the manual route for Part 3. |
| The tool-call approval names a different site | Decline. You may be signed in to the wrong Atlassian account. |

**Safe use:** read every approval prompt. The AI can create and edit things in your Atlassian site. Approve only what this page tells you to do. Afterwards, you can remove the app authorization in your Atlassian account (**Security** settings).

---

## Manual route (about 25 minutes, no AI)

### Confluence pages

1. In space `BRT` choose **Create**. Choose a blank page.
2. Type the title from line 1 of the file in `1_prerequisites/atlassian_seed/content/pages/`.
3. Open the file in VS Code. Select everything after line 1. Copy it. Paste into the page body. Confluence converts pasted Markdown headings, lists, and tables in most editors. If it does not, apply headings and lists with the toolbar.
4. Publish. Repeat for the other two pages.
5. Add the four screenshots as in Part 2.

### Jira tickets

1. In project `BRT` choose **Create**. Set **Work type** to **Epic**.
2. Copy the Summary and Description from `1_prerequisites/atlassian_seed/content/jira_tickets.md`. Create.
3. Create each of the other three. Set the **Parent** (or **Epic**) field to the epic.
