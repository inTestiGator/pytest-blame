"""This tracks the last commit and prints out the results."""
import pytest

# import json
# import requests
# import re
# import subprocess
#
# from git import Repo

global USERTOKEN
USERTOKEN = " "

pytest_plugins = "pytester"


@pytest.fixture
def TOKEN():
    return USERTOKEN


# def pytest_configure(config):
#     global SLUG
#     rawProcess = subprocess.run(
#         ["git", "config", "--get", "remote.origin.url"], stdout=subprocess.PIPE
#     )
#     output = rawProcess.stdout.decode("utf-8")
#     regexMatches = re.search(r".*(/|:)(.+?/.+?)\.git", output)
#     SLUG = regexMatches.group(2)
#
#
# def pytest_addoption(parser):
#     """Print stuff to header with --track"""
#     group = parser.getgroup("track")
#     group.addoption(
#         "--track",
#         action="store_true",
#         help="pytest-blame help \n--track: show last git commit",
#     )
#
#
# def getstatus(sha):
#     """Get status of CI check from github"""
#     # request data of the specific sha
#     response = requests.get(
#         "https://api.github.com/repos/" + SLUG + "/statuses/" + str(sha)
#     )
#     # read json data and convert it to list
#     statuses = json.loads(response.text)
#     # statuses will be an empty list if the state is failling or pending
#     if statuses == []:
#         check = "failure"
#     else:
#         state = statuses[0]
#         check = state["state"]
#     return check
#
#
# # pylint: disable=E1101
# def pytest_report_header():
#     """Display github commits"""
#     if pytest.config.getoption("track"):
#         PATH = "."
#         repo = Repo(PATH)
#         commits = list(repo.iter_commits())
#         for i in range(len(commits)):
#             # check if the most recent commit is passing
#             if getstatus(commits[i].hexsha) == "success" and i == 0:
#                 print(
#                     "\nThe most recent commit is passing: ",
#                     "https://github.com/" + SLUG + "/commit/" + commits[i].hexsha,
#                     "\n",
#                     commits[i].author,
#                     ":",
#                     commits[i].message,
#                 )
#                 break
#             # check if no passing commit
#             elif i == len(commits) - 1 and getstatus(commits[i].hexsha) == "failure":
#                 print(
#                     "\nCan't find passing commit, the most recent commit is failing: ",
#                     "https://github.com/" + SLUG + "/commit/" + commits[0].hexsha,
#                     "\n",
#                     commits[0].author,
#                     ":",
#                     commits[0].message,
#                 )
#                 break
#             # check if current commit is failing
#             elif getstatus(commits[i].hexsha) == "failure":
#                 pass
#             # find the most recent passing commit
#             else:
#                 passingcommits = (
#                     "\nMost recent passing commit: "
#                     + "https://github.com/"
#                     + SLUG
#                     + "/commit/"
#                     + commits[i].hexsha
#                     + "\n"
#                     + str(commits[i].author)
#                     + ": "
#                     + str(commits[i].message)
#                     + "\n"
#                     + "--------------------------------"
#                 )
#                 faillingcommits = ""
#                 # looping through all failing commits
#                 while i > 0:
#                     faillingcommits = (
#                         "\nFailing commit: "
#                         + "https://github.com/"
#                         + SLUG
#                         + "/commit/"
#                         + commits[i].hexsha
#                         + "\n"
#                         + str(commits[i - 1].author)
#                         + ": "
#                         + str(commits[i - 1].message)
#                         + faillingcommits
#                     )
#                     i -= 1
#                 print(
#                     passingcommits,
#                     faillingcommits,
#                     "\nThe last one is the most recent commit\n",
#                 )
#                 break
#     # give msg a default value
#     else:
#         print("\nCan't find commits")
#
#
# @pytest.fixture
# def no_arguments():
#     """Return no command-line arguments"""
#     return []
