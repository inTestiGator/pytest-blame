""" This tracks the last commit and prints out the results. """
import pytest
import json
import requests
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


def getstatus(sha):
    """get status of CI check from github"""
    response = requests.get(
        "https://api.github.com/repos/inTestiGator/pytest-blame/statuses/" + str(sha)
    )
    statuses = json.loads(response.text)
    if statuses == []:
        check = "failure"
    else:
        state = statuses[0]
        check = state["state"]
    return check


# pylint: disable=E1101
def pytest_report_header():
    """ Display github commit in header """
    if pytest.config.getoption("track"):
        PATH = "."
        repo = Repo(PATH)
        commits = list(repo.iter_commits())
        for i in range(len(commits)):
            if getstatus(commits[i].hexsha) == "success" and i == 0:
                msg = print(
                    "\nThe most recent commit is passing --> ",
                    commits[i].author,
                    ":",
                    commits[i].message,
                )
            elif i == len(commits) - 1 and getstatus(commits[i].hexsha) == "failure":
                msg = print(
                    "\nCan't find passing commit, the most recent commit is failling --> ",
                    commits[0].author,
                    ":",
                    commits[0].message,
                )
                break
            elif getstatus(commits[i].hexsha) == "failure":
                pass
            else:
                msg = print(
                    "\nMost recent passing commit --> ",
                    commits[i].author,
                    ":",
                    commits[i].message,
                )
                break
    else:
        msg = print("Can't find commits")
    return msg

@pytest.fixture
def no_arguments():
    """Return no command-line arguments"""
    return []
