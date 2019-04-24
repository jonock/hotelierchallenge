#this script will help calculate the mean of the region to make it comparable to the hotel_prices

import pandas as pd
import numpy as np
import os
from glob import glob

for entry in glob('Test/*.csv'):
    with open(entry, 'r') as f:
        region_prices = pd.read_csv (entry)

        #save locality and date in variables to write to xlsx later
        locality = region_prices.values[1,0]
        date = region_prices.values[0,1]


        #convert strings to numeric values for further calculations
        region_prices = region_prices.apply(pd.to_numeric, errors='coerce').combine_first(region_prices)
        avg = region_prices.loc[:, "price_per_night"].mean()

        output = pd.DataFrame([[locality, avg, date]],
                                columns = ['Locality', 'AVG_Price', 'Date'])
        output.to_excel(entry + "_average.xlsx")

        print ("Excel Created")
