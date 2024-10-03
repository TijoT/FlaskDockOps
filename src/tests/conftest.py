import pytest

from src.server.webapp import app

@pytest.fixture
def client():
    yield app.test_client()