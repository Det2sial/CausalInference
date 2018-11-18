#!python
import pandas as pd
import numpy as np

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


#        18  19  20  21  22  23
# 1972 | d11 d12 d13 d14 d15 d16 |
# 1974 | d21 d22 d23 d24 d25 d26 |
#


# Creating the difference matrix
diff_matrix = np.ones((2,6))
age1 = 18
age2 = 19
year1 = 1990
year2 = 1991
year3 = 1992
year4 = 1993

for i in range(diff_matrix.shape[1]):
    temp1 = float(table.loc[str(age1),str(year1)].replace(',',''))
    temp2 = float(table.loc[str(age2),str(year2)].replace(',',''))
    diff_matrix[0,i] = abs(temp1 - temp2)

    temp1 = float(table.loc[str(age1),str(year3)].replace(',',''))
    temp2 = float(table.loc[str(age2),str(year4)].replace(',',''))
    diff_matrix[1,i] = abs(temp1 - temp2)

    age1 += 1
    age2 += 1

# After creating the difference matrix,we have to calculate the difference for each column

diff_column = np.ones((1,6))

for i in range(6):
    diff_column[0,i] = (abs(diff_matrix[0,i] - diff_matrix[1,i])) / max(diff_matrix[0,i],diff_matrix[1,i])

print(diff_column)

print(diff_column.mean(axis = 1))
