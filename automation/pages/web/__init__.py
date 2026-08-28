"""Web Page Object Model components."""
from automation.pages.web.login_page import LoginPage
from automation.pages.web.home_page import HomePage
from automation.pages.web.explore_page import ExplorePage
from automation.pages.web.place_detail_page import PlaceDetailPage
from automation.pages.web.itinerary_page import ItineraryPage
from automation.pages.web.admin_dashboard_page import AdminDashboardPage

__all__ = [
    "LoginPage",
    "HomePage",
    "ExplorePage",
    "PlaceDetailPage",
    "ItineraryPage",
    "AdminDashboardPage"
]
