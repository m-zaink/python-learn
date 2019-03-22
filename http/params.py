import requests as req

url = 'https://icanhazdadjoke.com/search'

res = req.get(
    url,
    headers={'Accept': 'application/json'},
    params={'term': 'cat'}
)

data = res.json()

for result in data['results']:
    print(result['joke'])
# print(data['results'])
# print(data['joke'])