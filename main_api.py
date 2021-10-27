# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:33:14 2021

@author: CJCU-CC
"""
import requests,csv
path = 'politics.csv'
#file = open(path,'w',encoding='utf-8-sig')

r = requests.get('https://www.cec.gov.tw/referendum/api/data')
data = r.json()
with open(path,'w',newline='',encoding='utf-8-sig') as fp:
    writer = csv.writer(fp)
    writer.writerow(['no','date','title','txt','attach'])
    for i in range(len(data)):
        title   = data[i]['title']
        content = data[i]['content']
        for j in range(len(content)):
            no     = content[j]['no']
            date   = content[j]['date']
            txt    = content[j]['content']
            attach = content[j]['attach']
        writer.writerow([no,date,title,txt,attach])
    #incsv_txt = f"{no},{date},{title},{txt},{attach}"
    

#title = [i['title'] for i in data]
#data[1]['content'][1]['date']
#contact=[i['content'] for i in data]
#license

#print(r.)
    
#    with open(path,'w',encoding='utf-8') as fp:
#        fp.write(r.text)
#        print('complete')

