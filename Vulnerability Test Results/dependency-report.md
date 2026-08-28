# 📦 Dependency & Third-Party Package Vulnerability Report

**Audited Manifests**: `backend/requirements.txt`, `web/package.json`  
**Audit Scanners**: `pip-audit`, `safety`, `npm audit`  

---

## 1. Python Backend Dependencies Audit Matrix

| Package Name | Installed Version | Advisory ID | Severity | Remediation Upgrade Target |
| :--- | :---: | :--- | :---: | :--- |
| `python-jose` | `3.3.0` | CVE-2024-33663 | Low | Migrate to `PyJWT >= 2.8.0` |
| `cryptography` | `41.0.3` | CVE-2023-49083 | Med | Upgrade to `cryptography >= 42.0.5` |
| `urllib3` | `2.0.7` | CVE-2023-45803 | Low | Upgrade to `urllib3 >= 2.2.1` |
| `aiohttp` | `3.8.6` | CVE-2023-49081 | Med | Upgrade to `aiohttp >= 3.9.3` |
| `pillow` | `10.0.1` | CVE-2023-50447 | High | Upgrade to `pillow >= 10.3.0` |

---

## 2. Web Frontend NPM Dependencies Audit Matrix

| Package Name | Installed Version | Severity | Recommendation |
| :--- | :---: | :---: | :--- |
| `react` | `19.0.0` | Clean | Production Ready |
| `vite` | `6.0.7` | Clean | Production Ready |
| `tailwindcss` | `4.0.0` | Clean | Production Ready |
| `leaflet` | `1.9.4` | Clean | Production Ready |
