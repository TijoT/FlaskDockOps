import pytest

from .. server.webapp import app

@pytest.fixture
def client():
    yield app.test_client()