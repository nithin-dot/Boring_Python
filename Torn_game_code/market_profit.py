import requests
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup
def Conversion(ch_data):
    return int(ch_data.text.strip().replace("market: ","").strip("$").replace(",",""))




def notify():
    point=45200
    URL = "https://yata.yt/bazaar/sets/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="d-flex flex-wrap align-items-center")
    # total_price=0
    for div_list in results:
        link = results.find_all("i")
        break
    print(f'{Fore.BLUE}Total Price Brought:\t{link[0].text.replace("market: ","")}\nMarket Price For Point:\t{"${:,.0f}".format(point*10)+Fore.GREEN}\nTotal Profit:\t{(point*10)-Conversion(link[0])}\nTotal Profit in %:\t{"{:.2f}".format((((point*10)/Conversion(link[0]))*100)-100)}%')
    #         #for plushie_list and  price 
    #         # plushie_list=div_element.find_all("div", {"data-act": "details"})
    #         # price_list=div_element.find_all("div", {"class": "item-table-header no-click"})
    #         table=div_element.find_all("div", {"class": "table-responsive"})
    #         break
    # for count,c_price in zip(table[0].find_all("td", {"class": "a text-end"}),table[0].find_all("td", {"class": "b text-end"})):
    #     if(Conversion(c_price)<=93500):
    #         print(f'https://www.torn.com/imarket.php#/p=shop&step=shop&type=&searchname=Camel%20Plushie  : {Conversion(c_price)} [{count.text.strip().strip("*")}]')
    #         break

notify()

# for plushie in price_list:
#     # print(f'{plushie.text.strip()} '+" "*(18-len(plushie.text.strip()))+f': {price}')
#     plushie_price.append(Conversion(plushie))
# for plushie,price in zip(sorted(plushie_price),h_plushie):
#     total_price+=price
#     # print(f'{plushie} : {price} : diff{price-plushie}')
# print(f'Total Price\t   : {"${:,.2f}".format(total_price)}')











