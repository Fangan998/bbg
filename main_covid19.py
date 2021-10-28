import requests
from bs4 import BeautifulSoup
#import urllib
#https://zh.wikipedia.org/wiki/2019%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%97%85%E5%85%A8%E7%90%83%E5%90%84%E5%9C%B0%E7%96%AB%E6%83%85
url_1 ='https://zh.wikipedia.org/wiki/2019%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%97%85%E5%85%A8%E7%90%83%E5%90%84%E5%9C%B0%E7%96%AB%E6%83%85'
r_data = requests.get(url_1)


r_data.encoding = 'utf8'
soup = BeautifulSoup(r_data.text,'lxml')

#table class = wikitable mw-collapsible sortable jquery-tablesorter mw-made-collapsible

covid_n = soup.find(id ='covid19-container')
#list_covid_n_s = BeautifulSoup(covid_n.text,'lxml')
#list_covid_n   =
