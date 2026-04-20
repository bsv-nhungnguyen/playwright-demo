import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.login_page import LoginPage

def test_button_login_displayed(access_to_login_page):
    """Check if login button is displayed on the login page."""
    lg = access_to_login_page
    lg.input_email("nhungntt@gmail.com")
    lg.input_password("xxxx")
    lg.click_login()
    lg.expect_visible(lg.login_button), "Login button should be visible after clicking it."
