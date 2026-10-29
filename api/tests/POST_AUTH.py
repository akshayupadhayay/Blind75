import requests

baseurl = "https://gorest.co.in/public/v2/users"

header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 3ed9c62da6c2f2359589f68d3a7e96fee5034b161157ebc7dc1b139382ef6f8f",
}

request_payload = {
    "name": "Tenali Ramakrishna",
    "email": "tenali2216@example.com",
    "gender": "male",
    "status": "active",
}

response = requests.post(baseurl, headers=header, json=request_payload)

assert response.status_code == 201

getResponse = requests.get(baseurl + "/" + str(response.json()["id"]), headers=header)

print(getResponse.json())
