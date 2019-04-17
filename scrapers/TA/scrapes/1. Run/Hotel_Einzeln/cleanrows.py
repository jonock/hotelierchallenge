#this script will go through the hotel_price files and delete unnecessary RainbowClubSA

import pandas as pd
import os
from glob import glob

for entry in glob('*.csv'):
    with open(entry, 'r') as f:
        prices = pd.read_csv (entry)

#To delete columns axis = 1
        prices.drop('platform_name', axis=1, inplace=True)
#delete rows (axis = 0)
        prices.drop(prices.index[1:],axis = 0, inplace=True)


        prices.to_csv(entry)

print("Done")
