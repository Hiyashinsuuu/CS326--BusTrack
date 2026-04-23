# Risk Register

## Project: BusTrack – Real-Time Commuter Bus Information System

**Risk Score Formula:** `Likelihood (1–5) × Impact (1–5)`  
**Score Levels:** Low (1–8) | Medium (9–14) | High (15–25)

---

| # | Risk | Likelihood (1–5) | Impact (1–5) | Score | Level | Mitigation Plan | Owner |
|---|------|:-:|:-:|:-:|---|---|---|
| R-01 | GPS/real-time bus data API is unreliable or rate-limited | 3 | 5 | 15 | High | Use a fallback polling interval; cache last known location; display "last updated" timestamp to users. | Backend Dev |
| R-02 | Team member drops out or becomes unavailable before deadline | 2 | 5 | 10 | Medium | Document all tasks clearly on GitHub; cross-train members on critical features; Scrum Master redistributes tasks immediately. | Scrum Master |
| R-03 | Merge conflicts causing broken code on the main branch | 4 | 4 | 16 | High | Enforce branch protection rules; require at least 1 PR review before merging; communicate frequently in Discord before touching shared files. | All Developers |
| R-04 | Deployment platform outage (e.g., Vercel/Render goes down) | 2 | 4 | 8 | Low | Keep a backup deployment ready on an alternative platform (e.g., Railway); document rollback steps in `deployment-plan.md`. | DevOps Lead |
| R-05 | Scope creep — adding too many features before core is stable | 4 | 3 | 12 | Medium | Strictly follow the sprint backlog; new features must go through backlog refinement first; Scrum Master blocks unplanned work. | Scrum Master |
| R-06 | Database schema changes break existing API endpoints | 3 | 4 | 12 | Medium | Use database migrations (e.g., Alembic/Django migrations); never edit schema directly in production; test migrations on a staging DB first. | Backend Dev |
| R-07 | Security vulnerability — exposed API keys in GitHub repo | 2 | 5 | 10 | Medium | Use `.env` files excluded via `.gitignore`; rotate any accidentally pushed keys immediately; add `git-secrets` pre-commit hook. | DevOps Lead |
| R-08 | Low test coverage leads to undetected bugs in production | 3 | 4 | 12 | Medium | Set a minimum coverage target of 70%; QA Engineer reviews test results before each sprint review; block PR merges if tests fail. | QA Engineer |
| R-09 | Poor internet connectivity at demo/presentation time | 3 | 3 | 9 | Medium | Prepare a recorded demo video as backup; ensure the deployed system works on mobile data; test on multiple networks before demo day. | DevOps Lead |
| R-10 | Miscommunication leads to duplicate or missing features | 3 | 3 | 9 | Medium | Assign one GitHub Issue per feature; use PR descriptions to clarify what was built; hold a quick sync before every coding session. | Scrum Master |
