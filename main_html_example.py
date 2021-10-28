# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:23:48 2021

@author: CJCU-CC
"""

import requests
from bs4 import BeautifulSoup
url = 'https://www.hky.idv.tw/example.html'
r   = requests.get(url)
r.encoding = 'utf-8'

#load Beautifu Soup model
soup = BeautifulSoup(r.text,'lxml')

#print tag a 
#print(soup.find('a').string)

#tag_p = soup.find(name='p')
#tag_a = soup.find(name='a')

#print(tag_p.a.string)
#print(tag_a.string)

#tag_div_email = soup.find(id='email')
#print(tag_div_email.string)
div_q1 = soup.find(name = 'div',id='q1')

