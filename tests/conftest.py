""" This tracks the last commit and prints out the results. """
import pytest
import requests
import json
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
    response = requests.get('https://api.github.com/repos/inTestiGator/pytest-blame/statuses/' + str(sha))
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
            if getstatus(commits[i].hexsha) == "success":
                pass
            else:
                msg = print(
                    "\nLast passing commit --> ", commits[i-1].author, ":", commits[i-1].message,
                )
                break
    else:
        msg = print("Can't find the last passing commit")
    return msg
