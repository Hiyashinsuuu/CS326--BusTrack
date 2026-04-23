# Defect Log

## Project: BusTrack – Real-Time Commuter Bus Information System

---

| Bug ID | Title | Reported By | Date Reported | Severity | Status | Description | Steps to Reproduce | Expected Result | Actual Result | Fix Applied | Date Closed |
|--------|-------|-------------|---------------|----------|--------|-------------|-------------------|----------------|---------------|-------------|-------------|
| BUG-001 | Bus location API returns `null` for inactive buses | QA Engineer | April 22, 2026 | Medium | Closed | When a bus has not sent a GPS ping in over 10 minutes, the `/api/bus/location/:id` endpoint returns `null` instead of a proper "unavailable" status, causing the frontend to crash with a TypeError. | 1. Start the app. 2. Call `/api/bus/location/99` where bus 99 has no recent ping. 3. Observe frontend map component. | API returns `{ status: "unavailable", last_seen: "..." }` and map shows a greyed-out marker. | Frontend throws `TypeError: Cannot read properties of null (reading 'lat')` and map crashes. | Added a null check in `getBusLocation()`. If `location` is null, return `{ status: "unavailable", last_seen: timestamp }`. Frontend updated to handle `status: "unavailable"` gracefully by showing a greyed marker with a tooltip. | April 22, 2026 |

---

## Bug Status Legend
| Status | Meaning |
|--------|---------|
| Open | Bug reported, not yet assigned |
| In Progress | Developer is working on the fix |
| In Review | Fix is in a PR, awaiting review |
| Closed | Fix merged and verified by QA |
