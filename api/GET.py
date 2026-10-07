import requests

# https://api.github.com/search/repositories?q=language%3Apython&sort=stars&order=desc&page=2

header = {"Accept": "*/*", "Content-Type": "application/json"}

response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "language:python", "sort": "stars", "order": "desc"},
    headers=header,
)

print(response.status_code)

json_response = response.json()
popular_repositories = json_response["items"]
for repo in popular_repositories[:3]:
    print(f"Name: {repo['name']}")
    print(f"Description: {repo['description']}")
    print(f"Stars: {repo['stargazers_count']}\n")


response = requests.post(
    "https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=header
)

print(response.status_code)
