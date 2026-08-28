"""
Web Login & Authentication Page Object
"""

from automation.pages.base_page import BasePage


class LoginPage(BasePage):
    """Encapsulates Web Login Page interactions and DOM selectors."""

    # Selectors
    EMAIL_INPUT = "input[type='email'], input[name='email'], #email"
    PASSWORD_INPUT = "input[type='password'], input[name='password'], #password"
    SUBMIT_BUTTON = "button[type='submit'], button:has-text('Sign In'), button:has-text('Log In')"
    REMEMBER_ME_CHECKBOX = "input[type='checkbox']"
    FORGOT_PASSWORD_LINK = "a[href*='forgot-password'], button:has-text('Forgot Password')"
    ERROR_ALERT = "[role='alert'], .text-red-500, .error-message"
    REGISTER_LINK = "a[href*='register'], a[href*='signup']"

    def open(self):
        return self.navigate_to("/login")

    def login(self, email: str, password: str) -> dict:
        """Perform user login action."""
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.SUBMIT_BUTTON)
        return {"action": "login", "email": email, "status": "submitted"}

    def get_error_message(self) -> str:
        return self.get_element_text(self.ERROR_ALERT)

    def is_login_button_enabled(self) -> bool:
        element = self.find_element(self.SUBMIT_BUTTON)
        return element.is_enabled() if element else False
