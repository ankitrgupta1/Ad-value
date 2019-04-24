# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:59:34 2019

@author: User
"""

ad_data_directory='C:\\Users\\User\\Desktop\\ads_data\\ad_data'
company_dict_path='C:\\Users\\User\\Desktop\\company_dict.json'
ad_dates_path='C:\\Users\\User\\Desktop\\ad_dates.json'


import os
import json
import pandas as pd

with open(company_dict_path) as json_file:  
    company_dict = json.load(json_file)

with open(ad_dates_path) as json_file:  
    ad_dates = json.load(json_file)


data=[]

for direc in os.listdir(ad_data_directory):
    text_path=os.path.join(ad_data_directory,direc,"text.txt")
    json_path=os.path.join(ad_data_directory,direc,"data.json")
    if os.path.isfile(text_path) and os.path.isfile(json_path) and (direc in company_dict) and (direc in ad_dates):
        with open(text_path) as file:  
            text_contents = file.read()
        with open(json_path) as json_file:  
            json_contents = json.load(json_file)
        json_labels=[]
        for descr in json_contents['labels']:
            json_labels.append(descr['description'])
        
        data.append([direc,text_contents,list(set(json_labels)),company_dict[direc],ad_dates[direc]])

df=pd.DataFrame.from_records(data)
df.to_csv('combined_data.csv',index=False,header =['Speech to Text','Video Intelligence api','Company','Upload date'])






