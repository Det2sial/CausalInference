#!python
import pandas as pd
import scipy.stats as scs

#Read the dataset
table = pd.read_csv('../datasets/age-wise-crimes.csv')

# Remove unneccesary columns
cols = [c for c in table.columns if c.lower()[:7] != 'unnamed']
new_table = table[cols]


# Drop the first row which is now redundant
table = new_table.drop([0])
print(table)

# Change the index so that we can choose rows by their names (eg. 18)
table.set_index("Age",inplace = True)
# print(table.loc['18','1985'])

# Start difference-in-difference approach
print(table[['1987','1988','1989']])
# For each year 'x', we need to subtract the rate of age1 wi

table.to_csv('crime_rates.csv',encoding = 'utf-8')
