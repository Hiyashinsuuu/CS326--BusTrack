<!-- edited locally -->
# SCM Notes – Branch & Merge Log

## Project: BusTrack – Real-Time Commuter Bus Information System

---

## Branch Naming Convention

| Type | Format | Example |
|------|--------|---------|
| New feature | `feature/<short-name>` | `feature/real-time-map` |
| Bug fix | `bugfix/<bug-id-or-name>` | `bugfix/null-location-crash` |
| Hotfix (urgent production fix) | `hotfix/<name>` | `hotfix/fcm-key-exposed` |
| Release prep | `release/<version>` | `release/v0.5-scm` |

---

## Merge Conflict Simulation – April 23, 2026

### What Happened
Two team members edited `docs/backlog.md` at the same time on different branches:
- `feature/risk-management` updated US-07 to add a new acceptance criterion
- `feature/route-search` also edited US-07 to change the priority from High to Medium

When we tried to merge `feature/route-search` into `dev` after `feature/risk-management` was already merged, Git detected a conflict in `backlog.md`.

### Conflict Output
```
<<<<<<< HEAD (dev)
| US-07 | Admin can update bus schedules | High | 5 | Admin dashboard saves and publishes changes within 1 minute. |
=======
| US-07 | Admin can update bus schedules | Medium | 5 | Admin can edit schedule entries. |
>>>>>>> feature/route-search
```

### How We Resolved It
1. Opened `backlog.md` in VS Code — Git highlighted the conflict
2. Discussed as a team: kept **High** priority (agreed it's a core feature) and merged both acceptance criteria
3. Final resolved version:
```
| US-07 | Admin can update bus schedules | High | 5 | Admin dashboard saves and publishes changes within 1 minute; admin can edit, delete, and add schedule entries. |
```
4. Ran `git add docs/backlog.md` then `git commit -m "resolve: merge conflict in backlog US-07 priority and criteria"`
5. Pushed and opened PR → reviewed → merged

### Lesson Learned
Communicate before editing shared files. Assign one owner per document per sprint to avoid overlapping edits.

---

## PR Log

| PR # | Branch | Description | Status |
|------|--------|-------------|--------|
| #1 | `feature/risk-management` | Add risk register and GitHub PR/issue templates | ✅ Merged |
| #2 | `feature/route-search` | Add route search endpoint and UI component | ✅ Merged |
| #3 | `bugfix/null-location-crash` | Fix BUG-001 null GPS location crash | ✅ Merged |
| #4 | `release/v0.5-scm` | Sprint 1 release prep | ✅ Merged |
