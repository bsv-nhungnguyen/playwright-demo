import pytest
from pages.Odaku.register_page import RegisterPage

ADMIN_EMAIL = "kimtran@bravesoft.com.vn"
ADMIN_PASSWORD = "brave0404"
BASE_URL = "https://admin.odakyu.bravesoft.vn/account-management"
EXPECTED_URL_PATH = "/account-management"


@pytest.fixture()
def register_page(page):
    """
    Log in as admin, navigate to account management page,
    then open the 新規アカウント追加 modal.

    If the server returns an error modal (エラーが発生しました。もう一度お試しください。)
    at any step, the '戻る' button is clicked automatically and the flow continues.
    """
    rp = RegisterPage(page)

    # ── Step 1: Navigate (may redirect to login if not authenticated) ────────
    page.goto(BASE_URL)

    # ── Step 2: Fill login credentials ──────────────────────────────────────
    page.locator("input[name='email']").fill(ADMIN_EMAIL)
    page.locator("input[name='password']").fill(ADMIN_PASSWORD)
    page.get_by_role("button", name="ログイン").click()

    # Dismiss error modal if server is unstable after login attempt
    rp.dismiss_error_modal_if_present()

    # ── Step 3: Wait for account management page ─────────────────────────────
    page.wait_for_url(f"**{EXPECTED_URL_PATH}", timeout=15_000)

    # Dismiss error modal if it appears on page load
    rp.dismiss_error_modal_if_present()

    # ── Step 4: Open the 新規アカウント追加 modal ──────────────────────────────
    rp.open_register_modal()

    # Dismiss error modal if it appears when opening the register modal
    rp.dismiss_error_modal_if_present()

    return rp

