#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pylab as plt


# In[2]:


csv_path = "/Users/danishmir/desktop/courseera/FiveYear.csv"


# In[3]:


df=pd.read_csv(csv_path)


# In[4]:


df.head(5)


# In[5]:


df.columns


# In[6]:


df.describe(include="all")# include all helps to the data including irregularities like NaN


# In[7]:


missing_data=df.isnull()#returns True if null is present
missing_data.head(10)


# In[9]:


for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")


# In[10]:


import numpy as np
df.drop(["Unnamed: 0"], axis = 1, inplace = True) # dropping redundunt s.no 


# In[46]:


df.dropna(subset=["CASE_SUBMITTED"], axis = 0, inplace = True) # dropping 1 Na in the Case_Submitted column


# In[21]:


import statistics as st
Mode_EMPLOYER_NAME_loss = st.mode(df["EMPLOYER_NAME"])# get mode for 123 missing values
print("the mode of employer name is " + Mode_EMPLOYER_NAME_loss)


# In[22]:


df["EMPLOYER_NAME"].replace(np.nan, Mode_EMPLOYER_NAME_loss, inplace=True)#replace the NAN with mode


# In[23]:


Mode_EMPLOYER_ADDRESS_loss = st.mode(df["EMPLOYER_ADDRESS"])# get mode for 52 na
print("the mode of employer address is " + Mode_EMPLOYER_ADDRESS_loss)
df["EMPLOYER_ADDRESS"].replace(np.nan, Mode_EMPLOYER_ADDRESS_loss, inplace=True)#replace the NAN with mode


# In[48]:


Mode_EMPLOYER_CITY_loss = st.mode(df["EMPLOYER_CITY"])# get mode 
print("the mode of employer city is " + Mode_EMPLOYER_CITY_loss)
df["EMPLOYER_CITY"].replace(np.nan, Mode_EMPLOYER_CITY_loss, inplace=True)#replace the NAN with mode


# In[50]:


#df.drop(["EMPLOYER_PHONE"], axis=1, inplace=True) # too many Nan and not important for analysis
#df.drop(["EMPLOYER_PHONE_EXT"], axis=1, inplace=True)


# In[52]:


Mode_EMPLOYER_POSTAL_CODE_loss = st.mode(df["EMPLOYER_POSTAL_CODE"])# get mode 
print("the mode of employer postal code is " + Mode_EMPLOYER_POSTAL_CODE_loss)
df["EMPLOYER_POSTAL_CODE"].replace(np.nan, Mode_EMPLOYER_POSTAL_CODE_loss, inplace=True)#replace the NAN with mode


# In[53]:


df.drop(["EMPLOYER_PROVINCE"], axis=1, inplace=True)# Drop as this column has large NAs and is of not much use in analysis

