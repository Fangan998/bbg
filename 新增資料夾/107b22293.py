# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 09:36:30 2021

@author: CJCU-CC
"""
import requests
from bs4 import BeautifulSoup
#
url = 'https://zh.wikipedia.org/zh-tw/2019%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%97%85%E6%AD%BB%E4%BA%A1%E7%97%85%E4%BE%8B%E6%95%B8'
r=requests.get(url)
#id = mw-content-text
r_s    = BeautifulSoup(r.text,'lxml')
re     = r_s.find(id = 'mw-content-text')
get_h2 = re.findAll('h2')

for i in range(len(get_h2)-1):
    he_txt = get_h2[i+1].find(class_='mw-headline')
    print(he_txt.text)