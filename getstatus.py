"""get status of CI check from github"""
import json
import requests


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
