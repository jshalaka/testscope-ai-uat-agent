import json
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def app_url() -> str:
    """Return the local TestScope AI application URL."""
    return "http://localhost:8501"


@pytest.fixture(scope="session")
def requirement_data() -> dict[str, str]:
    """Load the sample banking requirement used by UI tests."""

    project_root = Path(__file__).resolve().parents[2]
    data_file = (
        project_root
        / "test_data"
        / "automation"
        / "sample_requirement.json"
    )

    return json.loads(data_file.read_text(encoding="utf-8"))