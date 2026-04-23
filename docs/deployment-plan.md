# Deployment Plan

## Project: BusTrack – Real-Time Commuter Bus Information System

---

## 1. Deployment Strategy

**Strategy:** Rolling Deployment with a Staging Environment

We deploy to a **staging environment** first, verify everything works, then promote to **production**. This prevents untested code from reaching real users.

| Environment | URL | Platform | Purpose |
|-------------|-----|----------|---------|
| Development | `localhost:5173` | Local machine | Active development |
| Staging | `bustrack-staging.vercel.app` | Vercel | Pre-production testing |
| Production | `bustrack.vercel.app` | Vercel + Render | Live system for users |

**Frontend:** Deployed to Vercel (automatic deploys from `main` branch)  
**Backend API:** Deployed to Render (web service running Node.js/Django)  
**Database:** PostgreSQL hosted on Render (managed database)

---

## 2. Pre-Deployment Checklist
- [ ] All tests pass (`npm test` / `pytest`)
- [ ] `.env` variables are set in the deployment platform (not hardcoded)
- [ ] Database migrations are applied (`python manage.py migrate` or equivalent)
- [ ] PR has been reviewed and merged to `main`
- [ ] Release tag has been created (e.g., `v0.5`)

---

## 3. Deployment Steps

### Frontend (Vercel)
1. Push or merge changes to the `main` branch
2. Vercel automatically triggers a new build
3. Wait for build to complete (~2–3 minutes)
4. Visit the production URL and verify the app loads

### Backend (Render)
1. Push changes to `main` branch (Render auto-deploys from GitHub)
2. Check Render dashboard for build logs
3. Verify health check endpoint: `GET /api/health` returns `{ status: "ok" }`
4. Run a quick smoke test on key endpoints

---

## 4. Rollback Steps

If a deployment breaks production:

1. **Immediate:** In Vercel/Render dashboard → go to **Deployments** → click the last working deployment → click **Redeploy**
2. **Via Git:** `git revert HEAD` → push to `main` → triggers automatic re-deploy
3. **Database:** If a bad migration was applied, run: `python manage.py migrate <app> <previous_migration_name>`
4. **Notify the team** in Discord immediately with details of what broke

**Target Recovery Time:** Under 15 minutes for a rollback

---

## 5. Environment Variables Required

```
DATABASE_URL=postgresql://user:password@host:5432/bustrack
GOOGLE_MAPS_API_KEY=your_key_here
FCM_SERVER_KEY=your_fcm_key_here
JWT_SECRET=your_jwt_secret
NODE_ENV=production
```

All variables must be set in the Vercel/Render environment settings — **never committed to the repository.**
