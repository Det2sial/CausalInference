#!python
import pandas as pd
import numpy as np



def calculate(all_matrices):
    means = []
    s = 0
    for i in range(len(all_matrices)):
        matrix = all_matrices[i]
        diff_column = np.ones((1,matrix.shape[1]))
        for j in range(matrix.shape[1]):
            diff_column[0,j] = (matrix[0,j] - matrix[1,j])
        print(matrix.shape[1])
        print(diff_column)
        print(diff_column.mean())
        means.append(diff_column.mean())
    print(means)
    print(len(means))
    print(sum(means)/len(means))
    # results -
    # 1. very small effect, can't really say that abortion had an effect
    # 2. The effect was actually negative which is a good sign


def main():
    #Read the dataset
    table = pd.read_csv('../datasets/age-wise-crimes.csv')

    # Remove unneccesary columns
    cols = [c for c in table.columns if c.lower()[:7] != 'unnamed']
    new_table = table[cols]


    # Drop the first row which is now redundant
    table = new_table.drop([0])


    # Change the index so that we can choose rows by their names (eg. 18)
    table.set_index("Age",inplace = True)
    # print(table.loc['18','1985'])

    # Start difference-in-difference approach
    print(table.loc[:,'1990':'1998'])
    # For each year 'x', we need to subtract the rate of age1 wi

    table.to_csv('crime_rates.csv',encoding = 'utf-8')


    #        18  19  20  21  22  23
    # 1972 | d11 d12 d13 d14 d15 d16 |
    # 1974 | d21 d22 d23 d24 d25 d26 |
    #


    # Creating the difference matrix
    all_matrices = []
    pre_abortion_year = 1972
    post_abortion_year = 1974

    for year1 in range(1990,1997):
        age1 = year1 - pre_abortion_year
        age2 = age1 + 1
        year2 = year1 + 1
        year3 = year2 + 1
        year4 = year3 + 1
        diff_matrix = np.ones((2,24-age1))

        for i in range(diff_matrix.shape[1]):
            temp1 = float(table.loc[str(age1),str(year1)].replace(',',''))
            temp2 = float(table.loc[str(age2),str(year2)].replace(',',''))
            diff_matrix[0,i] = (temp2 - temp1)/temp1

            temp1 = float(table.loc[str(age1),str(year3)].replace(',',''))
            temp2 = float(table.loc[str(age2),str(year4)].replace(',',''))
            diff_matrix[1,i] = (temp2 - temp1)/temp1

            age1 += 1
            age2 += 1

            if(diff_matrix != []):
                all_matrices.append(diff_matrix)
        print(year1,year2,year3,year4)
        print(diff_matrix)

    calculate(all_matrices)
    return

if __name__ == '__main__':
    main()

