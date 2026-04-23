# Release Notes

## Project: BusTrack – Real-Time Commuter Bus Information System

---

## v0.8.0 – Performance & Refactor Release
**Release Date:** April 23, 2026  
**Tag:** `v0.8`  
**Branch:** `main`

### What's New
- Refactored `getBusLocation()` to handle null/unavailable bus states gracefully
- Improved route search response time from ~800ms to ~210ms by adding a database index on `route_name`
- Cleaned up unused imports and dead code in `routes.py` and `MapView.jsx`

### Bug Fixes
- Fixed BUG-001: Bus location API no longer crashes when GPS data is unavailable
- Fixed incorrect fare calculation for routes under 2 km

### Technical Changes
- Added `CREATE INDEX idx_route_name ON routes(name)` migration
- Removed 3 deprecated helper functions from `utils.py`
- Split `MapView.jsx` (450 lines) into `MapView.jsx` + `BusMarker.jsx` for readability

---

## v0.5.0 – Sprint 1 Feature Release
**Release Date:** April 21, 2026  
**Tag:** `v0.5`  
**Branch:** `main`

### Features Delivered
- ✅ Real-time bus location displayed on interactive map (US-01)
- ✅ Push notifications when bus is 5 minutes away (US-02)
- ✅ Route search by destination (US-03)
- ✅ Full schedule viewer for each route (US-04)
- ✅ Admin dashboard for managing bus schedules (US-07)
- ✅ Automated unit tests for core API endpoints (US-12)

### Known Limitations
- Crowding data (US-11) not yet implemented — planned for Sprint 2
- Fare display (US-06) shows static values; dynamic calculation coming in Sprint 2
- Language toggle (US-10) is UI-only; backend localization not yet wired up

### Dependencies
- Node.js 20.x / Python 3.11
- PostgreSQL 15
- Firebase Cloud Messaging (for push notifications)
- Google Maps JavaScript API

---

## v0.1.0 – Initial Project Setup
**Release Date:** April 14, 2026  
**Tag:** `v0.1`

### Included
- Project repository initialized with `main` and `dev` branches
- Folder structure for frontend (React + Vite) and backend (Node.js / Django)
- README, `.gitignore`, and initial `docs/` folder
- GitHub Actions CI workflow scaffold
