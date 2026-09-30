from playwright.sync_api import Page,expect

def test_testscope_application_loads(page: Page, app_url: str) -> None:
    """Verify that the TestScope AI application loads successfully."""
    response = page.goto(app_url)

    assert response is not None
    assert response.ok
    assert page.url.startswith(app_url)

    expect(page.get_by_text("Testscope AI", exact=False).first).to_be_visible(timeout=15_000)