import json
import requests
import pytest


def test_json_file_request():
    b_url = "https://fakerestapi.azurewebsites.net"
    header = {"Content-Type": "application/json", "Accept": "text/plain"}

    with open("api/json_payload.json", "r") as json_file:
        json_payload = json.load(json_file)

    response = requests.post(
        f"{b_url}/api/v1/Activities", headers=header, json=json_payload
    )

    print(response.json())
    assert response.status_code == 200


test_json_file_request()
