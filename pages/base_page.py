class BasePage:
    """Single base page class shared across the entire project."""

    def __init__(self, page):
        self.page = page

    def navigate(self, url: str):
        """Navigate to a given URL."""
        self.page.goto(url)

    def get_current_url(self) -> str:
        """Return the current page URL."""
        return self.page.url

    def get_input_value(self, locator) -> str:
        """Return the current value of an input element."""
        return locator.input_value()

    def get_text_content(self, locator) -> str:
        """Return visible text content of an element."""
        return locator.text_content()

    def is_visible(self, locator) -> bool:
        """Return True if the element is visible on the page."""
        return locator.is_visible()

    def is_disabled(self, locator) -> bool:
        """Return True if the element is disabled."""
        return locator.is_disabled()

    def is_checked(self, locator) -> bool:
        """Return True if a radio/checkbox element is checked."""
        return locator.is_checked()

    def get_attribute(self, locator, attribute: str):
        """Return the value of the given attribute of the element."""
        return locator.get_attribute(attribute)

    def dismiss_error_modal_if_present(self, timeout: int = 3_000) -> bool:
        """
        Dismiss the server error modal (エラーが発生しました。もう一度お試しください。)
        by clicking the '戻る' button if it is visible.

        Args:
            timeout: Max milliseconds to wait for the modal to appear (default 3s).

        Returns:
            True  — modal was detected and dismissed.
            False — modal was not present, nothing was done.
        """
        back_button = self.page.get_by_role("button", name="戻る")
        try:
            back_button.wait_for(state="visible", timeout=timeout)
            back_button.click()
            # Wait for the modal to disappear before continuing
            back_button.wait_for(state="hidden", timeout=5_000)
            return True
        except Exception:
            # Modal was not present — safe to continue
            return False

