# QA Plan

## Project: BusTrack – Real-Time Commuter Bus Information System

---

## 1. Objectives
- Ensure all features meet their acceptance criteria before merging to `main`
- Catch bugs early through automated testing at multiple levels
- Maintain a documented defect log for full traceability

---

## 2. Test Levels

### Unit Testing
Tests individual functions or modules in isolation — no database, no network, no other components involved.

**Tool:** Pytest (Python)
**Scope:** `bus_utils.py` — route search, fare calculation, location formatting, bus status helpers

### Integration Testing
Tests how multiple components work together. Verifies that the API endpoints correctly interact with the database and return the right responses.

**Tool:** Pytest + test database (SQLite in-memory for tests)
**Scope:** `/api/routes/search`, `/api/bus/location/:id`, `/api/health`

### System Testing
End-to-end tests that simulate a real user interacting with the full running application — frontend through backend through database.

**Tool:** Manual testing + browser DevTools
**Scope:** Full user flows: search route → view schedule → trigger notification → report delay

---

## 3. Entry and Exit Criteria

### Entry Criteria (when testing can begin)
- Feature branch has been pushed and a PR has been opened
- Developer confirms the feature is code-complete locally
- At least 1 unit test exists for the new logic
- No syntax errors — code runs without crashing on startup

### Exit Criteria (when testing is considered done)
- All unit tests pass with 0 failures
- No S1 or S2 severity bugs remain open in the defect log
- Code coverage is at or above 70%
- QA Engineer has signed off on the PR
- CI pipeline shows green on GitHub Actions

---

## 4. Severity Levels

| Level | Name | Definition | Example | Response Time |
|-------|------|-----------|---------|--------------|
| S1 | Critical | System is down or data is lost/corrupted | App crashes on launch, database wiped | Immediate — fix before anything else |
| S2 | High | Major feature is completely broken | Bus location never loads, login fails | Within 24 hours |
| S3 | Medium | Feature works but behaves incorrectly | Wrong fare calculated, notification fires late | Within the current sprint |
| S4 | Low | Cosmetic or minor issue | Button misaligned, typo in UI text | Next sprint or backlog |

---

## 5. Test Environment
- **Local:** Each developer runs `pytest` before pushing
- **CI:** GitHub Actions runs all tests automatically on every push and PR
- **Staging:** Deployed to staging URL before merging to `main`

---

## 6. Test Coverage Target
- Minimum **70% code coverage** on backend logic
- All critical API endpoints must have at least **1 passing test**
- PRs that break existing tests will **not be merged**

---
