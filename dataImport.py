## Dataset processing: Merge by year

import pandas as pd

inPath = r'E:\code\python\causalInference\abortion.csv'
outPath = 'E:\code\python\causalInference\dataset.csv'

inf = pd.read_csv(inPath, delimiter = ',')

year = inf.iloc[:,0]
abortion = inf.iloc[:,-1]


header = ["year","abortion","crime","Dow_Jones","Incarceration", "Police_Employment"]

df = pd.DataFrame(columns = header)
df.loc[:,"year"]=year
df.loc[:,"abortion"]=abortion
df.to_csv(outPath)



