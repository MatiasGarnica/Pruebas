import requests

response = requests.get(
    "https://api.github.com/search/repositories",
    params = {"q":"python"}
)

data = response.json()
print(data.keys())



