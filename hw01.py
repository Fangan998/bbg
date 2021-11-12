# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 16:29:43 2021

@author: George
"""

import requests,csv
path = 'Tainan_Social_Welfare.csv'
#file = open(path,'w',encoding='utf-8-sig')

r = requests.get('http://tnsmap.tainan.gov.tw/api/list.aspx')
data = r.json()['list']

#data[0]['id']
with open(path,'w',newline='',encoding='utf-8-sig') as fp:
     writer = csv.writer(fp)
     writer.writerow(['id','name','phone','o','u','k','d','addr','content','x y','url'])
     for i in range(len(data)):
         n_id       = data[i]['id']
         name       = data[i]['name']
         phone      = data[i]['phone']
         n_o        = data[i]['o']
         n_u        = data[i]['u']
         n_k        = data[i]['k']
         n_d        = data[i]['d']
         n_url      = data[i]['url']
         n_addr     = data[i]['addr']
         n_xy       = [data[i]['x'],data[i]['y']]
         content    = data[i]['content']
         writer.writerow([n_id,name,phone,n_o,n_u,n_k,n_d,n_addr,content,n_xy,n_url])