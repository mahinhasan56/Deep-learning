import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6
data = pd.read_csv('C:/Users/User/Desktop/AirPassengers.csv')

print data.head()
print '\n Data Types:'
print data.dtypes
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
data = pd.read_csv('C:/Users/User/Desktop/AirPassengers.csv', parse_dates=['Month'], index_col='Month',date_parser=dateparse)
print data.head()