# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 09:59:43 2021

@author: CJCU-CC
"""

import requests,re
import csv
from bs4 import BeautifulSoup

url ='https://zh.wikipedia.org/zh-tw/2019%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%97%85%E5%85%A8%E7%90%83%E5%90%84%E5%9C%B0%E7%96%AB%E6%83%85'
r = requests.get(url)
r_s = BeautifulSoup(r.text,'lxml')
#class = wikitable mw-collapsible sortable jquery-tablesorter mw-made-collapsible
#id = covid19-container
rid_coivd=r_s.find(id ='covid19-container')
get_tr=rid_coivd.findAll('tr')

path = 'covid_data.csv'
with open(path,'w',newline='',encoding='utf-8-sig')as fp:
    wr = csv.writer(fp)
    for row in get_tr:
        rowList=[]
        for cell in row.findAll(['td','th']):
            a = re.sub('\n','',cell.text)
            b = re.sub(' ','',a)
            rowList.append(b)
        wr.writerow(rowList)


