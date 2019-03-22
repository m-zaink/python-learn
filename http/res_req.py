import requests as r
url = 'http://www.google.com'

res = r.get(url)

print(res.status_code)
