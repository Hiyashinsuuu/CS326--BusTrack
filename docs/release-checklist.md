# Release Checklist

## Project: BusTrack – Real-Time Commuter Bus Information System

---

## How to Use This Checklist
Go through every item before merging a release branch to `main` and deploying to production. A release is only approved if **all items are checked.**

---

## Pre-Release Checklist

### Code Quality
- [ ] All feature branches have been merged to `dev` via approved PRs
- [ ] No open PRs that are blocking this release
- [ ] Code has been reviewed by at least 1 other team member
- [ ] No hardcoded API keys, passwords, or secrets in the codebase
- [ ] Dead code and unused imports have been removed

### Testing
- [ ] All unit tests pass (`pytest` / `npm test` — 0 failures)
- [ ] Integration tests pass
- [ ] CI pipeline is green (GitHub Actions shows ✅)
- [ ] New features have at least 1 unit test covering the happy path
- [ ] All bugs marked S1 and S2 in the defect log are `Closed`

### Documentation
- [ ] `docs/release-notes.md` updated with this version's changes
- [ ] `docs/backlog.md` updated — completed stories marked done
- [ ] `README.md` reflects current setup/run instructions
- [ ] Any new environment variables documented

### Versioning
- [ ] Version number follows format: `v<major>.<minor>-<label>` (e.g. `v0.5-scm`)
- [ ] Git tag created: `git tag v0.5-scm`
- [ ] Tag pushed to GitHub: `git push origin v0.5-scm`

### Deployment
- [ ] `.env` variables are set correctly on the deployment platform (not local defaults)
- [ ] Database migrations applied successfully on staging
- [ ] App loads correctly on staging URL before promoting to production
- [ ] Health check endpoint returns `{ "status": "ok" }`: `GET /api/health`
- [ ] Rollback steps in `deployment-plan.md` reviewed and ready

### Post-Deploy Verification
- [ ] Production URL is accessible
- [ ] Core user flows tested manually on production (route search, map load, notifications)
- [ ] No console errors on page load
- [ ] Team notified of successful deployment in Discord

---

## Sign-Off

| Role | Name | Date | Approved |
|------|------|------|---------|
| Scrum Master | Keissha | | ☐ |
| QA Lead | [Member 4] | | ☐ |
| DevOps Lead | [Member 5] | | ☐ |
