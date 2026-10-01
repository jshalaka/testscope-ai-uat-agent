from playwright.sync_api import Locator, Page, Response

class TestScopeHomePage:
    """Page object representing the Testscope AI home page"""

    def __init__(self, page: Page, app_url: str) -> None:
        self.page = page
        self.app_url = app_url

        self.domain_input: Locator = page.get_by_role(
            "textbox",
            name="Domain",
            exact=True,
        )
        self.feature_input: Locator = page.get_by_role(
            "textbox",
            name="Feature",
            exact=True,
        )
        self.acceptance_criteria_input: Locator = page.get_by_role(
            "textbox",
            name="Acceptance criteria",
            exact=True,
        )
        self.business_context_input: Locator = page.get_by_role(
            "textbox",
            name="Business context",
            exact=True,
        )
        self.known_risks_input: Locator = page.get_by_role(
            "textbox",
            name="Known risks",
            exact=True,
        )
        self.generate_button: Locator = page.get_by_test_id(
            "stBaseButton-secondaryFormSubmit"
        )

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

    def fill_requirement_context(
        self,
        domain: str,
        feature: str,
        acceptance_criteria: str,
        business_context: str,
        known_risks: str,
    ) -> None:
        """Enter the remaining requirement and risk information."""
        self.domain_input.fill(domain)
        self.feature_input.fill(feature)
        self.acceptance_criteria_input.fill(acceptance_criteria)
        self.business_context_input.fill(business_context)
        self.known_risks_input.fill(known_risks)

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