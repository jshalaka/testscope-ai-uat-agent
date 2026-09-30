import pytest

@pytest.fixture(scope="session")
def app_url() -> str:
    """return the application URL used by the Playwright tests."""
    return "http://localhost:8501"
