# 🛠️ Developer Remediation Playbook & Code Fixes

This guide provides concrete, copy-paste code patches to remediate all identified vulnerabilities.

---

## 1. [P0 Fix] Server-Side Request Forgery (SSRF) in Thumbnail Proxy

**Target File**: `app/api/v1/endpoints/image_search.py`

```python
import ipaddress
import urllib.parse
from fastapi import HTTPException

ALLOWED_DOMAINS = {"upload.wikimedia.org", "images.unsplash.com", "bing.com", "microsoft.com"}

def validate_safe_url(target_url: str):
    parsed = urllib.parse.urlparse(target_url)
    if parsed.scheme not in ("http", "https"):
        raise HTTPException(status_code=400, detail="Invalid URL scheme")
    
    hostname = parsed.hostname
    if not hostname or hostname in ("localhost", "127.0.0.1", "169.254.169.254"):
        raise HTTPException(status_code=400, detail="Private host addresses not permitted")
        
    try:
        ip = ipaddress.ip_address(hostname)
        if ip.is_private or ip.is_loopback or ip.is_link_local:
            raise HTTPException(status_code=400, detail="Private IP addresses prohibited")
    except ValueError:
        pass  # Hostname is a domain name
```

---

## 2. [P0 Fix] Remove Hardcoded Secrets & Mistral Key

**Target File**: `app/core/config.py`

```python
class Settings(BaseSettings):
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    MISTRAL_API_KEY: str = Field(..., env="MISTRAL_API_KEY")
    FIRST_ADMIN_PASSWORD: str = Field(..., env="FIRST_ADMIN_PASSWORD")
    DEBUG: bool = False
```

---

## 3. [P1 Fix] Enforce Object Ownership (IDOR) on Review Edits/Deletions

**Target File**: `app/api/v1/endpoints/reviews.py`

```python
if review.user_id != current_user.id and current_user.role != "admin":
    raise HTTPException(status_code=403, detail="You do not have permission to modify this review")
```

---

## 4. [P1 Fix] Restrict Place Updates to Admins

**Target File**: `app/api/v1/endpoints/places.py`

```python
@router.patch("/{uuid}", response_model=PlaceResponse)
async def update_place(
    uuid: str,
    place_in: PlaceUpdate,
    db: AsyncSession = Depends(get_db),
    current_admin: User = Depends(get_current_admin)  # Replaced get_current_active_user
):
    ...
```

---

## 5. [P1 Fix] Disallow Unsanitized SVG Uploads

**Target File**: `app/api/v1/endpoints/uploads.py`

```python
ALLOWED_MIME_TYPES = {"image/jpeg", "image/png", "image/webp"}

if file.content_type not in ALLOWED_MIME_TYPES:
    raise HTTPException(status_code=400, detail="Unsupported image format. Allowed: JPEG, PNG, WebP.")
```
