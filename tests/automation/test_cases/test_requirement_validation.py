from playwright.sync_api import Page, expect

from tests.automation.pages.testscope_home_page import ( # type: ignore
    TestScopeHomePage as HomePage,
)

def test_blank_title_is_rejected(
    page: Page,
    app_url: str,
    requirement_data: dict[str, str],
) -> None:
    """Verify that TestScope rejects a requirement with a blank title."""

    home_page = HomePage(page, app_url)
    response = home_page.open()

    assert response is not None
    assert response.ok

    home_page.fill_requirement_details(
        requirement_id=requirement_data["requirement_id"],
        title=requirement_data["title"],
        user_story=requirement_data["user_story"],
    )

    home_page.fill_requirement_context(
        domain=requirement_data["domain"],
        feature=requirement_data["feature"],
        acceptance_criteria=requirement_data["acceptance_criteria"],
        business_context=requirement_data["business_context"],
        known_risks=requirement_data["known_risks"],
    )

    # Make one otherwise-valid requirement field invalid.
    home_page.title_input.fill("")

    home_page.submit_requirement()

    expect(
        home_page.validation_error_alert
    ).to_be_visible(timeout=10_000)

    expect(
        home_page.validation_error_alert
    ).to_contain_text("title")

    expect(
        home_page.validation_error_alert
        ).to_contain_text(
        "String should have at least 1 character"
    )