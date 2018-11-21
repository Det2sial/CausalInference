# For stationary examination

from pandas import Series
from matplotlib import pyplot

series1 = Series.from_csv('abortion_NYS.csv',header=0)
series2 = Series.from_csv('abortion_NYC.csv',header=0)
series1.plot()
series2.plot()
pyplot.xlabel("Year")
pyplot.ylabel("Reported Abortion Number")
pyplot.show()
