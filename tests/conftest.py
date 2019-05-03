"""This tracks the last commit and prints out the results."""
import pytest

global USERTOKEN
USERTOKEN = " "

pytest_plugins = "pytester"


@pytest.fixture
def TOKEN():
    return USERTOKEN
