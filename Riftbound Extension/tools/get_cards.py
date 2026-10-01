import requests

API_KEY = "RGAPI-06ee9002-e5ff-4d95-8e2f-5eeb550cc614"

url = "https://americas.api.riotgames.com/riftbound/content/v1/contents"

response = requests.get(
    url,
    headers={
        "X-Riot-Token": API_KEY
    }
)

print("Status:", response.status_code)
print("Headers:", response.headers)
print("Body:", response.text)
url = "https://americas.api.riotgames.com/riftbound/content/v1/contents"

headers = {
    "X-Riot-Token": API_KEY
}

params = {
    "locale": "en-US"
}


response = requests.get(
    url,
    headers=headers,
    params=params
)


print("Status:", response.status_code)

print(response.text)