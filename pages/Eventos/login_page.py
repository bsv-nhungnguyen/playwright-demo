from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input = page.get_by_role("textbox", name="sample@example.com")
        self.password_input = page.get_by_role("textbox", name="半角英数記号8文字以上32文字まで")
        self.login_button = page.get_by_role("button", name="ログイン", exact=True)
    
    def input_email(self, email):
        self.email_input.click()
        self.email_input.fill(email)
        print(f"Filled email input with: {email}")
    
    def input_password(self, password):
        self.password_input.click()
        self.password_input.fill(password)
        print(f"Filled password input with: {password}")

    def click_login(self):
        self.login_button.click()
        print("Clicked on login button")