import pandas as pd
import numpy as np

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
print football.head()
print "tail()"
print football.tail()
print "football['wins'].map(lambda x: x >= 1)"
print football[football['losses'] > 5]['wins'].map(lambda x: x >= 1)
print "np.mean(football[football['losses'] > 5]['wins'])"
print np.mean(football[football['losses'] > 5]['wins'])
print "football[football['losses'] > 5]['wins'].apply(np.mean)"
print football[football['losses'] > 5]['wins'].apply(np.mean)