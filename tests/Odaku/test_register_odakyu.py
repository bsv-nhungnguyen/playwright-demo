EXPECTED_URL_PATH = "/account-management"

# ---------------------------------------------------------------------------
# TC-01  画面タイトル
# ---------------------------------------------------------------------------


def test_register_01_modal_title(register_page):
    """
    新規アカウント追加-1
    Verify that the modal title '新規アカウント追加' is displayed.
    """
    title_text = register_page.modal_title.text_content()
    assert "新規アカウント追加" in title_text, (
        f"Expected modal title to contain '新規アカウント追加', got: '{title_text}'"
    )


# ---------------------------------------------------------------------------
# TC-02  URL
# ---------------------------------------------------------------------------

def test_register_02_url(register_page):
    """
    新規アカウント追加-2
    Verify that the page URL contains '/account-management'.
    """
    current_url = register_page.get_current_url()
    assert EXPECTED_URL_PATH in current_url, (
        f"Expected URL to contain '{EXPECTED_URL_PATH}', got: '{current_url}'"
    )


# ---------------------------------------------------------------------------
# TC-03  アカウント名ラベル表示
# ---------------------------------------------------------------------------

def test_register_03_account_name_label_visible(register_page):
    """
    新規アカウント追加-3
    Verify that the label 'アカウント名 *（255文字以内）' is displayed.
    """
    label = register_page.account_name_label
    assert label.is_visible(), "Label 'アカウント名' should be visible"

    label_text = label.text_content()
    assert "アカウント名" in label_text, (
        f"Expected label to contain 'アカウント名', got: '{label_text}'"
    )
    assert "255文字以内" in label_text, (
        f"Expected label to contain '255文字以内', got: '{label_text}'"
    )
    # Required mark '*' should be present
    required_mark = label.locator(".required-mark")
    assert required_mark.is_visible(), "Required mark '*' should be visible on the label"


# ---------------------------------------------------------------------------
# TC-04  アカウント名 — 入力可能
# ---------------------------------------------------------------------------

def test_register_04_account_name_input(register_page):
    """
    新規アカウント追加-4
    Verify that text can be typed into the アカウント名 field and is displayed.
    """
    test_value = "テストアカウント"
    register_page.fill_account_name(test_value)
    assert register_page.get_account_name_value() == test_value, (
        f"Expected account name input to show '{test_value}'"
    )


# ---------------------------------------------------------------------------
# TC-05  メールアドレスラベル表示
# ---------------------------------------------------------------------------

def test_register_05_email_label_visible(register_page):
    """
    新規アカウント追加-5
    Verify that the label 'メールアドレス' is displayed.
    """
    label = register_page.email_label
    assert label.is_visible(), "Label 'メールアドレス' should be visible"

    label_text = label.text_content()
    assert "メールアドレス" in label_text, (
        f"Expected label to contain 'メールアドレス', got: '{label_text}'"
    )


# ---------------------------------------------------------------------------
# TC-06  メールアドレス — 入力可能
# ---------------------------------------------------------------------------

def test_register_06_email_input(register_page):
    """
    新規アカウント追加-6
    Verify that a valid email address can be entered and is displayed correctly.
    """
    test_email = "trucly@bravesoft-vn.com.vn"
    register_page.fill_email(test_email)
    assert register_page.get_email_value() == test_email, (
        f"Expected email input to show '{test_email}'"
    )


# ---------------------------------------------------------------------------
# TC-07  パスワードラベル表示
# ---------------------------------------------------------------------------

def test_register_07_password_label_visible(register_page):
    """
    新規アカウント追加-7
    Verify that the label 'パスワード（半角英数字 8文字以上32文字以内）' is displayed.
    """
    label = register_page.password_label
    assert label.is_visible(), "Label 'パスワード' should be visible"

    label_text = label.text_content()
    assert "パスワード" in label_text, (
        f"Expected label to contain 'パスワード', got: '{label_text}'"
    )
    assert "8文字以上" in label_text or "8文字以上32文字以内" in label_text, (
        f"Expected label to describe password constraints, got: '{label_text}'"
    )


# ---------------------------------------------------------------------------
# TC-08  パスワード — placeholder表示
# ---------------------------------------------------------------------------

def test_register_08_password_placeholder(register_page):
    """
    新規アカウント追加-8
    Verify that the password field has the placeholder '**********'.
    """
    placeholder = register_page.get_password_placeholder()
    assert placeholder == "**********", (
        f"Expected password placeholder to be '**********', got: '{placeholder}'"
    )


# ---------------------------------------------------------------------------
# TC-09  パスワード — マスク入力
# ---------------------------------------------------------------------------

def test_register_09_password_masked_input(register_page):
    """
    新規アカウント追加-9
    Verify that text can be entered in the password field and that the field
    masks the input (input type = 'password').
    """
    register_page.fill_password("Abcd1234")

    # The field should mask the input (type="password")
    input_type = register_page.get_password_input_type()
    assert input_type == "password", (
        f"Expected password input type to be 'password' (masked), got: '{input_type}'"
    )


# ---------------------------------------------------------------------------
# TC-10  権限セレクトボックス 初期表示
# ---------------------------------------------------------------------------

def test_register_10_role_selectbox_visible(register_page):
    """
    新規アカウント追加-10
    Verify that the 権限 combobox is visible, has a dropdown caret icon,
    and its initial value is blank (empty).
    """
    role_label = register_page.role_label
    assert role_label.is_visible(), "Label '権限' should be visible"

    combobox = register_page.role_combobox
    assert combobox.is_visible(), "Role combobox should be visible"

    # Caret (dropdown arrow) should be present
    caret = combobox.locator(".multiselect-caret")
    assert caret.is_visible(), "Dropdown caret icon should be visible in the role combobox"

    # Initial selected value should be empty
    single_label = register_page.modal.locator(
        ".label-input", has_text="権限"
    ).locator(".multiselect-single-label")
    assert not single_label.is_visible(), (
        "Role combobox should show no selected value on initial display"
    )


