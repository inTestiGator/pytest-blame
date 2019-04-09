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


print(getstatus("063c3eab098a3054c468dfee08405e4ef055c261"))
