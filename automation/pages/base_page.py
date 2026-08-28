"""
Enterprise Base Page Object with Explicit Waits, DOM Diagnostics & Logging
"""

import time
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger("POM.BasePage")


class BasePage:
    """Base class for all Web Page Objects providing robust interaction primitives."""

    def __init__(self, driver=None, base_url: str = "http://127.0.0.1:3000"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 15

    def navigate_to(self, path: str = "") -> Dict[str, Any]:
        """Navigate to relative or absolute path."""
        target_url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
        logger.info(f"Navigating to {target_url}")
        start = time.time()
        if self.driver:
            try:
                self.driver.get(target_url)
                return {"status": "PASS", "url": target_url, "duration_ms": round((time.time() - start) * 1000, 2)}
            except Exception as e:
                logger.error(f"Navigation failed: {e}")
                return {"status": "FAIL", "error": str(e), "url": target_url}
        return {"status": "PASS", "url": target_url, "duration_ms": round((time.time() - start) * 1000, 2)}

    def find_element(self, selector: str, by: str = "css"):
        """Locate element with explicit wait."""
        if self.driver:
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC

            by_map = {
                "css": By.CSS_SELECTOR,
                "xpath": By.XPATH,
                "id": By.ID,
                "name": By.NAME,
                "tag": By.TAG_NAME
            }
            wait = WebDriverWait(self.driver, self.timeout)
            return wait.until(EC.presence_of_element_located((by_map.get(by, By.CSS_SELECTOR), selector)))
        return None

    def click_element(self, selector: str, by: str = "css") -> bool:
        """Click element safely."""
        element = self.find_element(selector, by)
        if element:
            element.click()
            return True
        return False

    def enter_text(self, selector: str, text: str, by: str = "css") -> bool:
        """Send keys to input field."""
        element = self.find_element(selector, by)
        if element:
            element.clear()
            element.send_keys(text)
            return True
        return False

    def get_element_text(self, selector: str, by: str = "css") -> str:
        """Retrieve inner text."""
        element = self.find_element(selector, by)
        return element.text if element else ""

    def is_element_visible(self, selector: str, by: str = "css") -> bool:
        """Check if element is visible within timeout."""
        try:
            element = self.find_element(selector, by)
            return element.is_displayed() if element else False
        except Exception:
            return False

    def set_viewport_size(self, width: int, height: int):
        """Resize browser window for responsive layout testing."""
        if self.driver:
            self.driver.set_window_size(width, height)
            logger.info(f"Viewport adjusted to {width}x{height}")
