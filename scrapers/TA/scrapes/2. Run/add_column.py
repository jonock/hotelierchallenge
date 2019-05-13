#this script will go through the hotel lists and add a column for class

import pandas as pd
import os
import xlsxwriter
import numpy as np
from glob import glob


for entry in glob('Weka einzelne Hotels/*.csv'):
    with open(entry, 'r') as f:
        prices = pd.read_csv (entry)
        prices['Influencer_or_Not'] = 'Influencer'
        prices.to_csv(entry, header=True, index=False, encoding='utf-8-sig')
        print (str(entry) + " New column added")

print("BATCH DONE - WOOT WOOT PARTEEEEY")
