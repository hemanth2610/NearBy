# 🔒 Comprehensive Application Security Assessment & SAST Audit Report

**Target**: Nearby Enterprise Backend & Ecosystem  
**Audit Standard**: OWASP Top 10 API Security (2023) / CWE / NIST SP 800-115  
**Overall Security Score**: **64 / 100 (Grade: C+)**  

---

## 1. Executive Summary
The security assessment revealed **12 Total Findings** across the backend API, including 2 Critical vulnerabilities, 4 High vulnerabilities, 3 Medium vulnerabilities, and 3 Low findings.

---

## 2. Vulnerability Details & Threat Models

### [CRITICAL-01] Server-Side Request Forgery (SSRF) in Thumbnail Proxy
- **Endpoint**: `GET /api/v1/image-search/thumb?url={target_url}`
- **CVSS 3.1**: 10.0 (Critical) | **CWE**: CWE-918
- **Threat Vector**: Accepts unvalidated URLs and dispatches HTTP requests via `httpx.AsyncClient` without private IP or cloud metadata filtering.
- **Impact**: Full cloud metadata exfiltration (`169.254.169.254`) and internal port scanning (`127.0.0.1:6379`).

### [CRITICAL-02] Hardcoded Sensitive Credentials & Cryptographic Secrets
- **Location**: `app/core/config.py` & `app/main.py`
- **CVSS 3.1**: 9.1 (Critical) | **CWE**: CWE-798
- **Threat Vector**: Static default `SECRET_KEY`, default admin credentials, and hardcoded `MISTRAL_API_KEY` in source files.
- **Impact**: Token forgery, unauthorized admin privilege escalation, AI token quota depletion.

### [HIGH-01] Broken Object Level Authorization (IDOR) on Review Updates & Deletions
- **Endpoints**: `PATCH /api/v1/reviews/{id}`, `DELETE /api/v1/reviews/{id}`
- **CVSS 3.1**: 8.1 (High) | **CWE**: CWE-639
- **Threat Vector**: Omission of review author ownership verification (`review.user_id == current_user.id`).
- **Impact**: Arbitrary user review tampering and mass deletion.

### [HIGH-02] Insecure Direct Object Reference (IDOR) on Place Updates
- **Endpoint**: `PATCH /api/v1/places/{id}`
- **CVSS 3.1**: 6.5 (High) | **CWE**: CWE-285
- **Threat Vector**: Allows regular authenticated users to edit global tourist destination data.

### [HIGH-03] Unauthenticated File Upload & Stored XSS via SVG
- **Endpoint**: `POST /api/v1/uploads/image`
- **CVSS 3.1**: 7.5 (High) | **CWE**: CWE-434, CWE-79
- **Threat Vector**: Unauthenticated upload accepting `image/svg+xml` without script sanitization, served directly via static mount.

### [HIGH-04] Unauthenticated Database Flooding via Place Auto-Generation
- **Endpoint**: `GET /api/v1/places/{id}`
- **CVSS 3.1**: 7.5 (High) | **CWE**: CWE-400
- **Threat Vector**: Automatically creates new database records and calls external scrapers on non-existent place requests.
