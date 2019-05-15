#this script will go through the hotel_price files and create one file with all data

import pandas as pd
from glob import glob



excel_file = 'data/Test6.xlsx'

df = pd.read_excel(excel_file)
#print(df.head())

#print(df[12].head())

row = 1
column = 386

def eliminate(r,c,v):
    '''for row r and column c eliminate value v'''
    #another solution
    #df.loc[r, c] = [x for x in df.loc[r, c] if x != v]
    df.loc[r, c].remove(v)
    return df

print(eliminate(2,5,1))
