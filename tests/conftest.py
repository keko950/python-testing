import pytest


@pytest.fixture
def test_fixture():
    print("called before each test function that requires this fixture")
    return 1
