# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:14:30 2019

@author: User
"""
ad_data_directory='C:\\Users\\User\\Desktop\\ads_data\\ad_data'

import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException
#from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

company_dict={}
errs=[]

chrome_options=Options()
#chrome_options.headless=True
chrome_options.add_argument('--mute-audio')
caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'ALL'}

driver=webdriver.Chrome(executable_path="D:\\2018-2019\\CS525 Informational Retrieval and Social Media\\Project\\chromedriver.exe",options=chrome_options,desired_capabilities=caps)

#yt-simple-endpoint style-scope yt-formatted-string

for direc in os.listdir(ad_data_directory):
    try:
        with open(os.path.join(ad_data_directory,direc,"adwebsite.txt")) as file:  
            data = file.read() 
        url=data.split('\n')[0]
        domain=url.split("//")[-1].split("/")[0]
        if domain.startswith('www'):
            company=domain.split('.')[1]
        else:
            company=' '.join(domain.split('.')[:-1])
        if company=='youtube':
            driver.get(url)
            time.sleep(2)
            html=driver.page_source
            temp=html[html.find('\"author\":\"')+10:]
            company=temp[:temp.find('"')]
            if company==' html><html xmlns=':
                soup=BeautifulSoup(html)
                el=str(soup.find('h1',id="title"))
                el=el[:-el[::-1].find('<>a/<')-5]
                company=el[-el[::-1].find('>'):]
                print(company)
                errs.append(url)
        company_dict[direc]=company
    except FileNotFoundError:
        shutil.rmtree(os.path.join(ad_data_directory,direc))
driver.quit()

json = json.dumps(company_dict)
f = open("company_dict.json","w")
f.write(json)
f.close()



