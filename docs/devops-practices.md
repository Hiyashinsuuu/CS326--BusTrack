# DevOps Practices

## Project: BusTrack – Real-Time Commuter Bus Information System

---

## 1. Automation

| Practice | Tool | How We Use It |
|----------|------|--------------|
| Automated testing | pytest + GitHub Actions | Every push triggers `pytest tests/` — no manual test runs needed |
| Automated deployment | peaceiris/actions-gh-pages | Merging to `main` auto-deploys to GitHub Pages — no manual FTP/upload |
| Automated smoke test | curl in GitHub Actions | After deploy, pipeline checks the live URL returns HTTP 200 |
| Branch protection | GitHub Settings | PRs to `main` must pass CI before merge is allowed |

---

## 2. Collaboration

| Practice | Tool | How We Use It |
|----------|------|--------------|
| Pull Requests | GitHub | All changes go through PRs — no direct pushes to `main` |
| PR Template | `.github/pull_request_template.md` | Standardizes what every PR must include (summary, tests, screenshots) |
| Issue Templates | `.github/ISSUE_TEMPLATE/` | Bug reports and feature requests follow a consistent format |
| Branch naming | Convention: `feature/`, `bugfix/`, `hotfix/` | Makes branch purpose immediately clear to all team members |
| Code review | GitHub PR reviews | At least 1 approval required before merge |

---

## 3. Monitoring & Feedback

| Practice | Tool | How We Use It |
|----------|------|--------------|
| CI status badges | GitHub Actions | Team sees ✅/❌ on every push in real time |
| Smoke tests | curl HTTP check | Catches broken deployments within 30 seconds of going live |
| Defect log | `docs/defect-log.md` | All bugs tracked from open → in progress → closed |
| Release notes | `docs/release-notes.md` | Every version documents what changed and what's known |

---

## 4. Feedback Loop

```
Code written locally
       ↓
Push to feature branch
       ↓
GitHub Actions runs tests (< 2 min feedback)
       ↓
PR opened → teammate reviews → approved
       ↓
Merge to main → auto-deploy triggers
       ↓
Smoke test verifies live site (30 sec)
       ↓
Team notified in Discord
       ↓
User reports issues → defect log → next sprint
```

---

## 5. Cloud / DevOps Improvement — Docker Support

To make BusTrack portable and environment-independent, we added a `Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install pytest
CMD ["pytest", "tests/"]
```

**Why this matters:**
- Any team member can run `docker build . && docker run bustrack` without installing Python locally
- Consistent environment between local dev and CI
- Foundation for future deployment to cloud platforms (Railway, Fly.io, AWS ECS)

---

## 6. Sprint Retrospective — DevOps Lessons Learned

| What Worked | What To Improve |
|-------------|----------------|
| GitHub Actions caught broken tests before merge | Add test coverage reporting (codecov) |
| PR template kept reviews consistent | Add automated linting (flake8/eslint) to CI |
| Smoke test caught a 404 deploy issue immediately | Add uptime monitoring (e.g., UptimeRobot) |
| Branch naming made history readable | Enforce branch naming via GitHub ruleset |