# ---------------------------------------------------------------------------
# TC-11  権限 — マスター管理者を選択
# ---------------------------------------------------------------------------

def test_register_11_select_role_master(register_page):
    """
    新規アカウント追加-11
    Verify that 'マスター管理者' can be selected and is displayed in the combobox.
    """
    register_page.select_role("マスター管理者")
    selected_text = register_page.get_selected_role_text()
    assert "マスター管理者" in selected_text, (
        f"Expected selected role to be 'マスター管理者', got: '{selected_text}'"
    )


# ---------------------------------------------------------------------------
# TC-12  権限 — テナント管理者を選択
# ---------------------------------------------------------------------------

def test_register_12_select_role_tenant(register_page):
    """
    新規アカウント追加-12
    Verify that 'テナント管理者' can be selected and is displayed in the combobox.
    """
    register_page.select_role("テナント管理者")
    selected_text = register_page.get_selected_role_text()
    assert "テナント管理者" in selected_text, (
        f"Expected selected role to be 'テナント管理者', got: '{selected_text}'"
    )


# ---------------------------------------------------------------------------
# TC-13  権限 — 複数選択不可
# ---------------------------------------------------------------------------

def test_register_13_role_single_selection_only(register_page):
    """
    新規アカウント追加-13
    Verify that only one role can be selected at a time (single-select combobox).
    After selecting 'マスター管理者' then 'テナント管理者', only 'テナント管理者'
    should be shown.
    """
    # Select the first role
    register_page.select_role("マスター管理者")

    # Now select the second role — re-open dropdown then click テナント管理者
    register_page.select_role("テナント管理者")

    selected_text = register_page.get_selected_role_text()

    assert "テナント管理者" in selected_text, (
        f"Expected only 'テナント管理者' to be selected, got: '{selected_text}'"
    )
    assert "マスター管理者" not in selected_text, (
        "Both roles should not be selectable simultaneously. "
        f"Found 'マスター管理者' in selected text: '{selected_text}'"
    )

    # Confirm the combobox is NOT multi-selectable
    combobox = register_page.role_combobox
    aria_multiselectable = combobox.get_attribute("aria-multiselectable")
    assert aria_multiselectable == "false", (
        f"Role combobox should have aria-multiselectable='false', got: '{aria_multiselectable}'"
    )


# ---------------------------------------------------------------------------
# TC-14  チケット組成時のポイント付与パラメータの変更権限 — ラベル表示
# ---------------------------------------------------------------------------

def test_register_14_ticket_permission_label_visible(register_page):
    """
    新規アカウント追加-14
    Verify that the label 'チケット組成時のポイント付与パラメータの変更権限' is displayed
    along with '有' and '無' radio options.
    The section only appears after selecting 'テナント管理者' role.
    """
    register_page.select_role("テナント管理者")

    assert register_page.ticket_permission_label.is_visible(), (
        "Label 'チケット組成時のポイント付与パラメータの変更権限' should be visible"
    )
    assert register_page.ticket_permission_radio_yes.is_visible(), "Option '有' should be visible"
    assert register_page.ticket_permission_radio_no.is_visible(), "Option '無' should be visible"


# ---------------------------------------------------------------------------
# TC-15  チケット権限 — 「有」を選択
# ---------------------------------------------------------------------------

def test_register_15_ticket_permission_select_yes(register_page):
    """
    新規アカウント追加-15
    Verify that the '有' option for チケット組成時のポイント付与パラメータの変更権限
    can be selected.
    """
    register_page.select_role("テナント管理者")
    register_page.select_ticket_permission("有")

    assert register_page.ticket_permission_radio_yes.is_checked(), (
        "Radio option '有' should be checked after selection"
    )


# ---------------------------------------------------------------------------
# TC-16  チケット権限 — 「無」を選択
# ---------------------------------------------------------------------------

def test_register_16_ticket_permission_select_no(register_page):
    """
    新規アカウント追加-16
    Verify that the '無' option for チケット組成時のポイント付与パラメータの変更権限
    can be selected.
    """
    register_page.select_role("テナント管理者")
    register_page.select_ticket_permission("無")

    assert register_page.ticket_permission_radio_no.is_checked(), (
        "Radio option '無' should be checked after selection"
    )


# ---------------------------------------------------------------------------
# TC-17  チケット権限 — 「有」と「無」は同時選択不可
# ---------------------------------------------------------------------------

def test_register_17_ticket_permission_single_selection_only(register_page):
    """
    新規アカウント追加-17
    Verify that '有' and '無' cannot both be selected simultaneously
    (they behave as radio buttons — only one can be active at a time).
    """
    register_page.select_role("テナント管理者")

    # Select '有' first
    register_page.select_ticket_permission("有")
    assert register_page.ticket_permission_radio_yes.is_checked(), "Option '有' should be checked"
    assert not register_page.ticket_permission_radio_no.is_checked(), (
        "Option '無' should NOT be checked when '有' is selected"
    )

    # Now select '無' — '有' must be deselected automatically
    register_page.select_ticket_permission("無")
    assert register_page.ticket_permission_radio_no.is_checked(), "Option '無' should be checked"
    assert not register_page.ticket_permission_radio_yes.is_checked(), (
        "Option '有' should NOT be checked when '無' is selected"
    )
