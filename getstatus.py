"""get status of CI check from github"""
import json
import requests


def getstatus(sha):
    response = requests.get(
        "https://api.github.com/repos/inTestiGator/(sha)
    )
    statuses = json.loads(response.text)
    if statuses == []:
        check = "failure"
    else:
        state = statuses[0]
        check = state["state"]
    return check
