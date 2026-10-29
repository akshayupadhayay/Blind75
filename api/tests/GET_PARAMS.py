import requests

baseurl = "https://gorest.co.in"

header = {"Content-Type": "application/json"}

parameters = {"page": "2", "per_page": "3"}

response = requests.get(
    baseurl + "/" + "/public/v2/users", headers=header, params=parameters
)

print(response.json())
