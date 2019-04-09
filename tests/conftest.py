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


# m = re(r".*(/|:)(.+?/.+?)\.git", string)
# m.group(2)
def getstatus(sha):
    """get status of CI check from github"""
    response = requests.get(
        "https://api.github.com/repos/inTestiGator/pytest-blame/statuses/" + str(sha),
        headers={"Authorization" : "token c839aadbb62354cb1d205ffd7c06ecc1f53b43ae"}
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
    """Display github commits"""
    if pytest.config.getoption("track"):
        PATH = "."
        repo = Repo(PATH)
        commits = list(repo.iter_commits())
        for i in range(len(commits)):
            # check if the most recent commit is passing
            if getstatus(commits[i].hexsha) == "success" and i == 0:
                msg = print(
                    "\nThe most recent commit is passing --> ",
                    commits[i].author,
                    ":",
                    commits[i].message,
                )
                break
            # check if no passing commit
            elif i == len(commits) - 1 and getstatus(commits[i].hexsha) == "failure":
                msg = print(
                    "\nCan't find passing commit, the most recent commit is failling --> ",
                    commits[0].author,
                    ":",
                    commits[0].message,
                )
                break
            # check if current commit is failling
            elif getstatus(commits[i].hexsha) == "failure":
                pass
            # find the most recent passing commit
            else:
                passingcommits = (
                    "\nMost recent passing commit --> "
                    + str(commits[i].author)
                    + ":"
                    + str(commits[i].message)
                )
                faillingcommits = ""
                # looping through all failling commits
                while i > 0:
                    faillingcommits = (
                        "\nFailling commit --> "
                        + str(commits[i - 1].author)
                        + ":"
                        + str(commits[i - 1].message)
                        + faillingcommits
                    )
                    i -= 1
                msg = print(
                    passingcommits,
                    faillingcommits,
                    "\nThe last one is the most recent commit\n",
                )
                break
    # give msg a default value
    else:
        msg = print("\nCan't find commits")
    return msg


@pytest.fixture
def no_arguments():
    """Return no command-line arguments"""
    return []
