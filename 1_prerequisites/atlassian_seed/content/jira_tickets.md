# Jira tickets for project BRT (Brightside Time Off)

Create the epic first. Then create the other three tickets with the epic as their parent.

---

## 1. Epic

**Summary:** Time Off requests move to the Employee Portal

**Description:**

### Goal

Employees request vacation and personal days in the Employee Portal instead of by email, starting 2026-11-01.

### Documentation scope

* Update the employee how-to page.
* Verify the menu path and UI labels.
* Publish a release note.

### Reference pages

* Confluence: Time Off requests: feature overview
* Confluence: Employee Portal reference: Time Off form
* Confluence: Documentation plan: Time Off update

---

## 2. Story (parent: the epic)

**Summary:** Update the 'How to request time off' page

**Description:**

### Why

The current page tells employees to email their manager and then forward the email to HR. Both steps are retired.

### Acceptance criteria

* The page uses the Employee Portal Time Off form.
* The page states the approval rules for 1-2 days and 3 or more days.
* The page states the 5-business-day notice rule for 3 or more days.
* Every step ends with an outcome ("You see ...").
* Every fact comes from the Confluence reference pages or from a Jira ticket.
* Anything uncertain carries a verification note.

### Sources

* Confluence: Time Off requests: feature overview
* Confluence: Employee Portal reference: Time Off form
* Confluence: Documentation plan: Time Off update (editorial rules)

---

## 3. Task (parent: the epic)

**Summary:** Verify Time Off menu path and UI labels before release

**Description:**

### Why

The feature overview says the team has not confirmed the portal menu path. The screenshots on the reference page were captured on build 0.9, and labels can change before release.

### To do

* Confirm the menu path with product.
* Compare every label in the screenshots with the final build.
* Record any change as a comment on this ticket, and list the screenshots to replace.

### Labels seen on build 0.9

* Menu path: Employee Portal > Time Off > My Requests
* Button on the My Requests page: Request leave
* Form fields: Leave type, Start date, End date, Note to manager
* Submit button: Submit

---

## 4. Story (parent: the epic)

**Summary:** Write the release note for Time Off in the portal

**Description:**

### Why

Employees and managers need a short note explaining the change before 2026-11-01.

### Acceptance criteria

* Names the change (email to portal form) and the effective date.
* States what did not change (same balance, unpaid leave needs HR written approval).
* Links to the how-to page.
* Uses only verified labels. Check the comments on the verification ticket first.

### Sources

* Confluence: Time Off requests: feature overview
