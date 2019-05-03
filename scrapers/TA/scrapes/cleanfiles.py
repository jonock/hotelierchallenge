#this script will go through the hotel_price files and delete unnecessary cells

import pandas as pd
import os
import xlsxwriter
from glob import glob

for entry in glob('Test/Kontrolle/folder/*.csv'):
    with open(entry, 'r') as f:
        prices = pd.read_csv (entry)

#To delete columns axis = 1
        try:
            #prices.drop('platform_name', axis=1, inplace=True)
#delete rows (axis = 0)
        prices.drop(prices.index[1:],axis = 0, inplace=True)
            #prices.replace(",", ".", inplace=True)
        except:
            next
#writing the same csv with cleaned and encoded data
        prices.to_csv(entry, header=True, index=False, encoding='utf-8-sig')
        print ("Data cleaned - CSV saved")

print("BATCH DONE - WOOT WOOT PARTEEEEY")
