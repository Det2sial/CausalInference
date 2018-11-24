# For stationary examination

import pandas as pd
from pandas import Series
from matplotlib import pyplot


## ---------------------------------------------
# plot and see trend
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

# TODO: read csv file and make a table
# series = Series.from_csv('regression.csv',header=0)
# print(series)
# exit()
# series.plot()
# pyplot.title('Abortion', fontdict=font)
# pyplot.xlabel('Year',fontdict=font)
# pyplot.ylabel('Reported Rates',fontdict=font)
# pyplot.grid(True)
# pyplot.show()

def main():
    data = pd.read_csv("regression.csv", names=['year','abortion','dowjones','incarceration','crime_rate'])
    df = pd.DataFrame(data)

    ## abortion
    # Plot
    pyplot.plot(df['year'],df['abortion'],'r')
    pyplot.title('Abortion', fontdict=font)
    pyplot.xlabel('Year',fontdict=font)
    pyplot.ylabel('Reported Rates',fontdict=font)
    pyplot.grid(True)
    pyplot.show()
    # adf_test()
    adf_test(df['abortion'])
    # kpss_test()
    kpss_test(df['abortion'])


    ## dowjones
    pyplot.plot(df['year'],df['dowjones'],'y')
    pyplot.title('Dow Jones Industrial Average', fontdict=font)
    pyplot.xlabel('Year',fontdict=font)
    pyplot.ylabel('Index Average',fontdict=font)
    pyplot.grid(True)
    pyplot.show()
    # adf_test()
    adf_test(df['dowjones'])
    # kpss_test()
    kpss_test(df['dowjones'])


    # incarceration
    pyplot.plot(df['year'],df['incarceration'],'b')
    pyplot.title('Incarceration', fontdict=font)
    pyplot.xlabel('Year',fontdict=font)
    pyplot.ylabel('',fontdict=font)
    pyplot.grid(True)
    pyplot.show()
    # adf_test()
    adf_test(df['incarceration'])
    # kpss_test()
    kpss_test(df['incarceration'])


main()

# print(df["year"])


exit()

# TODO: log transformation -before parametric statistical test

# ADF (Augmented Dickey Fuller) Test

## ---------------------------------------------
# define function for ADF test
from statsmodels.tsa.stattools import adfuller
def adf_test(timeseries):
    #Perform Dickey-Fuller test:
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
       dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)



## ---------------------------------------------
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


## ---------------------------------------------
# Stationary process
# Trend differencing

