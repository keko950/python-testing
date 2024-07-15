import pytest

"""conftest.py

This file serves a critical role configurin and sharing fixtures, hooks,
and plugins across multiple test files. It is automatically discovered by pytest.

Fixtures are key features in pytest used to set up some precodintiions
for tests.

conftest.py allow these fixtures to be shared across multiple test modules.

"""


@pytest.fixture
def test_fixture():
    print("called before each test function that requires this fixture")
    return 1

def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark a test as a slow")

# Custom hook
def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def pytest_runtest_setup(item):
    print(f"setting up {item}")
    if "slow" in item.keywords and not item.config.getoption("--runslow"):
        pytest.skip("Skipping slow tests")
