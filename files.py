import requests

with open('dataset_3378_3.txt') as inf:
  url = inf.readline().strip()
r = requests.get(url, stream = False)
name = r.content.strip().decode()
nurl = 'https://stepic.org/media/attachments/course67/3.6.3/' + name
print(nurl)
