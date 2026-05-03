import re
from playwright.sync_api import Page, expect


def test_example_001(page: Page) -> None:
    page.goto("https://playwright-demo.eventos.work/web/portal/529/event/3988/users/login")
    page.get_by_role("textbox", name="sample@example.com").click()
    page.get_by_role("textbox", name="sample@example.com").fill("nhungntt@gmail.com")
    page.get_by_role("textbox", name="半角英数記号8文字以上32文字まで").click()
    page.get_by_role("textbox", name="半角英数記号8文字以上32文字まで").fill("124325")
    expect(page.get_by_role("button", name="ログイン", exact=True)).to_be_visible()
    expect(page.get_by_role("alert")).to_contain_text("パスワードは8文字以上32文字以下で指定してください")
    expect(page.get_by_role("textbox", name="sample@example.com")).to_have_value("nhungntt@gmail.com");
