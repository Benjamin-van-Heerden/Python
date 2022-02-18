import requests
import re

response = requests.get('http://www.google.com/')
print(response.text[:300])

print(response.request.headers)

print(response.ok)

print(response.status_code)

url = "https://www.coursera.org/learn/automating-real-world-tasks-python/supplement/QuFXx/useful-operations-for-python-requests"

response = requests.get(url)

if not response.ok:
    raise Exception(f"GET failed status code {response.status_code}")
else:
    look = re.findall(r"If the boolean isn’t specific enough for your needs", response.text)
    if bool(look):
        print(look)
    else:
        print("not found")

# the if block above can be replaced with response.raise_for_status() which is None if all is good
# i.e.

print(response.raise_for_status())

##
print("----------------")
##

url = "https://example.com/path/to/api"

p = {
    "description": "white kitten", 
    "name": "Snowball",
    "age_months": 6
}

response = requests.get(url, params=p) #params argument typically replaced with the somewhat equivalent json argument

print(response.request.url)
print("-----")

response = requests.post(url, data=p)

print(response)