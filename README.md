AdValue is a project to predict popularity of the Ads using the feature extracted from the Ads and the website information of the company and products.

## Problem Statement

Creating ads are expensive in money and time. 
Understanding features which lead to popularity could help tremendously

## Datasets

Youtube ad videos,  
Speech-to-Text,  
Labels Detection,   
Twitter data,  
Google Trends,     
Company website,   

## Data collection

We scrapped videos from YouTube to be used as our fundamental dataset.
We extracted the voice from the videos and converted them to text using Google speech-to-text api.
Labels were also detected from the ad videos using the google video intelligence api.
Along with these we also used the company or product information scrapped from theie respective website.
Together these information are used as features in our dataaset which we finally use to predict the popularity of the videos.

We gather and formalize our target value, we collected google trend stats of the respective product and company. We used these values to formalize the increase or decrease of the value around the launch of the ad videos.

## Methodology

We use the folowwing methodology:   

Feature Extraction,   
Feature Selection,  
Model Selection,  
Model Training

## Feture Extraction:   

Sources of information:   

Speech-to-text,   
Video Intelligence,   
Website contents

Feature extraction from text:   

Filter out words that contain any characters not in the alphabet,   
Stop Word Removal,  
Porter Stemmer,   
Convert to tf-idf features  

Features were extracted for 686 data instances. The number of features exceeds the number of instances and the data is sparse.
Variance Threshold feature selection was used to reduce the number of features to 201.

## Models   

Regression Models:  
Lasso Regression (M1),  
K-nearest Neighbors Regression (M2),  
Decision Tree Regression (M3),  
Random Forest Regression (M4)


## Results



## Conclusion   

The information extracted from advertisements allows for the prediction of how the interest in the company will change in time.   
Due to limited volume of data, the models’ predictive capabilities were stumped.  
More nuanced measurements of the viewer engagement would allow for more detailed analysis.

