#this script will go through the hotel_price files and create one file with all data

import pandas as pd
from glob import glob


filename = "data/next/Male_Versuch_1.csv"

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
    df.to_csv('data//next/Male_Versuch_2.csv', header=True, index=False, encoding='utf-8-sig')
    #print(df.head())
print("New File created")
