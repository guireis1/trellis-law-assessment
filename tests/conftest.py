import pytest
from starlette.testclient import TestClient

from core.server import create_app


@pytest.fixture()
def test_client():
    app = create_app()
    with TestClient(app) as test_client:
        yield test_client
