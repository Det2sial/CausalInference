## Dataset processing: Merge by year

import csv

infilename =  r'E:\code\python\causalInference\abortion.csv'
outfilename = r'E:\code\python\causalInference\dataset.csv'

# values = []
# with open(infilename,'r') as f:
#     for line in f:
#         x = line.strip().split(',')
#         values.append(x[-1])
#
# with open(outfilename,'w',newline = '') as f:
#     writer = csv.writer(f,delimiter = ',')
#
#     for row in values:
#         writer.writerow([row])

year = []
abortion = []
with open(infilename,'r') as f:
    for line in f:
        x = line.strip().split(',')
        year.append(x[0])
        abortion.append(x[-1])


with open(outfilename,'w',newline = '') as f:
    fieldnames = ['year','abortion','criminal','police','incarceration']
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    for row1 in year:
        for row2 in abortion:
            writer.writerow({'year':row1,'abortion':row2})
