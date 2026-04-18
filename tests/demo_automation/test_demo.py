from pages.login_page import LoginPage

def test_check_url_login(access_to_login_page):
    """Check if user can input text into username and password fields."""
    login_page = access_to_login_page
    expected_url = "https://playwright-demo.eventos.work/web/portal/529/event/3988/users/login"
    assert login_page.get_current_url() == expected_url
