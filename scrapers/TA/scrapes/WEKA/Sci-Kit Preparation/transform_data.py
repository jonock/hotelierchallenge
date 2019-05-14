#this script will go through the hotel_price files and create one file with all data

import pandas as pd
from glob import glob

#store data in pandas DataFrame
#all_data = pd.DataFrame()
#open every file in specified folder

#for entry in glob('data/*.xlsx'):
#    with open(entry, 'r') as f:
#        df = pd.read_excel(entry, sheet_name='Tabelle2')
#
#        df.to_csv(entry + '.csv', header=True, index=False)
#
#print('Dates appended - CSV saved')


#with open('data/Abu-Dhabi Sci Kit Preparation.csv', 'r'):
#    df = pd.read_csv('data/Abu-Dhabi Sci Kit Preparation.csv')
#
#    for i in range(8):
#        df = df.append(df)
#
#
#    df.to_csv('data/test1.csv', header=False, index=True)
n = 1
#with open('data/Abu-Dhabi Sci Kit Preparation.csv') as f:
#    df = pd.read_csv(f)
#    print(df.head())
#    for i in range(386):
#        n = n + 1
#        first_value = df.iloc[]
#        df.drop('1', axis=1, inplace=True)
#        print(df.head())

n = 0
p = 1
with open('data/Test1.csv') as f:
    df = pd.read_csv(f)
    #print(df.head())
    #first_value = df.iloc[1:2,1:2]
    #print("First Value: ", first_value)
    for line in df:
        n = n + 1
        p = p + 1
        x = df.iloc[n:p,n:p]
        print (x)
    #print(df.head())
