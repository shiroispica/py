import requests

with open('dataset_3378_2 (1).txt') as inf:
  url = inf.readline().strip()
r = requests.get(url, stream = False)
print(len(r.content.splitlines()))
with open('resp.txt','wb') as ouf:
  ouf.write(r.content)

