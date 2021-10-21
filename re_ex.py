# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 09:54:51 2021

@author: CJCU-CC
"""

import requests
path = 'flagl.txt'
try:
    r = requests.get('http://www.flag.com.tw')
    
    with open(path,'w',encoding='utf-8') as fp:
        fp.write(r.text)
        print('complete')

except requests.exceptions.RequestException as ex1:
    print(ex1)

except :
    print('Error')
    
