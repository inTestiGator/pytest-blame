""" This tracks the last commit and prints out the results. """
import pytest
from git import Repo


def pytest_addoption(parser):
    """ Print stuff to header with --track """
    group = parser.getgroup("track")
    group.addoption(
        "--track",
        action="store_true",
        help="pytest-blame help :D\n--track: show last git commit",
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
    return msg
