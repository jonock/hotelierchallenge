#this script will help calculate the mean of the region to make it comparable to the hotel_prices

import pandas as pd
import numpy as np
import os
from glob import glob

#open xlsx and replace wrong string characters to be able to calculate mean later.
for entry in glob('Hotel_Region/*.xlsx'):
    with open(entry, 'r') as f:
        df = pd.read_excel(entry, index_col=None)

        #drop not needed columns
        try:
            df.drop('hotel_name', axis=1, inplace=True)
            df['price_per_night'] = df['price_per_night'].str.replace(',','')
        except:
            next
        df.to_csv(entry + "_new.csv", header=True, index=False, encoding='utf-8-sig' )
        print ("csv ready")

#
for entry in glob('Hotel_Region/*.csv'):
    with open(entry, 'r') as f:
        region_prices = pd.read_csv (entry)
        #save locality and date in variables to write to xlsx later
        locality = region_prices.values[1,0]
        date = region_prices.values[0,2]
        date = region_prices.loc[region_prices.Datum, 'Datum'].values[0]

        #convert strings to numeric values for further calculations
        region_prices = region_prices.apply(pd.to_numeric, errors='coerce').combine_first(region_prices)
        avg = region_prices.loc[:, "price_per_night"].mean()

        output = pd.DataFrame([[locality, avg, date]],
                                columns = ['Locality', 'AVG_Price', 'Date'])
        output.to_excel(entry + "_average.xlsx")

        print ("Excel Created")

#store data in pandas DataFrame
all_data = pd.DataFrame()

#open every file in specified folder
for entry in glob('Hotel_Region/*average.xlsx'):
    with open(entry, 'r') as f:
        df = pd.read_excel(entry)
        all_data = all_data.append(df, ignore_index=True)
        print("price appended")
        #write appended data to excel
        all_data.to_excel('Region_Teplice_Prices_appended.xlsx')

print('Dates appended - Excel saved')

print ("Done")
