# For stationary examination

import pandas as pd
from matplotlib import pyplot


## ---------------------------------------------
# ADF (Augmented Dickey Fuller) Test
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
    return None



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
    return None

## ---------------------------------------------
# Stationary process
# De-trend by differencing
def detrend(timeseries):
    X = timeseries
    diff = list()
    for i in range(1, len(X)):
        value = X[i] - X[i - 1]
        diff.append(value)
    return diff

## ---------------------------------------------
# font settings
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }



## ---------------------------------------------
# MAIN FUNCTION
def main():
    data = pd.read_csv("regression.csv", names=['year','abortion','dowjones','incarceration','crime_rate'])
    df = pd.DataFrame(data)

    ## abortion
    # Plot
    pyplot.plot(df['year'],df['abortion'],'r')
    pyplot.title('Abortion(Before)', fontdict=font)
    pyplot.xlabel('Year',fontdict=font)
    pyplot.ylabel('Reported Rates',fontdict=font)
    pyplot.grid(True)
    pyplot.show()
    # adf_test()
    adf_test(df['abortion'])
    # kpss_test()
    kpss_test(df['abortion'])
    # detrend by differencing
    abortion_diff = detrend(df['abortion'])
    pyplot.plot(abortion_diff,'--r')
    pyplot.title('Abortion(After)', fontdict=font)
    pyplot.xlabel('Year',fontdict=font)
    pyplot.ylabel('',fontdict=font)
    pyplot.grid(True)
    pyplot.show()
    print("-----------------------")
    # adf_test()
    adf_test(abortion_diff)
    # kpss_test()
    kpss_test(abortion_diff)
    # exit()

    # dowjones
    pyplot.plot(df['year'],df['dowjones'],'y')
    pyplot.title('Dow Jones Industrial Average(Before)', fontdict=font)
    pyplot.xlabel('Year',fontdict=font)
    pyplot.ylabel('Index Average',fontdict=font)
    pyplot.grid(True)
    pyplot.show()
    # adf_test()
    adf_test(df['dowjones'])
    # kpss_test()
    kpss_test(df['dowjones'])
    # detrend by differencing
    dowjones_diff = detrend(df['dowjones'])
    pyplot.plot(dowjones_diff,'--y')
    pyplot.title('Dow Jones Industrial Average(After)', fontdict=font)
    pyplot.xlabel('Year',fontdict=font)
    pyplot.ylabel('',fontdict=font)
    pyplot.grid(True)
    pyplot.show()
    print("-----------------------")
    # adf_test()
    adf_test(dowjones_diff)
    # kpss_test()
    kpss_test(dowjones_diff)
    # exit()

    # incarceration
    pyplot.plot(df['year'],df['incarceration'],'b')
    pyplot.title('Incarceration(Before)', fontdict=font)
    pyplot.xlabel('Year',fontdict=font)
    pyplot.ylabel('',fontdict=font)
    pyplot.grid(True)
    pyplot.show()
    # adf_test()
    adf_test(df['incarceration'])
    # kpss_test()
    kpss_test(df['incarceration'])
    # detrend by differencing
    incar_diff = detrend(df['incarceration'])
    pyplot.plot(incar_diff,'--b')
    pyplot.title('incarceration(After)', fontdict=font)
    pyplot.xlabel('Year',fontdict=font)
    pyplot.ylabel('',fontdict=font)
    pyplot.grid(True)
    pyplot.show()
    print("-----------------------")
    # adf_test()
    adf_test(incar_diff)
    # kpss_test()
    kpss_test(incar_diff)
    # exit()

    # crime rate
    pyplot.plot(df['year'],df['crime_rate'],'g')
    pyplot.title('Crime Rate(Before)', fontdict=font)
    pyplot.xlabel('Year',fontdict=font)
    pyplot.ylabel('',fontdict=font)
    pyplot.grid(True)
    pyplot.show()
    # adf_test()
    adf_test(df['crime_rate'])
    # kpss_test()
    kpss_test(df['crime_rate'])
    # detrend by differencing
    crime_diff = detrend(df['crime_rate'])
    pyplot.plot(crime_diff,'--g')
    pyplot.title('Crime Rate(After)', fontdict=font)
    pyplot.xlabel('Year',fontdict=font)
    pyplot.ylabel('',fontdict=font)
    pyplot.grid(True)
    pyplot.show()
    print("-----------------------")
    # adf_test()
    adf_test(crime_diff)
    # kpss_test()
    kpss_test(crime_diff)
    # exit()

    # write csv
    sdata = {'abortion':abortion_diff,'dowjones':dowjones_diff,'incarceration':incar_diff,'crime_rate':crime_diff}
    sf = pd.DataFrame(sdata)
    sf.to_csv("stationary.csv")

main()

# print(df["year"])


exit()

# TODO: log transformation -before parametric statistical test

