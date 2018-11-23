# For stationary examination

import pandas as pd
from pandas import Series
from matplotlib import pyplot

# plot and see trend
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

series = Series.from_csv('abortion_NYC.csv',header=0)
series.plot()
pyplot.title('Abortion', fontdict=font)
pyplot.xlabel('Year',fontdict=font)
pyplot.ylabel('Reported Rates',fontdict=font)
pyplot.grid(True)
pyplot.show()

# log transformation -before parametric statistical test
# not now

# ADF (Augmented Dickey Fuller) Test

#define function for ADF test
from statsmodels.tsa.stattools import adfuller
def adf_test(timeseries):
    #Perform Dickey-Fuller test:
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
       dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)

adf_test(series)








# KPSS (Kwiatkowski-Phillips-Schmidt-Shin) Test

from statsmodels.tsa.stattools import kpss
#define KPSS
def kpss_test(timeseries):
    print ('Results of KPSS Test:')
    kpsstest = kpss(timeseries, regression='c')
    kpss_output = pd.Series(kpsstest[0:3], index=['Test Statistic','p-value','Lags Used'])
    for key,value in kpsstest[3].items():
        kpss_output['Critical Value (%s)'%key] = value
    print (kpss_output)


kpss_test(series)
