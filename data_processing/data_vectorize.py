# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:16:41 2019

@author: User
"""


import pandas as pd
from contractions import CONTRACTION_MAP
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import os
import ast
from nltk.stem import PorterStemmer
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.corpus import stopwords
import json

ps = PorterStemmer()

ad_data_directory='C:\\Users\\User\\Desktop\\ads_data\\ad_data'
vectorizer = TfidfVectorizer()
data=pd.read_csv('C:\\Users\\User\\Downloads\\combined_data.csv').values

website_contents=[]
for direc in os.listdir(ad_data_directory):
    if direc in data[:,0]:
        if os.path.isfile(os.path.join(ad_data_directory,direc,"adwebsite.txt")):
            with open(os.path.join(ad_data_directory,direc,"adwebsite.txt")) as file:  
                website_text = file.read() 
            words=' '.join(website_text.split('/n')[1:]).split(' ')
            words=[word for word in words if word.isalpha()]
            words=[ps.stem(word) for word in words]
            words=[word for word in words if not word in set(stopwords.words('english'))]
            contents=' '.join(words)
            website_contents.append(contents)
        else:
            website_contents.append('')

X = vectorizer.fit_transform(website_contents)
np.save('website_contents.npy',X.todense())
print(X.todense().shape)

json1 = json.dumps(list(vectorizer.vocabulary_.keys()))
f = open("website_contents_dict.json","w")
f.write(json1)
f.close()


corpus=[]
for line in data[:,1]:
    if not pd.isna(line):
        words=line.split(' ')
        words=[word for word in words if word.isalpha()]
        words=[ps.stem(word) for word in words]
        words=[word for word in words if not word in set(stopwords.words('english'))]
        contents=' '.join(words)
        corpus.append(contents)
    else:
        corpus.append('')

X = vectorizer.fit_transform(corpus)
np.save('speech_to_text.npy',X.todense())

print(X.todense().shape)

json1 = json.dumps(list(vectorizer.vocabulary_.keys()))
f = open("speech_to_text_dict.json","w")
f.write(json1)
f.close()

corpus=[]
for line in data[:,2]:
    if line!='[]':
        words=ast.literal_eval(line)
        words=[word for word in words if word.isalpha()]
        words=[ps.stem(word) for word in words]
        words=[word for word in words if not word in set(stopwords.words('english'))]
        contents=' '.join(words)
        corpus.append(contents)
    else:
        corpus.append('')

X = vectorizer.fit_transform(corpus)
np.save('video_intel.npy',X.todense())
print(X.todense().shape)

json1 = json.dumps(list(vectorizer.vocabulary_.keys()))
f = open("video_intel_dict.json","w")
f.write(json1)
f.close()


#data=pd.read_csv('raw_label.csv')
#original_ids=list(pd.read_csv('C:/Users/User/Downloads/combined_data.csv')['id'].values)
#labels=np.zeros(data.shape[0])
#for k in range(data.shape[0]):
#    labels[k]=np.log((data['After'][k]+1)/(data['Before'][k]+1))
#    
#change=np.zeros(data.shape[0])
#for k in range(data.shape[0]):
#    change[k]=data['After'][k]-data['Before'][k]
#np.save('targets.npy',labels)
#import matplotlib.pyplot as plt
#plt.hist(labels,bins=100)
#plt.title('Histogram of Targets')
#plt.xlabel('Relative Change')
#plt.ylabel('Frequency')
#
#
#df=pd.read_csv('C:/Users/User/Downloads/combined_data.csv')
#df['Company']=data['Advertiser'].values
#df['Before']=data['Before'].values
#df['After']=data['After'].values
#df['Target']=list(labels)
#
#df.to_csv('final_data.csv',index=False)





















