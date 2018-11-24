#!python
import pandas as pd
import statsmodels.tsa.stattools as st
import numpy as np


crime_data = pd.read_csv('crime_rates.csv')

abortion_data = pd.read_csv('../datasets/abortion_by_year.csv')

# Abortion rates per year
x2 = np.array(abortion_data.iloc[1:-1,-1])

# Crime rates per year
x1 = np.array(crime_data.loc[5])


x1 = np.delete(x1,[0,1,2])
for i in range(len(x1)):
    x1[i] = x1[i].replace(',','')
    
x1 = x1.astype(np.float)
x2 = x2.astype(np.float)


x = np.array([x1,x2])
x = np.transpose(x)

res1 = st.grangercausalitytests(x,maxlag = 10,verbose = True)
    
exit()
x = np.array([x2,x1])
x = np.transpose(x)

res2  = st.grangercausalitytests(x,maxlag = 10,verbose = True)

#x1 = np.transpose(x1)
adf_test1 = st.adfuller(x2)
adf_test2 = st.adfuller(x1)

#documentation of the final F-test and t-test..we can also talk about tackling the unit-root hypothesis





# RESULTS
# The null hypothesis cannot be rejected but this does not mean that the null hypothesis is correct. We still have to do a multiple-hypothesis testing
