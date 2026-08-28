"""
Mobile Login Screen & Screen Objects
"""

from automation.pages.mobile.base_screen import BaseScreen


class LoginScreen(BaseScreen):
    EMAIL_INPUT = "com.tourismguide.app:id/et_email"
    PASSWORD_INPUT = "com.tourismguide.app:id/et_password"
    LOGIN_BTN = "com.tourismguide.app:id/btn_login"
    BIOMETRIC_AUTH_BTN = "com.tourismguide.app:id/btn_biometric_login"
    SIGNUP_LINK = "com.tourismguide.app:id/tv_signup"
    ERROR_SNACKBAR = "com.tourismguide.app:id/snackbar_text"

    def login_with_credentials(self, email: str, password: str):
        self.send_input(self.EMAIL_INPUT, email)
        self.send_input(self.PASSWORD_INPUT, password)
        self.tap(self.LOGIN_BTN)


class MainNavScreen(BaseScreen):
    BOTTOM_NAV_HOME = "com.tourismguide.app:id/nav_home"
    BOTTOM_NAV_EXPLORE = "com.tourismguide.app:id/nav_explore"
    BOTTOM_NAV_SAVED = "com.tourismguide.app:id/nav_favorites"
    BOTTOM_NAV_AI_ASSIST = "com.tourismguide.app:id/nav_ai_chat"
    BOTTOM_NAV_PROFILE = "com.tourismguide.app:id/nav_profile"


class BiometricScreen(BaseScreen):
    FINGERPRINT_ICON = "com.tourismguide.app:id/biometric_prompt_icon"
    BIOMETRIC_TITLE = "com.tourismguide.app:id/biometric_prompt_title"
    USE_PIN_FALLBACK = "com.tourismguide.app:id/btn_use_pin"
    CANCEL_AUTH_BTN = "com.tourismguide.app:id/btn_cancel_biometric"
