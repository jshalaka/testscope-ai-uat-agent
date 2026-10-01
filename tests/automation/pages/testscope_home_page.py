from playwright.sync_api import Locator, Page, Response

class TestScopeHomePage:
    """Page object representing the Testscope AI home page"""

    def __init__(self, page: Page, app_url: str) -> None:
        self.page = page
        self.app_url = app_url

        self.heading: Locator = page.get_by_text(
            "TestScope AI",
            exact=False,
        ).first

    def open(self) -> Response |None:
        """Navigate to the testscope AI application"""
        return self.page.goto(self.app_url)