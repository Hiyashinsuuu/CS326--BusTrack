# Metrics Report

## Project: BusTrack – Real-Time Commuter Bus Information System
**Reporting Period:** April 14 – May 7, 2026 (Sprint 1 & 2)

---

## KPI Dashboard

| KPI | Current Value | Target | Status | Interpretation | Action Plan |
|-----|:------------:|:------:|:------:|----------------|-------------|
| KPI-01: Defect Rate | 0.33 bugs/feature | ≤ 0.5 | ✅ Good | 1 bug logged (BUG-001) across 3 completed features — within acceptable range | Maintain current QA review process; add integration tests in Sprint 3 |
| KPI-02: Lead Time | 3.2 days avg | ≤ 5 days | ✅ Good | Features move from backlog to merged in 3.2 days on average — team is moving efficiently | Continue daily standups to catch blockers early |
| KPI-03: Deployment Frequency | 2.5 deploys/week | ≥ 2/week | ✅ Good | Team is deploying consistently — CI/CD pipeline is working as intended | Tag releases properly; maintain branch protection rules |
| KPI-04: API Response Time | 210ms avg | ≤ 300ms | ✅ Good | After adding DB index in v0.8, response time dropped from 810ms to 210ms | Monitor under load; add Redis cache if traffic increases |
| KPI-05: System Availability | 98.6% | ≥ 99% | ⚠️ Watch | One unplanned outage (~1 hr) when Render free tier spun down due to inactivity | Add uptime monitor (UptimeRobot); upgrade hosting if needed |

---

## Detailed Measurements

### KPI-01: Defect Rate
```
Sprint 1 features delivered: 3 (route search, map display, schedule viewer)
Bugs logged: 1 (BUG-001 — null GPS location crash)
Defect Rate = 1 / 3 = 0.33 bugs/feature ✅
```

### KPI-02: Lead Time (measured per feature)
```
feature/real-time-map:    Apr 14 → Apr 17 = 3 days
feature/route-search:     Apr 17 → Apr 20 = 3 days
feature/scm-config:       Apr 21 → Apr 25 = 4 days
feature/ci-pipeline:      Apr 25 → Apr 27 = 2 days
feature/security:         Apr 28 → May 1  = 3 days

Average Lead Time = (3 + 3 + 4 + 2 + 3) / 5 = 3.2 days ✅
```

### KPI-03: Deployment Frequency
```
Week 1 (Apr 14–18): 1 deploy
Week 2 (Apr 21–25): 3 deploys (v0.5-scm, bugfix, docs)
Week 3 (Apr 28–May 2): 3 deploys (v0.8-maintenance, security, ethics)
Week 4 (May 5–7): 2 deploys

Average = (1+3+3+2) / 4 weeks = 2.5 deploys/week ✅
```

### KPI-04: API Response Time
```
Measured using: curl -o /dev/null -s -w "%{time_total}" http://localhost:8000/api/routes/search?q=Divisoria

Before DB index (v0.5): ~810ms
After DB index (v0.8):  ~210ms

Current average: 210ms ✅
```

### KPI-05: System Availability
```
Total monitoring period: 504 hours (21 days)
Downtime recorded: 7 hours (Render free tier sleep + 1 manual deploy window)
Uptime = (504 - 7) / 504 × 100 = 98.6% ⚠️
```

---

## Basic Logging Added

Added to `bus_utils.py`:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("bustrack.log")
    ]
)
logger = logging.getLogger(__name__)

def search_routes(query):
    if not query or not isinstance(query, str):
        logger.warning("search_routes called with empty or invalid query")
        return []
    query = query.strip()
    if len(query) > MAX_QUERY_LENGTH:
        logger.error(f"Query too long: {len(query)} chars from input")
        raise ValueError(f"Query too long. Max {MAX_QUERY_LENGTH} characters.")
    results = [r for r in ROUTES if query.lower() in r["name"].lower()]
    logger.info(f"search_routes('{query}') returned {len(results)} result(s)")
    return results

def get_bus_location(bus_id):
    if not isinstance(bus_id, int) or bus_id <= 0:
        logger.error(f"Invalid bus_id received: {bus_id}")
        raise ValueError("bus_id must be a positive integer.")
    result = BUS_LOCATIONS.get(bus_id, {"status": "unavailable"})
    logger.info(f"get_bus_location({bus_id}) → {result}")
    return result
```

**Sample log output (`bustrack.log`):**
```
2026-05-07 10:32:01 [INFO] search_routes('Divisoria') returned 1 result(s)
2026-05-07 10:32:05 [WARNING] search_routes called with empty or invalid query
2026-05-07 10:32:09 [ERROR] Invalid bus_id received: -1
2026-05-07 10:33:00 [INFO] get_bus_location(2) → {'lat': 8.47, 'lng': 124.64}
```

---

## Suggested Improvements

| Area | Improvement | Priority |
|------|------------|---------|
| Availability | Upgrade from Render free tier to a paid plan or use Railway to prevent sleep | 🔴 High |
| Response Time | Add Redis caching for bus location — reduce DB hits on high-traffic endpoints | 🟡 Medium |
| Defect Rate | Add integration tests to catch API-level bugs before they reach production | 🟡 Medium |
| Logging | Ship logs to a centralized service (e.g., Logtail, Papertrail) for searchability | 🟢 Low |
| Monitoring | Set up UptimeRobot free tier to alert the team when the site goes down | 🔴 High |
