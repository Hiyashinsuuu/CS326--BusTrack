# Support Plan

## Project: BusTrack – Real-Time Commuter Bus Information System

---

## 1. Issue Reporting Process

Users and team members can report issues through the following channels:

| Channel | Who Uses It | Purpose |
|---------|------------|---------|
| GitHub Issues | Team members / developers | Bug reports, feature requests, technical issues |
| In-app "Report a Problem" form | End users (commuters) | Reporting delayed buses, app errors, wrong info |
| Email: `support@bustrack.app` | End users | General inquiries and escalations |
| Discord `#bugs` channel | Internal team only | Quick internal alerts and discussion |

### How to File a GitHub Issue
1. Go to the repository → **Issues** → **New Issue**
2. Select the appropriate template: `Bug Report` or `Feature Request`
3. Fill in: Title, Description, Steps to Reproduce, Expected vs Actual behavior
4. Assign to the relevant team member
5. Add labels: `bug`, `enhancement`, `high-priority`, etc.

---

## 2. Response Times

| Severity | Definition | First Response | Resolution Target |
|----------|-----------|---------------|-----------------|
| Critical | App is down / data is completely wrong | Within 2 hours | Within 24 hours |
| High | Major feature broken but app is accessible | Within 4 hours | Within 48 hours |
| Medium | Minor bug, cosmetic issue, performance lag | Within 24 hours | Within 1 week |
| Low | UI polish, non-urgent requests | Within 48 hours | Next sprint |

---

## 3. Support Workflow

```
User reports issue
       ↓
QA Engineer triages and assigns severity
       ↓
Assigned developer creates a fix branch (fix/bug-id-description)
       ↓
Fix is tested locally + unit test added
       ↓
PR opened → reviewed → merged to dev
       ↓
Deployed to staging → QA verifies fix
       ↓
Merged to main → deployed to production
       ↓
Bug marked ✅ Closed in defect-log.md
```

---

## 4. Known Limitations (Documented)
- Real-time location accuracy depends on the bus's GPS hardware — we cannot guarantee sub-10-meter precision
- Push notifications require users to grant browser/app notification permission
- The system currently supports Metro Manila routes only

---

## 5. Maintenance Schedule
- **Weekly:** Review open GitHub Issues; close resolved ones
- **Per Sprint:** Defect log reviewed and updated during sprint retrospective
- **Monthly:** Check for dependency updates (`npm audit` / `pip audit`); apply security patches
