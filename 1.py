import requests
res = requests.get('http://www.feng.com')
print(res.status_code)
