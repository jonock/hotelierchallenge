#this script will go through the hotel lists and add a column for class

import pandas as pd
import os
import xlsxwriter
import numpy as np
from glob import glob


for entry in glob('ControlHotels Mean Control/*.csv'):
    with open(entry, 'r') as f:
        prices = pd.read_csv (entry)
        prices['Mean_Zero'] = pd.to_numeric(prices['Mean_Zero'])
        prices['Mean'] = pd.to_numeric(prices['Mean'])
        prices['Delta'] = prices['Mean_Zero'] - prices['Mean']
        prices.to_csv(entry, header=True, index=False, encoding='utf-8-sig')
        print (str(entry) + "Delta calculated")

print("BATCH DONE - WOOT WOOT PARTEEEEY")
