"""This tracks the last commit and prints out the results."""
import re
import subprocess
import os
import pytest
import requests
from git import Repo


# pylint: disable=W0601
def pytest_configure(config):
    """Get the slug of the user's repository and the user's github token and save
    them both in global variables."""
    global USERTOKEN
    global SLUG
    if config.pluginmanager.hasplugin("blame"):
        rawProcess = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"], stdout=subprocess.PIPE
        )
        if rawProcess == "":
            raise Exception(
                "No git repository found. Please run pytest-blame \
                            from inside a git repo."
            )
        output = rawProcess.stdout.decode("utf-8")
        regexMatches = re.search(r".*(/|:)(.+?/.+?)\.git", output)
        SLUG = regexMatches.group(2)
        USERTOKEN = os.environ["GITHUB_OAUTH_TOKEN"]


def pytest_addoption(parser):
    """Create --track option to run the plugin"""
    group = parser.getgroup("track")
    group.addoption(
        "--track",
        action="store_true",
        help="pytest-blame help \n--track: show last git commit",
    )


def getstatus(sha, TOKEN):
    """Get status of CI check from github"""
    # request data of the specific sha
    response = requests.get(
        "https://api.github.com/repos/" + SLUG + "/commits/" + str(sha) + "/check-runs",
        headers={
            "Authorization": f"token {TOKEN}",
            "Accept": "application/vnd.github.antiope-preview+json",
        },
    )
    raw = response.json()
    if raw["total_count"] != 0:
        status = raw["check_runs"][0]["conclusion"]
        return status
    return "failure"


# pylint: disable=E1101, C0200
def pytest_report_header():
    """Adjust the header of the report to display the information for last passing
    commit, failing commits, etc."""
    if pytest.config.getoption("track"):
        PATH = "."
        repo = Repo(PATH)
        commits = list(repo.iter_commits())
        for i in range(len(commits)):
            # check if the most recent commit is passing
            if getstatus(commits[i].hexsha, USERTOKEN) == "success" and i == 0:
                print(
                    "\nThe most recent commit is passing: ",
                    "https://github.com/" + SLUG + "/commit/" + commits[i].hexsha,
                    "\n",
                    commits[i].author,
                    ":",
                    commits[i].message,
                )
                break
            # check if no passing commit
            elif (
                # pylint: disable=C0330
                i == len(commits) - 1
                and getstatus(commits[i].hexsha, USERTOKEN) == "failure"
            ):
                print(
                    "\nCan't find passing commit, the most recent commit is failing: ",
                    "https://github.com/" + SLUG + "/commit/" + commits[0].hexsha,
                    "\n",
                    commits[0].author,
                    ":",
                    commits[0].message,
                )
                break
            # check if current commit is failing
            elif getstatus(commits[i].hexsha, USERTOKEN) == "failure":
                pass
            # traceback to find the last passing commit
            else:
                passingcommits = (
                    "\nMost recent passing commit: "
                    + "https://github.com/"
                    + SLUG
                    + "/commit/"
                    + commits[i].hexsha
                    + "\n"
                    + str(commits[i].author)
                    + ": "
                    + str(commits[i].message)
                    + "\n"
                    + "--------------------------------"
                )
                faillingcommits = ""
                # looping through all failing commits
                while i > 0:
                    faillingcommits = (
                        "\nFailing commit: "
                        + "https://github.com/"
                        + SLUG
                        + "/commit/"
                        + commits[i].hexsha
                        + "\n"
                        + str(commits[i - 1].author)
                        + ": "
                        + str(commits[i - 1].message)
                        + faillingcommits
                    )
                    i -= 1
                print(
                    passingcommits,
                    faillingcommits,
                    "\nThe first one is the most recent commit\n",
                )
                break
    # give msg a default value
    else:
        print("\nCan't find commits")
