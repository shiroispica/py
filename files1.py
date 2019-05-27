import requests

def f(url):
  req = requests.get(url, stream = False)
  content = req.content.strip().decode()
  return content

with open('dataset_3378_3.txt') as inf:
  furl = inf.readline().strip()

name = f(furl)
while name.find('We ') == -1:
  print('no text')
  nurl = 'https://stepic.org/media/attachments/course67/3.6.3/' + name
  name = f(nurl)
  print(name, '\n')
  
if name.find('We ') != -1:
  with open('We.txt','w') as ouf:
    ouf.write(name)
