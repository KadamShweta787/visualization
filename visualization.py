#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns


# In[2]:


#read data from datasets
df = pd.read_csv('IRIS.csv')


# In[3]:


df


# In[4]:


#visualize this count
sns.countplot(df['species'], label="Count")


# In[5]:


#select numeric variables
numeric_vars = ['sepal_width', 'petal_width']
#create histogram for each numeric variable
fig = plt.figure(figsize=(25,15))
for i in range(len(numeric_vars)):
    var=numeric_vars[i]
    sub=fig.add_subplot(2,5,i+1)
    sub.set_xlabel(var)
    df[var].plot(kind='hist')


# In[11]:


plt.title("Scatter Plot")


# In[13]:


# Setting the X and Y labels
plt.xlabel('sepal_width')
plt.ylabel('petal_width')


# In[19]:


plt.scatter(df['sepal_width'], df['petal_width'])


# In[ ]:




