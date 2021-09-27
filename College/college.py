import json
import urllib.request
import re
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import tabula
from pathlib import Path
import pandas as pd
import csv
import sys

# number = input('Enter number to find\n')
c_csv = csv.reader(open('tnea_2021.csv', "r"), delimiter=",")
p_csv = csv.reader(open('tnea_2020.csv', "r"), delimiter=",")
number = '245617'
# number = input("Enter the Appliction Number : ")
# collge_type=input("Do you only want Autonomous collge\nPlease enter (y/n) : ")
# if collge_type == "y": 
    # Do this. 
Autonomous='Autonomous'
# else: 
#    Autonomous=''
dep_cod=input("Enter the course code : ")
for row in c_csv:
    #if current rows 2nd value is equal to input, print that row
    if number == row[1]:
        #  print ("Rank : "+row[0])
        #  print ("Application Number :"+row[1])
        #  print ("Name of the Candidate :"+row[2])
        #  print ("Cutoff :"+row[3])
        #  print ("DOB :"+row[4])
        #  print ("Community :"+row[5])
        #  print ("Community Rank :"+row[6])
         Com=row[5]
         if 'MBC' in Com :
             Com='MBC'
         c_rank=row[6]
for df in p_csv:
    if(Com== df[4] and str(c_rank) == df[6]):
        expt_m=df[5]
# download raw json object
url = "https://cutoff.tneaonline.org/api/auth/glist/1C"
url_a = "https://facilities.aicte-india.org/dashboard/pages/files/nba.php"
data = urllib.request.urlopen(url).read().decode()
data_a = urllib.request.urlopen(url_a).read().decode()
sor={}
obj_a = json.loads(data_a)


# parse json object
cout=0
cour_data='no course found'
obj = json.loads(data)
for i in range(0,len(obj)):
    if (obj[i]["con"].find(Autonomous) != -1):    
        if(obj[i]["brc"]==dep_cod.upper()):
            if(type(obj[i][Com])==int):
                if(obj[i][Com]>float(expt_m)-12 and obj[i][Com]<float(expt_m)+20):
                    # print(f'\nCollege Name: {obj[i]["con"]} \nCourse: {obj[i]["brn"]} \nCutoff :{obj[i]["MBC"]}\n')
                    sor[i]=obj[i][Com]
                    cour_data=obj[i]["brn"]
                    cout+=1
                # if(j==4):
                #     break
print("Number of collges found : "+str(cout))
print(f'{cour_data.upper()}')
for index, value in sorted(sor.items(), key =lambda kv:(kv[1], kv[0]),reverse=True):
    print(f'\nCode : {obj[index]["coc"]} \nCollege Name: {obj[index]["con"]} \nCourse: {obj[index]["brn"]} \nCutoff :{obj[index]["MBC"]}') #\nCutoff :{obj[index]["MBC"]}
    dta=obj[index]["con"].split(",", 1)[0].split("(Autonomous)", 1)[0]
    fil_dta=dta.upper().strip()
    for i in range(0,len(obj_a["institutedetails"])): 
        if (obj_a["institutedetails"][i]["CURRENT_INSTITUTE_NAME"].find(fil_dta) != -1):  
            if(obj_a["institutedetails"][i]["COURSE"].find("INFORMATION") != -1):
                print(f'Inst_type :{obj_a["institutedetails"][i]["INST_TYPE"]}')
                print(f'Affiliating_to :{obj_a["institutedetails"][i]["AFFILIATING_UNIVERSITY"]}')
                print(f'Level_of_course :{obj_a["institutedetails"][i]["LEVEL_OF_COURSE"]}')
                print(f'Accreditation_type :{obj_a["institutedetails"][i]["ACCREDITATION_TYPE"]}  {obj_a["institutedetails"][i]["ACCREDITATION_STATUS"]}')
                print(f'Accreditation_till :{obj_a["institutedetails"][i]["ACCREDITATION_TILL"]}')
                print(f'Seats :{obj_a["institutedetails"][i]["APPROVED_INTAKE"]}')
    for j in search(dta, tld="co.in", num=1, stop=1, pause=2):
            print(f'Website :{j}')
    # for j_1 in search(dta+"Placement", tld="co.in", num=10, stop=10, pause=2):
    #     if(j_1.find(j) != -1 and j_1.find("placement") != -1):
    #         print(f'Placements :{j_1}')
    # for j in search(dta+"quora", tld="co.in", num=5, stop=5, pause=2):
    #         print(f'Review :{j}')
print(f'\n************************************************************************************')




    # Url=f'https://www.google.com/search?q={obj[index]["con"].replace(" ", "%20")}'
    # page = requests.get(Url)
    # soup = BeautifulSoup(page.content,"html.parser")
    # links = soup.findAll("a")
    # coutsearch=0
    # for link in soup.find_all("a",href=re.compile("(?<=/url\?q=)(https.*://.*)")):
    #     content=re.split(":(?=http)",link["href"].replace("/url?q=",""))
    #     if(coutsearch == 0 and content[0].find(".in") != -1):
    #          print("website :"+content[0].split("&", 1)[0])
    #          coutsearch+=1









# mc = mechanize.Browser()
# mc.set_handle_robots(False)

# url = 'https://www.knowyourcollege-gov.in/'
# mc.open(url)

# mc.select_form(name='searchForm1')
# mc['keyword'] = 'SNS' # Enter a mobile number
# res = mc.submit().read()
# soup = BeautifulSoup(res,'html.parser')
# tbl = soup.find_all(id ='tech')
# # print(tbl)
# data_1 = tbl[0].find('a', {'id':"instituteLinks"})['href']
# print(data_1)

    #  for j in search(obj[index]["con"], tld="co.in", num=1, stop=1, pause=1):
    #    print("Website :"+j)
    #  for j in search(obj[index]["con"], tld="co.in", num=1, stop=6 , pause=1):
    #     if(j.find("www.shiksha.com") != -1): 
    #         print("Website :"+j)
    #     if(j.find("collegedunia.com") != -1):
    #         print("Website :"+j)



# parse json object

