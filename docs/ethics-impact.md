# Ethics & Impact Assessment

## Project: BusTrack – Real-Time Commuter Bus Information System

---

## 1. Stakeholders

| Stakeholder | Role | How They Are Affected |
|-------------|------|-----------------------|
| Commuters | Primary users | Benefit from accurate real-time bus info; risk: location data privacy |
| Bus drivers | Indirect users | Routes and schedules are made public; risk: constant location tracking |
| Bus operators / LTFRB | Data providers | Must supply accurate data; benefit: reduced passenger complaints |
| Local government | Regulatory body | Benefits from improved public transport transparency |
| Development team | Builders | Responsible for accuracy, security, and ethical use of data |
| Vulnerable groups | Low-income commuters, elderly, PWDs | May benefit most from reliable transit info; risk: digital divide |

---

## 2. Potential Harms & Mitigations

| Harm | Who Is Affected | Likelihood | Mitigation |
|------|----------------|:-:|---|
| Inaccurate bus location data causes missed rides | Commuters | Medium | Display "last updated" timestamp; show data confidence level |
| Driver location tracking without consent | Bus drivers | Medium | Inform drivers of tracking; obtain consent; limit data retention |
| App inaccessible to users without smartphones | Low-income / elderly commuters | High | Provide SMS fallback or offline schedule access |
| Data breach exposing commuter travel patterns | All users | Low | Encrypt data in transit and at rest; minimize data collected |
| Algorithmic bias in route prioritization | Minority route users | Low | Ensure all routes are treated equally in the system |

---

## 3. Ethical Principles Applied

- **Transparency:** Users are informed about what data is collected and why
- **Fairness:** All routes served equally regardless of ridership volume
- **Accountability:** Development team maintains a defect log and responds to issues
- **Privacy by Design:** Only collect data necessary for the feature to work
- **Accessibility:** System designed to work on low-end devices and slow connections
