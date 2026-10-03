from playwright.sync_api import Page,expect
from tests.automation.pages.testscope_home_page import (TestScopeHomePage as HomePage,) # pyright: ignore[reportMissingImports]

def test_testscope_application_loads(page: Page, app_url: str) -> None:
    """Verify that the TestScope AI application loads successfully."""
    

    home_page = HomePage(page, app_url)
    response= home_page.open()

    assert response is not None
    assert response.ok
    assert page.url.startswith(app_url)

    expect(home_page.heading).to_be_visible(timeout=15_000)

