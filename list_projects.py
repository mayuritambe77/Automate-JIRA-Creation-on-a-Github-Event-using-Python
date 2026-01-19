# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://mayuritambe777jira.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0C3A6_wSW-pa4NLZvNDOGz6Jrgo2blgDMUxuWcKiyaC1D2zBno2y74a0JOsnSH8H18vXMqXG5MpXCqmNVImqKGJNU-v0sola-iLSjwGkAOb3dz8sdBxRbGDpitbcF2IYeqmUpOMtJcZmwHKOjsEnh0sc453JsaotYh7oKGSpBDqQ=83F8DB33"
auth = HTTPBasicAuth("mayuritambe777@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)
