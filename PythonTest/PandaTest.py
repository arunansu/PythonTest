import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#df = pd.read_csv(filename)
symbol = "IBM" # or AAPL
#df = pd.read_csv("data/{}.csv".format(symbol)) #File is located in data/<symbol>.csv
#nd = df.values #gives ndarray panda wraps numpy ndarray as dataframe
#nd[r, c] #access element at r row and c column
#nd[1:3, 2:4] #acces sub matrix with row index 1 to 2 and column index 2 to 3
#nd[:,3] #all rows of column index 3
#nd[-1,1:3] #last row with column index 1 to 2
#print df['close'].max() #print maximum of column titled close
#print df['volume'].mean() #print mean of column titled volume
#print df[10:21] #print rows 10 to 20
#df['Adj Close'].plot() #Plot Adj Close column
#ax = df[['Adj Close', 'Close']].plot(title="Adj Close Plot", fontsize=2) #Plot Adj Close and Close columns
#ax.set_xlabel("Date")
#ax.set_ylabel("Price")
#plt.show()
start_date = '2010-01-22'
end_date = '2010-01-26'
dates = pd.date_range(start_date, end_date)
df1 = pd.DataFrame(index=dates)
#print df1._ix['2010-01-01':'2010-01-31'] #Slice by row index dates for month of January 
#print df1._ix['2010-01-01':'2010-01-31', ['AAPL', 'IBM']] #Slice by row index dates for month of January with only AAPL and IBM columns
#df = pd.read_csv("data/SPY.csv", index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'], 
#                    na_values=['nan']) #Use date column parsed as date as index and select only Date and Adj Close columns
#df = df.dropna()
#df = df.rename(columns={'Adj Close': 'SPY'})
#df1 = df1.join(df) #left join by default, all rows in df1 are retained and only the rows in df that match are added and rest are set to Nan
#df1 = df1.join(df1, how='inner') #select rows in both dataframes
#df1 = df1/df1.ix[0,:] #Normalize by first column
#rmSPY = pd.rolling_mean(df1['SPY'], window = 20)
#df[1:] #all rows of df starting 1
#df[:-1] #all rows of df from 0 to last but 1
#daily_returns = df.copy()
#daily_returns[1:] = (daily_returns[1:]/daily_returns[:-1].values) - 1
#daily_returns = daily_returns / daily_returns.shift(1) - 1 #same as above
#daily_returns.ix[0, :] = 0
#df.corr(method='pearson') #correlation between features
series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
print series

series = pd.Series(['Dave', 'Cheng-Han', 359, 9001], index=['Instructor', 'Curriculum Manager', 'Course Number', 'Power Level'])
print series
print series['Instructor']
print series[['Instructor', 'Curriculum Manager', 'Course Number']]

cuteness = pd.Series([1,2,3,4,5], index = ['Cockroach', 'Fish', 'Mini Pig', 'Puppy', 'Kitten'])
print cuteness > 3
print cuteness[cuteness > 3]

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4], 
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data)
print football
print "dtypes"
print football.dtypes
print "describe()"
print football.describe()
print "head()"
print football.head() #first 5 rows
print "tail()"
print football.tail() #last 5 rows
print "football['wins'].map(lambda x: x >= 1)"
print football[football['losses'] > 5]['wins'].map(lambda x: x >= 1)
print "np.mean(football[football['losses'] > 5]['wins'])"
print np.mean(football[football['losses'] > 5]['wins'])
print "football[football['losses'] > 5]['wins'].apply(np.mean)"
print football[football['losses'] > 5]['wins'].apply(np.mean)