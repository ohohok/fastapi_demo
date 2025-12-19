import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def http_client():
    """Create test client"""
    return TestClient(app)


def test_root_endpoint(http_client):
    response = http_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_stream_demo_endpoint(http_client):
    response = http_client.get("/stream_demo")
    assert response.status_code == 200
    assert "text/event-stream" in response.headers["content-type"]
