# Security Checklist

## Project: BusTrack – Real-Time Commuter Bus Information System

---

## 1. Input Validation
- [x] Route search query is validated — stripped, length-checked, alphanumeric only
- [x] `bus_id` is validated — must be a positive integer before lookup
- [x] Invalid inputs raise `ValueError` with a clear message
- [ ] All future API endpoints must validate inputs before processing

## 2. Authentication & Authorization
- [x] Token-based authentication implemented in `bus_utils.py`
- [x] `authenticate()` function checks token against a set of valid tokens
- [x] Empty or non-string tokens are rejected immediately
- [ ] Future: replace static tokens with JWT (JSON Web Tokens)
- [ ] Future: add role-based access (admin vs. commuter)

## 3. Secrets Management
- [x] API keys and tokens are NOT hardcoded in source files
- [x] `.env` file is listed in `.gitignore`
- [x] GitHub Actions uses `secrets.GITHUB_TOKEN` (auto-provided, never exposed)
- [x] No sensitive values appear in commit history

## 4. Dependency Audit
- [x] `pip-audit` run on Python dependencies
- [x] Results reviewed and documented below
- [ ] Schedule monthly audits as part of maintenance

## 5. Logging & Monitoring
- [x] Errors raised with descriptive messages (not silent failures)
- [ ] Future: add structured logging (e.g., Python `logging` module)
- [ ] Future: set up alerts for repeated auth failures (brute-force detection)

## 6. Least Privilege
- [x] GitHub Actions deploy step uses minimum required permissions (`contents: write` only)
- [x] No admin credentials stored in the repo
- [ ] Future: separate service accounts for deploy vs. read-only operations

---

## Dependency Audit Results

Run command:
```bash
pip install pip-audit
pip-audit
```

| Package | Version | Vulnerability | Action |
|---------|---------|--------------|--------|
| pytest | 9.0.3 | None found | ✅ Safe |
| pip | 24.x | None found | ✅ Safe |

**Result: No known vulnerabilities found in current dependencies.**

---

## Security Risks Added to Risk Register

| # | Risk | Likelihood | Impact | Score | Mitigation |
|---|------|:-:|:-:|:-:|---|
| R-11 | SQL/code injection via unsanitized user input | 3 | 5 | 15 | Validate and sanitize all inputs; use parameterized queries |
| R-12 | Hardcoded API keys accidentally pushed to GitHub | 2 | 5 | 10 | Use `.env` + `.gitignore`; rotate keys immediately if exposed |
| R-13 | Unauthorized access to admin dashboard | 2 | 4 | 8 | Enforce token/session auth on all admin routes |
