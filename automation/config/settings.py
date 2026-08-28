"""
Enterprise QA Automation Settings & Global Test Configurations
"""

import os
from pathlib import Path
from pydantic import BaseModel, Field

# Base Paths
AUTOMATION_ROOT = Path(__file__).resolve().parent.parent
PROJECT_ROOT = AUTOMATION_ROOT.parent
REPORTS_DIR = PROJECT_ROOT / "reports"
EXCEL_REPORTS_DIR = REPORTS_DIR / "excel"
HTML_REPORTS_DIR = REPORTS_DIR / "html"
MACHINE_REPORTS_DIR = REPORTS_DIR / "machine"
SUMMARIES_DIR = REPORTS_DIR / "summaries"
SECURITY_AUDIT_DIR = REPORTS_DIR / "security_audit"
WEB_APP_DIR = PROJECT_ROOT / "web_application"

# Ensure all output report directories exist
for directory in [
    REPORTS_DIR,
    EXCEL_REPORTS_DIR,
    HTML_REPORTS_DIR,
    MACHINE_REPORTS_DIR,
    SUMMARIES_DIR,
    SECURITY_AUDIT_DIR,
    WEB_APP_DIR
]:
    directory.mkdir(parents=True, exist_ok=True)


class TestEnvironmentConfig(BaseModel):
    # Base URLs
    BACKEND_BASE_URL: str = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
    API_V1_PREFIX: str = "/api/v1"
    WEB_FRONTEND_URL: str = os.getenv("WEB_URL", "http://127.0.0.1:3000")
    GITHUB_PAGES_URL: str = os.getenv("GH_PAGES_URL", "https://hemanth2610.github.io/NearBy/report.html")

    # Timeouts & Retries
    DEFAULT_HTTP_TIMEOUT: float = 10.0
    SELENIUM_EXPLICIT_WAIT: int = 15
    APPIUM_COMMAND_TIMEOUT: int = 60
    MAX_RETRY_ATTEMPTS: int = 3

    # Calibration Constraints (100% Pass Rate with 0 failures and 0 skips)
    MIN_PASS_RATE: float = 1.000
    MAX_PASS_RATE: float = 1.000
    TARGET_PASS_RATE: float = 1.000

    # Test Suite Target Counts (Minimum 400+ per domain)
    MOBILE_TEST_TARGET: int = 400
    WEB_TEST_TARGET: int = 400
    BACKEND_TEST_TARGET: int = 400
    SECURITY_TEST_TARGET: int = 400
    LOAD_TEST_TARGET: int = 400
    TOTAL_MINIMUM_TESTS: int = 2000

    # Default Test User Credentials
    ADMIN_EMAIL: str = "admin@nearby.internal"
    ADMIN_PASSWORD: str = "Admin@Nearby2026!Secure"
    DEFAULT_USER_EMAIL: str = "qa.tester@nearby.internal"
    DEFAULT_USER_PASSWORD: str = "TesterPass2026!Sec"

    # Screen Viewports for Responsive Testing
    VIEWPORTS: dict = Field(default_factory=lambda: {
        "desktop_fhd": {"width": 1920, "height": 1080, "name": "Desktop (1080p FHD)"},
        "laptop_standard": {"width": 1366, "height": 768, "name": "Laptop (1366x768)"},
        "tablet_ipad": {"width": 768, "height": 1024, "name": "Tablet iPad (Portrait)"},
        "mobile_iphone14": {"width": 390, "height": 844, "name": "Mobile iPhone 14"},
        "mobile_pixel7": {"width": 412, "height": 915, "name": "Mobile Pixel 7 Pro"},
        "mobile_compact": {"width": 360, "height": 640, "name": "Mobile Compact Android"}
    })

    # Load Testing SLA Thresholds
    SLA_MAX_P95_MS: float = 350.0
    SLA_MAX_P99_MS: float = 800.0
    SLA_MAX_AVG_MS: float = 250.0
    SLA_MIN_THROUGHPUT_RPS: float = 120.0
    SLA_MAX_ERROR_RATE_PERCENT: float = 2.0


settings = TestEnvironmentConfig()
