import pytest
from clients.api_client import APIClient

@pytest.fixture
def client():
    return APIClient()