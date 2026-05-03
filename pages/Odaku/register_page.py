from pages.Odaku.base_page import BasePage


class RegisterPage(BasePage):
    """Page Object Model for the 新規アカウント追加 (New Account Registration) modal."""

    # ── URLs ────────────────────────────────────────────────────────────────
    URL = "https://admin.odakyu.bravesoft.vn/account-management"

    def __init__(self, page):
        super().__init__(page)

        # ── Modal container ─────────────────────────────────────────────────
        self.modal = page.locator(".modify-account-modal-content")

        # ── Modal title ─────────────────────────────────────────────────────
        self.modal_title = self.modal.locator(".title-confirm")

        # ── Account name field ──────────────────────────────────────────────
        # label text contains "アカウント名"
        self.account_name_label = self.modal.locator(".label-title", has_text="アカウント名")
        self.account_name_input = page.locator("input[name='userName']")

        # ── Email field ─────────────────────────────────────────────────────
        self.email_label = self.modal.locator(".label-title", has_text="メールアドレス")
        self.email_input = page.locator("input[name='email']")

        # ── Password field ──────────────────────────────────────────────────
        self.password_label = self.modal.locator(".label-title", has_text="パスワード")
        self.password_input = page.locator("input[name='password']")

        # ── 権限 (Role) select box ───────────────────────────────────────────
        self.role_label = self.modal.locator(".label-title", has_text="権限")
        self.role_combobox = self.modal.locator(
            ".label-input", has_text="権限"
        ).locator("[role='combobox']")
        self.role_option_master = page.get_by_role("option", name="マスター管理者")
        self.role_option_tenant = page.get_by_role("option", name="テナント管理者")

        # ── 新規追加 button (opens the modal) ────────────────────────────────
        self.add_new_button = page.get_by_role("button", name="新規追加")

        # ── Form action buttons ──────────────────────────────────────────────
        self.cancel_button = self.modal.get_by_role("button", name="キャンセル")
        self.save_button = self.modal.get_by_role("button", name="保存")

    # ── Navigation ──────────────────────────────────────────────────────────

    def go_to_account_management(self):
        """Navigate to the account management page."""
        self.navigate(self.URL)

    # ── Modal actions ────────────────────────────────────────────────────────

    def open_register_modal(self):
        """Click the 新規追加 button to open the registration modal."""
        self.add_new_button.click()
        self.modal.wait_for(state="visible")

    # ── Account name ─────────────────────────────────────────────────────────

    def fill_account_name(self, name: str):
        """Fill in the アカウント名 input field."""
        self.account_name_input.click()
        self.account_name_input.fill(name)

    def get_account_name_value(self) -> str:
        """Return the current value of the アカウント名 input."""
        return self.account_name_input.input_value()

    # ── Email ────────────────────────────────────────────────────────────────

    def fill_email(self, email: str):
        """Fill in the メールアドレス input field."""
        self.email_input.click()
        self.email_input.fill(email)

    def get_email_value(self) -> str:
        """Return the current value of the メールアドレス input."""
        return self.email_input.input_value()

    # ── Password ─────────────────────────────────────────────────────────────

    def fill_password(self, password: str):
        """Fill in the パスワード input field."""
        self.password_input.click()
        self.password_input.fill(password)

    def get_password_input_type(self) -> str:
        """Return the type attribute of the password input (password / text)."""
        return self.password_input.get_attribute("type")

    def get_password_placeholder(self) -> str:
        """Return the placeholder attribute of the password input."""
        return self.password_input.get_attribute("placeholder")

    # ── Role combobox ────────────────────────────────────────────────────────

    def open_role_dropdown(self):
        """Click the 権限 combobox to open its dropdown."""
        self.role_combobox.click()

    def select_role(self, role_name: str):
        """
        Select a role from the 権限 dropdown.
        role_name: 'マスター管理者' or 'テナント管理者'
        """
        self.open_role_dropdown()
        self.page.get_by_role("option", name=role_name).click()

    def get_selected_role_text(self) -> str:
        """Return the text of the currently selected role option."""
        return self.modal.locator(
            ".label-input", has_text="権限"
        ).locator(".multiselect-single-label").text_content()

    # ── チケット組成時のポイント付与パラメータの変更権限 (Ticket permission) ─────────
    # This section is only visible after selecting 'テナント管理者' role.
    # HTML: <label for="authority1"> 有 </label>  /  <label for="authority2"> 無 </label>

    @property
    def ticket_permission_label(self):
        """Locator for the ticket permission section label."""
        return self.modal.locator(
            ".label-title", has_text="チケット組成時のポイント付与パラメータの変更権限"
        )

    @property
    def ticket_permission_radio_yes(self):
        """Locator for the '有' radio button (id=authority1)."""
        return self.page.get_by_label("有")

    @property
    def ticket_permission_radio_no(self):
        """Locator for the '無' radio button (id=authority2)."""
        return self.page.get_by_label("無")

    def select_ticket_permission(self, value: str):
        """
        Select a ticket permission radio option.
        value: '有' or '無'
        """
        if value == "有":
            self.ticket_permission_radio_yes.check()
        elif value == "無":
            self.ticket_permission_radio_no.check()
        else:
            raise ValueError(f"Invalid ticket permission value: '{value}'. Use '有' or '無'.")
