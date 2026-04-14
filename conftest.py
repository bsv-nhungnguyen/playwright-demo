from pages.base_page import BasePage
from pages.login_page import LoginPage
import pytest

URL = "https://playwright-demo.eventos.work/web/portal/529/event/3988/users/login"


@pytest.fixture
def access_to_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate(URL)
    return login_page