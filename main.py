# use the api
# html web scrapping using some tool like bs4

#from http.client import REQUESTED_RANGE_NOT_SATISFIABLE


import requests
from bs4 import BeautifulSoup
url="https://www.magmabrakes.com/catalog/"

page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
lists=soup.find_all('ul',class_="product columns-4")

with open('brakes.csv','w',encoding='utf8',newline='') as f:
    thewriter= writer(f)
    header=['anchors']
    thewriter.writerow(header)

for list in lists:
    anchors=list.find('a',class_="woocommerce-Loopproduct-link woocommerce-loop-product_link").text.replace('\n','')
    info=[anchors]
    thewriter.writerow(info)

