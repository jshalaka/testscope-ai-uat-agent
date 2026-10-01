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

        self.heading: Locator = page.get_by_text(
            "TestScope AI",
            exact=False,
        ).first

        self.requirement_id_input: Locator = page.get_by_role(
            "textbox",
            name="Requirement ID",
            exact=True,
        )
        self.title_input: Locator = page.get_by_role(
            "textbox",
            name="Title",
            exact=True,
        )
        self.user_story_input: Locator = page.get_by_role(
            "textbox",
            name="User story",
            exact=True,
        )

    def open(self) -> Response |None:
        """Navigate to the testscope AI application"""
        return self.page.goto(self.app_url)

    def fill_requirement_details(
        self,
        requirement_id: str,
        title: str,
        user_story: str,
    ) -> None:
        """Enter the core business-requirement details."""
        self.requirement_id_input.fill(requirement_id)
        self.title_input.fill(title)
        self.user_story_input.fill(user_story)