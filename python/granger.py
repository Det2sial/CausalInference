#!python
import pandas as pd
import statsmodels.tsa.stattools as st
import numpy as np


crime_data = pd.read_csv('crime_rates.csv')

abortion_data = pd.read_csv('../datasets/abortion_by_year.csv')


x2 = np.array(abortion_data.iloc[1:-1,-1])
x1 = np.array(crime_data.loc[5])


x1 = np.delete(x1,[0,1,2])
for i in range(len(x1)):
    x1[i] = x1[i].replace(',','')
    
x1 = x1.astype(np.float)
x2 = x2.astype(np.float)


x = np.array([x1,x2])
x = np.transpose(x)

res1 = st.grangercausalitytests(x,maxlag = 10,verbose = False)

for key,value in res1.items():
    print(value[0])
    exit()


exit()
    

x = np.array([x2,x1])
x = np.transpose(x)

res2  = st.grangercausalitytests(x,maxlag = 10,verbose = False)



# RESULTS
