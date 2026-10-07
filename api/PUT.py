import requests

baseurl = "https://fakerestapi.azurewebsites.net"

header = {"Content-Type": "application/json", "Accept": "text/plain"}

request_payload = {
    "id": 499,
    "title": "Akki",
    "dueDate": "2026-10-07T14:54:39.078Z",
    "completed": True,
}

response = requests.put(
    baseurl + "/api/v1/Activities/3", headers=header, json=request_payload
)

assert response.status_code == 200
assert response.json()["id"] == 499
print(response.json()["id"])
