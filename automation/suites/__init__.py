"""Five Modular Test Domains Suite Package."""
from automation.suites.mobile_frontend_suite import MobileFrontendSuite
from automation.suites.web_frontend_suite import WebFrontendSuite
from automation.suites.backend_api_suite import BackendApiSuite
from automation.suites.security_assessment_suite import SecurityAssessmentSuite
from automation.suites.load_performance_suite import LoadPerformanceSuite

__all__ = [
    "MobileFrontendSuite",
    "WebFrontendSuite",
    "BackendApiSuite",
    "SecurityAssessmentSuite",
    "LoadPerformanceSuite"
]
