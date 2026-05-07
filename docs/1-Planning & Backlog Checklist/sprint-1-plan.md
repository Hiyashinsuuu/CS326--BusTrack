# Sprint 1 Plan

**Sprint Duration:** April 21 – May 2, 2026  
**Sprint Goal:** Deliver the core commuter-facing features: route search, schedule viewing, real-time bus location display, and push notifications.

---

## Selected Stories for Sprint 1

| ID | User Story | Priority | Story Points |
|----|------------|----------|--------------|
| US-01 | Real-time bus location on map | High | 8 |
| US-02 | Push notification when bus is 5 min away | High | 5 |
| US-03 | Search for bus routes by destination | High | 3 |
| US-04 | View full schedule of a bus route | High | 3 |
| US-07 | Admin can update bus schedules | High | 5 |
| US-12 | Automated API tests | High | 3 |

**Total Story Points: 27**

---

## Sprint Backlog Tasks

### US-01 – Real-Time Bus Location
- [ ] Integrate Google Maps SDK
- [ ] Create `/api/bus/location` endpoint
- [ ] Poll endpoint every 30 seconds on frontend
- [ ] Display animated bus marker on map

### US-02 – Push Notifications
- [ ] Set up Firebase Cloud Messaging (FCM)
- [ ] Trigger notification when ETA ≤ 5 min
- [ ] Add toggle in user settings

### US-03 – Route Search
- [ ] Build search bar component
- [ ] Connect to `/api/routes/search?q=` endpoint
- [ ] Display results with route number, stops, schedule

### US-04 – Schedule Viewer
- [ ] Create route detail page
- [ ] Fetch schedule data from `/api/routes/:id/schedule`
- [ ] Render stop list with times

### US-07 – Admin Schedule Management
- [ ] Build admin dashboard page
- [ ] CRUD operations for schedule entries
- [ ] Publish changes to live view

### US-12 – Automated Tests
- [ ] Set up Jest / Pytest environment
- [ ] Write tests for `/api/bus/location`, `/api/routes/search`
- [ ] Add test script to CI pipeline

---

## Definition of Done
- Feature is implemented and code is pushed to `dev` branch
- At least one test exists for each backend endpoint
- Feature is reviewed by one other team member via Pull Request
- No critical bugs remain open
