"""
Web Home & Landing Dashboard Page Object
"""

from automation.pages.base_page import BasePage


class HomePage(BasePage):
    """Encapsulates Web Home Page interactions."""

    HERO_SEARCH_INPUT = "input[placeholder*='Search destinations'], #hero-search"
    CATEGORY_PILLS = "[data-testid='category-pill'], .category-chip"
    FEATURED_PLACES_GRID = "[data-testid='featured-places'], .places-grid"
    MAP_CONTAINER = "#leaflet-map, .leaflet-container, [data-testid='interactive-map']"
    NAVBAR_USER_MENU = "[data-testid='user-menu'], button:has-text('Account')"
    THEME_TOGGLE_BTN = "[data-testid='theme-toggle'], button[aria-label='Toggle theme']"
    AI_TRIP_PLANNER_CTA = "a[href*='itinerary'], button:has-text('Plan Trip with AI')"

    def open(self):
        return self.navigate_to("/")

    def search_destination(self, query: str):
        self.enter_text(self.HERO_SEARCH_INPUT, query)

    def toggle_theme(self):
        self.click_element(self.THEME_TOGGLE_BTN)

    def select_category(self, category_name: str):
        self.click_element(f"button:has-text('{category_name}')")
