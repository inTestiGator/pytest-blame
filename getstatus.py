import requests
import json


def getstatus(sha):
    response = requests.get('https://api.github.com/repos/inTestiGator/pytest-blame/statuses/' + str(sha))
    statuses = json.loads(response.text)
    if statuses == []:
        check = "failure"
    else:
        state = statuses[0]
        check = state["state"]
    return check


print(getstatus("a1b86303fe8d88f45e7973b274153c44c0bbbd6b"))
