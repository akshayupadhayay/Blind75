import requests

baseurl = "https://fakerestapi.azurewebsites.net"

header = {"Accept": "*/*", "Content-Type": "application/json"}

request_payload = {
    "id": 45,
    "title": "akki",
    "dueDate": "2026-10-07T13:02:52.675Z",
    "completed": True,
}

response = requests.post(
    url=baseurl + "/api/v1/Activities", headers=header, json=request_payload
)

data = response.json()

assert response.status_code == 200
assert data["id"] == 45
