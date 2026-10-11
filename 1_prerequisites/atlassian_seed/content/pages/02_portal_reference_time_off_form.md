# Employee Portal reference: Time Off form

## Where to find it

Navigation path: **Employee Portal > Time Off > My Requests**.

## Screenshots

*Captured on build 0.9. Labels can change before release. Check them against the final build.*

### My Requests page

[Screenshot: 01_my_requests.png]

### Time Off form

[Screenshot: 02_time_off_form.png]

### Request submitted

[Screenshot: 03_request_pending.png]

## Form fields

| Field | Required | Notes |
|---|---|---|
| Leave type | Yes | Vacation or Personal |
| Start date | Yes | |
| End date | Yes | |
| Note to manager | No | Up to 200 characters |

## Approval rules

| Request length | Approval | Submit by |
|---|---|---|
| 1 to 2 days | Automatic, if balance is sufficient | No minimum notice |
| 3 or more days | Manager, within 2 business days | 5 business days before start |

## Statuses

[Screenshot: 04_status_badges.png]

- **Pending:** waiting for the manager.
- **Approved:** confirmed. HR is updated automatically.
- **Declined:** the manager declined. A reason is shown.
- **Cancelled:** you cancelled the request.

## Notifications

The employee gets an email when the status changes. There is no separate step to tell HR.

Helper text on the form: "Requests of 3 or more days need manager approval."
