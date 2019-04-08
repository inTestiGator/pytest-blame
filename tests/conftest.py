""" This tracks the last commit and prints out the results. """
import pytest
from git import Repo

pytest_plugins = "pytester"


def pytest_addoption(parser):
    """ Print stuff to header with --track """
    group = parser.getgroup("track")
    group.addoption(
        "--track",
        action="store_true",
        help="pytest-blame help \n--track: show last git commit",
    )


# pylint: disable=E1101
def pytest_report_header():
    """ Display github commit in header """
    if pytest.config.getoption("track"):
        PATH = "."
        repo = Repo(PATH)
        commits = list(repo.iter_commits())
        msg = print(
            "\nLast passing commit --> ", commits[0].author, ":", commits[0].message
        )
    else:
        msg = print("Can't find the last passing commit")
    return msg


@pytest.fixture
def no_arguments():
    """Return no command-line arguments"""
    return []
