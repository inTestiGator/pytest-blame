import requests
import json

def getstatus():
    response = requests.get('https://api.github.com/repos/inTestiGator/pytest-blame/commits/heads/master/status')
    print(response)
    statuses = json.loads(response.text)
    print(type(statuses))

    for i in statuses:
        print(statuses[i])

getstatus()
