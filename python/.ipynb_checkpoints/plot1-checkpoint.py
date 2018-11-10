
# coding: utf-8

# In[20]:


import matplotlib.pyplot as plt
import csv
import pandas as pd
df = pd.read_csv('/Users/aubhikmazumdar/Desktop/Fall_2018/CAUSAL/CausalInference/datasets/overall/nyc_crime_data.csv')


# In[21]:


plotdf = df.drop(columns = 'Population')
plotdf.plot(x='Year')

