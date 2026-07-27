import json, urllib.request
url = 'https://api.github.com/users/Minta1234/repos?per_page=100'
req = urllib.request.Request(url, headers={'Accept':'application/vnd.github+json','User-Agent':'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=20) as r:
    data = json.load(r)
print('count', len(data))
for repo in data[:5]:
    print(repo['name'], repo['html_url'])
