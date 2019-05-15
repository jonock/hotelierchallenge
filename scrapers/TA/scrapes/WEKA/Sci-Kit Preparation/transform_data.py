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

filename = "data/Abu-Dhabi Sci Kit Preparation.csv"
filetest = "data/Test1.csv"
n = 0
p = 0
with open(filename) as f:
    df = pd.read_csv(f)
    #print(df.head())
    #first_value = df.iloc[1:2,1:2]
    #print("First Value: ", first_value)
    for line in df:
        n = n + 1
        p = p + 1
        #x = df.iloc[:1,-2:]
        #df.at[n:,-p:] = ''    #from 2nd row and last column on
        df.at[n:,:p] = ''      #from 2nd row and first column on
        #print (df.head())
    df.to_csv('data/Versuch_4.csv', header=True, index=False, encoding='utf-8-sig')
    #print(df.head())
print("New File created")
