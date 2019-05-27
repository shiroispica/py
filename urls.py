#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:22:28 2019

@author: shiroispica
"""

import requests
import re
from urllib.parse import urlparse
    
url = 'http://pastebin.com/raw/2mie4QYa' #input()

res = requests.get(url, stream = False)
lst = res.content.splitlines()
#lst = re.findall(rb'<a \.* href=\".+\">', res.content.decode())
#print(res.content.decode())
for u in lst:
    print(u)
    #print(urlparse(u).nethloc)

        
#print(url12)
#print(res.content)
