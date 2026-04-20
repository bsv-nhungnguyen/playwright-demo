from playwright.sync_api import Locator, expect


class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, selector):
        self.page.click(selector)

    def fill(self, selector, text):
        self.page.fill(selector, text)
    
    #########GENERIC LOCATORS ACTIONS#########
    def click_by_role(self, role, name=None, exact=False):
        self.page.get_by_role(role, name=name, exact=exact).click()
        print(f"Clicked on element with role: {role}, name: {name}, exact: {exact}")
    
    def fill_by_placeholder(self, placeholder, text):
        self.page.get_by_placeholder(placeholder).fill(text)
        print(f"Filled element with placeholder: {placeholder} with text: {text}")


    # def get_input_value(self, selector):
    #     return self.page.input_value(selector)

    # def is_text_visible(self, text):
    #     return self.page.is_visible(f"text={text}")
    
    # def get_current_url(self):
    #     return self.page.url

    #########ASSERTIONS#########
    def expect_visible(self, selector):
        expect(selector).to_be_visible()
        print(f"Element with selector: {selector} is visible.")
    
    def expect_not_visible(self, selector):
        expect(selector).not_to_be_visible()
        print(f"Element with selector: {selector} is not visible.")
    
    def expect_text(self, selector, expected_text):
        expect(selector).to_have_text(expected_text)
        print(f"Element with selector: {selector} has text: {expected_text}")