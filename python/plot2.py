
# coding: utf-8

# In[21]:


import matplotlib.pyplot as plt
import csv
import pandas as pd
df = pd.read_csv('/Users/aubhikmazumdar/Desktop/Fall_2018/CAUSAL/CausalInference/datasets/overall/nyc_crime_data.csv')


# In[81]:


plotdf = df.drop(columns = 'Population')
plotdf.plot(x='Year',figsize=(8,8))


# In[82]:


diffdf = df.drop(columns = 'Year')
diffdf = diffdf.diff()
print(diffdf.head())


# In[83]:


diffdf['Year'] = pd.Series(df['Year'])
print(diffdf.head())
diffdf = diffdf.drop(['Population','Index','Property'],axis = 1)


# In[84]:


print(diffdf.head())
diffdf.plot(x='Year',figsize=(10,8))

