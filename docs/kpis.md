# KPIs – Key Performance Indicators

## Project: BusTrack – Real-Time Commuter Bus Information System

---

## What are KPIs?
KPIs are measurable values that show how effectively the project and system are meeting objectives. We track both **development process KPIs** and **system performance KPIs**.

---

## 5 Defined KPIs

### KPI-01: Defect Rate
**Definition:** Number of bugs logged per sprint divided by total features delivered.
**Formula:** `Defect Rate = Total Bugs Logged / Total Features Delivered`
**Target:** ≤ 0.5 bugs per feature
**Why it matters:** A high defect rate means features are being shipped without enough testing.

---

### KPI-02: Lead Time
**Definition:** Average time from a feature being added to the backlog to it being merged to `main`.
**Formula:** `Lead Time = Date Merged − Date Added to Backlog`
**Target:** ≤ 5 days per feature
**Why it matters:** Long lead times indicate bottlenecks in development or review.

---

### KPI-03: Deployment Frequency
**Definition:** How often a successful deployment to production (GitHub Pages) occurs.
**Formula:** `Deployments per week`
**Target:** ≥ 2 deployments per week
**Why it matters:** Frequent deployments mean the team is delivering value continuously.

---

### KPI-04: API Response Time
**Definition:** Average time for the backend to respond to a request on the `/api/routes/search` endpoint.
**Formula:** Measured via `curl` timing or browser DevTools Network tab
**Target:** ≤ 300ms average
**Why it matters:** Slow responses frustrate users and reduce trust in the system.

---

### KPI-05: System Availability (Uptime)
**Definition:** Percentage of time the deployed system is accessible and returns HTTP 200.
**Formula:** `Uptime % = (Total Time − Downtime) / Total Time × 100`
**Target:** ≥ 99% uptime
**Why it matters:** Commuters depend on real-time info — downtime directly hurts users.
