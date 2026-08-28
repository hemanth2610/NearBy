"""
Web Explore, Place Details, Itinerary & Admin Dashboard Page Objects
"""

from automation.pages.base_page import BasePage


class ExplorePage(BasePage):
    SEARCH_BAR = "input[placeholder*='Explore'], input[type='search']"
    RADIUS_SLIDER = "input[type='range'], [data-testid='radius-slider']"
    RATING_FILTER = "[data-testid='rating-filter-4-plus']"
    SORT_DROPDOWN = "select[name='sort'], [data-testid='sort-select']"
    RESULTS_LIST = "[data-testid='place-card'], .destination-card"
    PAGINATION_NEXT = "button[aria-label='Next page'], button:has-text('Next')"

    def open(self):
        return self.navigate_to("/explore")


class PlaceDetailPage(BasePage):
    PLACE_TITLE = "h1, [data-testid='place-title']"
    RATING_BADGE = "[data-testid='rating-score'], .rating-badge"
    FAVORITE_TOGGLE_BTN = "[data-testid='btn-bookmark'], button[aria-label='Save to favorites']"
    DIRECTIONS_BTN = "a[href*='directions'], button:has-text('Get Directions')"
    REVIEWS_CONTAINER = "[data-testid='reviews-list']"
    ADD_REVIEW_BTN = "button:has-text('Write a Review')"
    STAR_RATING_INPUT = "[data-testid='star-rating-input']"
    REVIEW_TEXTAREA = "textarea[name='comment'], textarea#review-comment"
    SUBMIT_REVIEW_BTN = "button:has-text('Submit Review')"


class ItineraryPage(BasePage):
    DESTINATION_INPUT = "input[name='destination'], #destination-input"
    DAYS_SELECT = "select[name='duration_days'], #duration-select"
    INTEREST_CHECKBOXES = "input[name='interests']"
    BUDGET_TIER = "select[name='budget_level']"
    GENERATE_BTN = "button:has-text('Generate Smart Itinerary'), button[type='submit']"
    TIMELINE_CONTAINER = "[data-testid='itinerary-timeline'], .itinerary-day-card"
    EXPORT_PDF_BTN = "button:has-text('Download PDF'), button:has-text('Export')"

    def open(self):
        return self.navigate_to("/itinerary")


class AdminDashboardPage(BasePage):
    METRICS_CARDS = "[data-testid='metric-card']"
    USER_TABLE = "table[data-testid='admin-users-table']"
    PLACES_TABLE = "table[data-testid='admin-places-table']"
    SYSTEM_LOGS_VIEW = "[data-testid='system-logs']"
    SYNC_EXTERNAL_BTN = "button:has-text('Trigger Wikipedia Sync')"

    def open(self):
        return self.navigate_to("/admin")
