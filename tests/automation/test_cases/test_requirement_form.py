from playwright.sync_api import Page, expect

from tests.automation.pages.testscope_home_page import ( # pyright: ignore[reportMissingImports]
    TestScopeHomePage as HomePage,
)


def test_requirement_form_accepts_business_details(
    page: Page,
    app_url: str,
    requirement_data: dict[str, str],
) -> None:
    """Verify that a tester can enter a complete business requirement."""

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

    expect(home_page.requirement_id_input).to_have_value(
        requirement_data["requirement_id"]
    )
    expect(home_page.title_input).to_have_value(
        requirement_data["title"]
    )
    expect(home_page.domain_input).to_have_value(
        requirement_data["domain"]
    )
    expect(home_page.feature_input).to_have_value(
        requirement_data["feature"]
    )
    expect(home_page.user_story_input).to_have_value(
        requirement_data["user_story"]
    )
    expect(home_page.acceptance_criteria_input).to_have_value(
        requirement_data["acceptance_criteria"]
    )
    expect(home_page.business_context_input).to_have_value(
        requirement_data["business_context"]
    )
    expect(home_page.known_risks_input).to_have_value(
        requirement_data["known_risks"]
    )