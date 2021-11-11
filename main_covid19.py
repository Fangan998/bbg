import requests,csv
from bs4 import BeautifulSoup
import urllib.request as ulreq
#import urllib
#https://zh.wikipedia.org/wiki/2019%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%97%85%E5%85%A8%E7%90%83%E5%90%84%E5%9C%B0%E7%96%AB%E6%83%85
url_1 ='https://zh.wikipedia.org/wiki/2019%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%97%85%E5%85%A8%E7%90%83%E5%90%84%E5%9C%B0%E7%96%AB%E6%83%85'
r_data = requests.get(url_1)

soup = BeautifulSoup(r_data.text,'lxml')

#table class = wikitable mw-collapsible sortable jquery-tablesorter mw-made-collapsible

covid_n = soup.find(id ='covid19-container')
covid_n_rows = covid_n.findAll('tr')  #<tr>
res=[]
path = 'covid19_world.csv'
#
for row in covid_n_rows:
    rowList=[]
    for cell in row.findAll(['td','th']):
        rowList.append(cell.get_text().replace('\n',''))
    res.append(rowList[:4])
    
with open(path,'w',newline= '',encoding='utf-8-sig') as fp:
    writer = csv.writer(fp)
    for i in range(len(res)-2):
        writer.writerow(res[i])
        
#img gallery mw-gallery-nolines
covid_img   = soup.find(class_='gallery')
covid_img_n = covid_img.findAll('li')
img_o_url = []
for i in range(len(covid_img_n)):
    img_tag= covid_img_n[i].find('img')
    img_src= img_tag.get('src')
    req = ulreq.urlopen('https:'+img_src)    
    img_a   = covid_img_n[i].a.get('href')
    img_o_url.append(img_a)
    with open('imges\\' +str(i).zfill(5)+ '.jpg','wb') as fp:
        size = 0
        while True:
            info = req.read(10000)
            if len(info)<1:
                break
            size += len(info)
            fp.write(info)            
    print(f"{str(i).zfill(5)}.jpg ,size is {size}")
    
#https://zh.wikipedia.org
#for i in range(len(img_o_url)):
r_img_data = requests.get('https://zh.wikipedia.org'+img_o_url[0])
img_soup = BeautifulSoup(r_img_data.text,'lxml')
o_img_c = img_soup.find(class_='fullImageLink')
o_img = o_img_c.find('a').get('href')
img_o_req = ulreq.urlopen('https:'+o_img)
with open('imges\\o_' +str(9).zfill(5)+ '.jpg','wb') as fp:
        size = 0
        while True:
            info = img_o_req.read(10000)
            if len(info)<1:
                break
            size += len(info)
            fp.write(info)            
        print(f"o_{str(0).zfill(5)}.jpg ,size is {size}")
     
     