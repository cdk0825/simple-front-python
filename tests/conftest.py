import pytest

@pytest.fixture(scope="session")
def base_url():
    # jsonplaceholder base url
    return "https://jsonplaceholder.typicode.com"
