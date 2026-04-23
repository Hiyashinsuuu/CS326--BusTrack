# Product Backlog

## Project: BusTrack – Real-Time Commuter Bus Information System

---

| ID | User Story | Priority | Story Points | Acceptance Criteria |
|----|------------|----------|--------------|---------------------|
| US-01 | As a commuter, I want to see the real-time location of my bus so that I know exactly when it will arrive. | High | 8 | Bus location updates every 30 seconds on the map; marker is accurate within 50 meters. |
| US-02 | As a commuter, I want to receive push notifications when my bus is 5 minutes away so that I can head to the stop on time. | High | 5 | Notification fires when estimated arrival ≤ 5 min; user can toggle alerts on/off. |
| US-03 | As a commuter, I want to search for bus routes by destination so that I can find which bus to take. | High | 3 | Search returns matching routes in under 1 second; results show route number, stops, and schedule. |
| US-04 | As a commuter, I want to view the full schedule of a bus route so that I can plan my trips in advance. | High | 3 | Schedule shows all stops with estimated departure times; data loads within 2 seconds. |
| US-05 | As a commuter, I want to mark favorite bus routes so that I can quickly access the lines I use most. | Medium | 2 | Favorites are saved to user profile; appear at the top of the route list on next login. |
| US-06 | As a commuter, I want to see the estimated fare for a route so that I can prepare exact change. | Medium | 2 | Fare is displayed on the route detail page; updates if route distance changes. |
| US-07 | As an admin, I want to update bus schedules from a dashboard so that commuters always see accurate times. | High | 5 | Admin can edit, save, and publish schedules; changes reflect on commuter view within 1 minute. |
| US-08 | As an admin, I want to view a report of peak-hour ridership so that I can allocate more buses during busy times. | Medium | 5 | Report shows hourly passenger counts per route; exportable as CSV. |
| US-09 | As a commuter, I want to report a delayed or missing bus so that the system can be kept accurate. | Medium | 3 | Report form submits in under 3 seconds; admin receives alert; submitted report shows "Under Review" status. |
| US-10 | As a commuter, I want the app to work in Filipino and English so that all commuters can use it comfortably. | Low | 3 | Language toggle switches UI text instantly; preference is saved per user. |
| US-11 | As a commuter, I want to see how crowded a bus is so that I can decide whether to wait for the next one. | Medium | 5 | Crowding level (Low / Medium / Full) is shown on the bus marker; updated every minute. |
| US-12 | As a developer, I want automated tests on the API so that bugs are caught before deployment. | High | 3 | All critical endpoints have at least one unit test; CI pipeline runs tests on every push. |
