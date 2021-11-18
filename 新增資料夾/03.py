# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 10:35:21 2021

@author: CJCU-CC
"""

import requests,re
#import csv
from bs4 import BeautifulSoup
import urllib.request as ulreq

url ='https://zh.wikipedia.org/zh-tw/2019%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%97%85%E5%85%A8%E7%90%83%E5%90%84%E5%9C%B0%E7%96%AB%E6%83%85'
r = requests.get(url)
r_s = BeautifulSoup(r.text,'lxml')
#class = gallery mw-gallery-nolines
rid_coivd=r_s.find(class_ = 'gallery mw-gallery-nolines')
get_li=rid_coivd.findAll('li')
#pass_img = '.svg'

for i in range(len(get_li)):
    img_ulr = 'https://zh.wikipedia.org'+get_li[i].a.get('href')
    if(img_ulr.find('.svg')>=1):
        print('aaa')
        pass
    else:
        rep  = requests.get(img_ulr)
        re_s = BeautifulSoup(rep.text,'lxml')
        req_img = re_s.find(class_ = 'fullImageLink')
        r_a = req_img.a.get('href')
        path = 'img/'+str(i)+'.jpg'
        resa = ulreq.urlopen('https:'+r_a)
        with open(path,'wb') as fp:
            while True:
                size = 0
                info = resa.read(10000)
                if len(info)<1:
                    break
                size = size +len(info)
                
                fp.write(info)
        print(info)
        
    #img = 