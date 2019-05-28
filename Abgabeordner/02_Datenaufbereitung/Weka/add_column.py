#this script will go through the hotel lists and add a column for class

import pandas as pd
import os
import xlsxwriter
import numpy as np
from glob import glob

n = 0

for entry in glob('WEKA Hotels/*.csv'):
    with open(entry, 'r') as f:
        prices = pd.read_csv (entry)
        n = n + 1
        hotel_id = str(n)
        prices['Hotel_ID'] = hotel_id
        prices.to_csv(entry, header=True, index=False, encoding='utf-8-sig')
        print (str(entry) + " New column added")

print("BATCH DONE - WOOT WOOT PARTEEEEY")
