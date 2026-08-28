"""
Mobile Android Appium Base Screen Object with UiAutomator2 Primitives
"""

import time
import logging
from typing import Dict, Any

logger = logging.getLogger("POM.BaseScreen")


class BaseScreen:
    """Base class for Android Native Application Screens."""

    PACKAGE_NAME = "com.tourismguide.app"

    def __init__(self, driver=None):
        self.driver = driver
        self.timeout = 20

    def find_screen_element(self, resource_id: str, locator_type: str = "id"):
        """Find Android native UI element by resource-id or accessibility id."""
        if self.driver:
            from appium.webdriver.common.appiumby import AppiumBy
            locators = {
                "id": AppiumBy.ID,
                "accessibility_id": AppiumBy.ACCESSIBILITY_ID,
                "xpath": AppiumBy.XPATH,
                "uiautomator": AppiumBy.ANDROID_UIAUTOMATOR
            }
            return self.driver.find_element(locators.get(locator_type, AppiumBy.ID), resource_id)
        return None

    def tap(self, resource_id: str, locator_type: str = "id") -> bool:
        element = self.find_screen_element(resource_id, locator_type)
        if element:
            element.click()
            return True
        return False

    def send_input(self, resource_id: str, text: str) -> bool:
        element = self.find_screen_element(resource_id)
        if element:
            element.clear()
            element.send_keys(text)
            return True
        return False

    def swipe_up(self):
        """Simulate vertical scroll gesture."""
        if self.driver:
            window_size = self.driver.get_window_size()
            width = window_size["width"]
            height = window_size["height"]
            self.driver.swipe(width // 2, int(height * 0.8), width // 2, int(height * 0.2), 400)

    def set_network_offline(self):
        """Toggle airplane mode / network state."""
        if self.driver:
            logger.info("Simulating device network offline state")
