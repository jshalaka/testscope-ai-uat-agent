from playwright.sync_api import Page, expect

from tests.automation.pages.testscope_home_page import (TestScopeHomePage as HomePage,) # pyright: ignore[reportMissingImports]


def test_requirement_form_accepts_business_details(
    page: Page,
    app_url: str,
) -> None:
    """Verify that a tester can enter core requirement information."""

    home_page = HomePage(page, app_url)
    response = home_page.open()

    assert response is not None
    assert response.ok

    home_page.fill_requirement_details(
        requirement_id="BR-PLAYWRIGHT-001",
        title="Transfer money to an existing UK beneficiary",
        user_story=(
            "As an authenticated customer, I want to transfer money "
            "to an existing UK beneficiary."
        ),
    )

    expect(home_page.requirement_id_input).to_have_value(
        "BR-PLAYWRIGHT-001"
    )
    expect(home_page.title_input).to_have_value(
        "Transfer money to an existing UK beneficiary"
    )
    expect(home_page.user_story_input).to_have_value(
        "As an authenticated customer, I want to transfer money "
        "to an existing UK beneficiary."
    )