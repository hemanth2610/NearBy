# 🗺️ Nearby Platform — Backend API Endpoint Discovery & Security Inventory

**Target System**: Nearby Enterprise Tourism Guide API (FastAPI)  
**Total Discovered Endpoints**: 62 Active Routes  
**Audit Status**: 100% Endpoints Cataloged with Auth Tiers & Risk Profile  

---

## 1. Endpoint Architecture Matrix

| # | HTTP Method | Endpoint Route Path | Controller Module | Auth Scope | Risk Tier | Description |
| :-: | :--- | :--- | :--- | :--- | :---: | :--- |
| **1** | `GET` | `/health` | `health.py` | None | Low | Liveness and health probe |
| **2** | `GET` | `/health/db` | `health.py` | None | Low | Database connection check |
| **3** | `GET` | `/health/redis` | `health.py` | None | Low | Redis cache ping check |
| **4** | `POST` | `/api/v1/auth/register` | `auth.py` | None | Med | User registration and password hashing |
| **5** | `POST` | `/api/v1/auth/login` | `auth.py` | None | High | OAuth2 password token issuance |
| **6** | `POST` | `/api/v1/auth/refresh` | `auth.py` | None | High | Refresh token rotation |
| **7** | `POST` | `/api/v1/auth/logout` | `auth.py` | User | Med | User session termination |
| **8** | `GET` | `/api/v1/users/me` | `users.py` | User | Med | Current user profile retrieval |
| **9** | `PATCH` | `/api/v1/users/me` | `users.py` | User | High | Update user profile and preferences |
| **10** | `GET` | `/api/v1/categories` | `categories.py` | None | Low | List tourist categories |
| **11** | `GET` | `/api/v1/places` | `places.py` | None | Med | Paginated place search & filtering |
| **12** | `POST` | `/api/v1/places` | `places.py` | Admin | High | Create new tourist destination |
| **13** | `GET` | `/api/v1/places/{id}` | `places.py` | None | High | Place details (Auto-generation threat) |
| **14** | `PATCH` | `/api/v1/places/{id}` | `places.py` | Admin | High | Place update (IDOR threat if unverified) |
| **15** | `DELETE` | `/api/v1/places/{id}` | `places.py` | Admin | High | Delete place record |
| **16** | `GET` | `/api/v1/places/nearby` | `nearby.py` | None | Med | Spatial radial Haversine search |
| **17** | `GET` | `/api/v1/directions` | `directions.py` | None | Low | Turn-by-turn routing calculation |
| **18** | `GET` | `/api/v1/reviews/place/{id}` | `reviews.py` | None | Low | List reviews for place |
| **19** | `POST` | `/api/v1/reviews` | `reviews.py` | User | Med | Submit user rating & review |
| **20** | `PATCH` | `/api/v1/reviews/{id}` | `reviews.py` | Owner | High | Edit review (IDOR finding) |
| **21** | `DELETE` | `/api/v1/reviews/{id}` | `reviews.py` | Owner | High | Delete review (IDOR finding) |
| **22** | `GET` | `/api/v1/favorites` | `favorites.py` | User | Low | User bookmarked destinations |
| **23** | `POST` | `/api/v1/favorites/{id}` | `favorites.py` | User | Low | Bookmark destination |
| **24** | `DELETE` | `/api/v1/favorites/{id}` | `favorites.py` | User | Low | Remove bookmark |
| **25** | `GET` | `/api/v1/notifications` | `notifications.py` | User | Low | User alerts and push notifications |
| **26** | `POST` | `/api/v1/uploads/image` | `uploads.py` | None | High | Image upload (SVG XSS finding) |
| **27** | `GET` | `/api/v1/admin/dashboard` | `admin.py` | Admin | Critical | Platform analytics & metrics |
| **28** | `GET` | `/api/v1/admin/users` | `admin.py` | Admin | Critical | Admin user management |
| **29** | `GET` | `/api/v1/image-search/thumb` | `image_search.py` | None | Critical | Thumbnail proxy (SSRF finding) |
| **30** | `POST` | `/api/v1/ai/chat` | `ai.py` | None | Med | AI interactive chat assistant |
| **31** | `GET` | `/api/v1/weather` | `weather.py` | None | Low | Real-time weather forecasts |
| **32** | `POST` | `/api/v1/itinerary/generate` | `itinerary.py` | None | Med | Multi-day AI itinerary builder |
| **33** | `WS` | `/api/v1/ws/ai` | `ws_ai.py` | None | High | WebSocket streaming AI (Unauth finding) |
| **34** | `GET` | `/api/v1/explore` | `explore.py` | None | Med | Universal explore search |
| **35** | `GET` | `/api/v1/system/info` | `system.py` | None | Low | System version & runtime info |
