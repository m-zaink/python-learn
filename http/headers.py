import requests as r

url = 'https://www.icanhazdadjoke.com'

res = r.get(url, headers={'Accept': 'application/json'})

# print(res.text)
data = res.json()   # shall be a python dictionary

print(data['joke']) 