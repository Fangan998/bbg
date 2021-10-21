# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:33:14 2021

@author: CJCU-CC
"""

import requests,json
path = ''


r = requests.get('https://www.cec.gov.tw/referendum/api/data')
data = r.json()

title = [i['title'] for i in data]
#data[1]['content'][1]['date']
#contact=[i['contact'] for i in data]
license

#print(r.)
    
#    with open(path,'w',encoding='utf-8') as fp:
#        fp.write(r.text)
#        print('complete')

