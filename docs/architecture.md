# System Architecture

## Project: BusTrack – Real-Time Commuter Bus Information System

---

## Architecture Diagram (ASCII)

```
┌─────────────────────────────────────────────────────────┐
│                        CLIENTS                          │
│                                                         │
│   [Commuter Browser]        [Admin Browser]             │
│   React + Vite + TS         React Admin Dashboard       │
└────────────┬───────────────────────┬────────────────────┘
             │  HTTPS                │  HTTPS
             ▼                       ▼
┌─────────────────────────────────────────────────────────┐
│                     FRONTEND LAYER                       │
│              GitHub Pages / Vercel                       │
│                                                         │
│   Pages: Home, Map, Route Search, Schedule, Report      │
└────────────────────────┬────────────────────────────────┘
                         │  REST API calls (HTTPS)
                         ▼
┌─────────────────────────────────────────────────────────┐
│                     BACKEND LAYER                        │
│                  Render (Node/Django)                    │
│                                                         │
│   /api/bus/location/:id   → get real-time GPS           │
│   /api/routes/search      → search routes               │
│   /api/routes/:id/schedule→ get schedule                │
│   /api/reports            → submit delay report         │
│   /api/health             → smoke test endpoint         │
│                                                         │
│   bus_utils.py — core logic + input validation + auth   │
└───────────┬─────────────────────────┬───────────────────┘
            │  SQL queries            │  Push notifications
            ▼                         ▼
┌───────────────────┐      ┌──────────────────────────────┐
│    DATABASE       │      │   EXTERNAL SERVICES          │
│  PostgreSQL       │      │                              │
│  (Render managed) │      │  Google Maps API (map tiles) │
│                   │      │  Firebase FCM (notifications)│
│  Tables:          │      └──────────────────────────────┘
│  - routes         │
│  - schedules      │
│  - bus_locations  │
│  - reports        │
└───────────────────┘
```

---

## Component Descriptions

| Component | Technology | Responsibility |
|-----------|-----------|----------------|
| Frontend | React + Vite + TypeScript | UI rendering, map display, user interaction |
| Backend API | Python / Node.js | Business logic, input validation, auth, data serving |
| Database | PostgreSQL | Persistent storage for routes, schedules, reports |
| CI/CD | GitHub Actions | Automated testing, deployment, smoke testing |
| Hosting | GitHub Pages + Render | Static frontend + dynamic backend |
| Notifications | Firebase FCM | Push alerts when bus is 5 min away |
| Maps | Google Maps JS API | Interactive real-time bus map |

---

## Data Flow Example — Commuter searches for a route

```
1. User types "Divisoria" in search bar (Frontend)
2. Frontend sends GET /api/routes/search?q=Divisoria (HTTPS)
3. Backend validates input (bus_utils.search_routes)
4. Backend queries PostgreSQL: SELECT * FROM routes WHERE name ILIKE '%Divisoria%'
5. Results returned as JSON to frontend
6. Frontend renders route cards with name, stops, schedule
```

---

## Concurrency in BusTrack

BusTrack handles concurrent operations naturally:
- Multiple commuters polling `/api/bus/location` simultaneously
- Real-time location updates pushed to all connected clients at once
- Admin schedule updates propagate to all users within 1 minute
- Firebase FCM delivers notifications to thousands of devices in parallel
