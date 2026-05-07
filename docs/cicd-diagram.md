# CI/CD Pipeline Diagram

## Project: BusTrack – Real-Time Commuter Bus Information System

---

## Pipeline Overview

```
Developer pushes to main
          │
          ▼
┌─────────────────────┐
│      TRIGGER        │
│  Push to main OR    │
│  Pull Request       │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│    JOB 1: TEST      │
│  - Checkout code    │
│  - Setup Python 3.11│
│  - pip install pytest│
│  - pytest tests/    │
│                     │
│  ✅ Pass → continue │
│  ❌ Fail → stop     │
└────────┬────────────┘
         │  (only if push to main)
         ▼
┌─────────────────────┐
│    JOB 2: DEPLOY    │
│  - Checkout code    │
│  - Deploy to        │
│    GitHub Pages     │
│    via GITHUB_TOKEN │
│                     │
│  ✅ Pass → continue │
│  ❌ Fail → stop     │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  JOB 3: SMOKE TEST  │
│  - Wait 30 seconds  │
│  - curl live URL    │
│  - Check HTTP 200   │
│                     │
│  ✅ 200 → Pipeline  │
│         complete!   │
│  ❌ Non-200 → fail  │
└─────────────────────┘
```

---

## Pipeline Stages Explained

| Stage | Trigger | What Happens | Success Condition |
|-------|---------|-------------|------------------|
| Test | Every push / PR | Runs all 5 pytest unit tests | 0 failures |
| Deploy | Push to `main` only | Publishes site to GitHub Pages | Deployment accepted |
| Smoke Test | After deploy | Sends HTTP GET to live URL | Returns HTTP 200 |

---

## Secrets & Environment Variables

| Secret | Where Set | Purpose |
|--------|-----------|---------|
| `GITHUB_TOKEN` | Auto-provided by GitHub Actions | Authenticates the deploy step |

---

## Branch Rules
- `main` → triggers full pipeline (test → deploy → smoke test)
- `dev` / `feature/*` → triggers test only (no deploy)
- PRs to `main` → must pass tests before merge is allowed
