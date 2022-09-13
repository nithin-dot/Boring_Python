from time import sleep
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from plyer import notification
import time
def Conversion(ch_data):
    return int(ch_data.text.strip().strip("$").replace(",",""))




def notify():
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    URL = "https://yata.yt/bazaar/sets/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="loop-over-item-sell-table-Plushie")
    div_element = results.find("div", class_="row row-cols-auto justify-content-center")
    # total_price=0
    for div_list in div_element:
        link = div_element.find_all("div", {"class": "col item-table p-0 mx-1 mb-2"})
        for tag in link:
            #for plushie_list and  price 
            # plushie_list=div_element.find_all("div", {"data-act": "details"})
            # price_list=div_element.find_all("div", {"class": "item-table-header no-click"})
            table=div_element.find_all("div", {"class": "table-responsive"})
            break
    for count,c_price in zip(table[0].find_all("td", {"class": "a text-end"}),table[0].find_all("td", {"class": "b text-end"})):
        if(Conversion(c_price)<=93500):
            print(f'https://www.torn.com/imarket.php#/p=shop&step=shop&type=&searchname=Camel%20Plushie  : {Conversion(c_price)} [{count.text.strip().strip("*")}] at {current_time}')
            notification.notify(
            title = "TORN BAZAAR",
            message=f'CAMEL PLUSHIE  x  {count.text.strip().strip("*")} at ${Conversion(c_price)}',
           
            # displaying time
            timeout=5
        )
            break
        else:
            print(f'Above the Market price : {Conversion(c_price)} [{count.text.strip().strip("*")}] at {current_time}')
            break

while True:
    notify()
    time.sleep(3)
# for plushie in price_list:
#     # print(f'{plushie.text.strip()} '+" "*(18-len(plushie.text.strip()))+f': {price}')
#     plushie_price.append(Conversion(plushie))
# for plushie,price in zip(sorted(plushie_price),h_plushie):
#     total_price+=price
#     # print(f'{plushie} : {price} : diff{price-plushie}')
# print(f'Total Price\t   : {"${:,.2f}".format(total_price)}')











# plushie=[]
# plushie_price=[]
# h_plushie_price=[]
# h_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRiA_TVEvGb7BU_OJzSEK5XicacoqNsXtBHnHsfYYPS-rjC1zCm_l8ifZ61ITL_sYcU4UW_sQdxBfN5/pubhtml?gid=641912627&single=true"
# h_page = requests.get(h_URL)
# h_soup = BeautifulSoup(h_page.content, "html.parser")
# h_plushie= h_soup.find("tbody")
# Counter=0
# for h_price in h_plushie:
#     if len((h_price.find_all("td", class_="s26")))>1:
        
#         if(Counter<11):
#             h_plushie_price.append(Conversion(h_price.find_all("td", class_="s26")[1]))
#         else:
#             h_plushie_price.append(Conversion(h_price.find_all("td", class_="s26")[0]))
#             break
#         Counter+=1
#     elif len((h_price.find_all("td", class_="s30")))>1:
#         Counter+=1
#         h_plushie_price.append(Conversion(h_price.find_all("td", class_="s30")[1]))
# h_plushie=sorted(h_plushie_price)