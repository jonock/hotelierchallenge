#this script will go through the hotel_price files and delete unnecessary columns

import pandas as pd
import os
import xlsxwriter
from glob import glob

for entry in glob('Hotel_Region/*.csv'):
    with open(entry, 'r') as f:
        prices = pd.read_csv (entry)

#To delete columns axis = 1
        try:
            prices.drop('timestamp', axis=1, inplace=True)
            prices.drop('url', axis=1, inplace=True)
            prices.drop('reviews', axis=1, inplace=True)
            prices.drop('tripadvisor_rating', axis=1, inplace=True)
            prices.drop('checkIn', axis=1, inplace=True)
            prices.drop('checkOut', axis=1, inplace=True)
            prices.drop('booking_provider', axis=1, inplace=True)
            prices.drop('no_of_deals', axis=1, inplace=True)
            prices.drop('hotel_features', axis=1, inplace=True)
#delete rows (axis = 0)
            #prices.drop(prices.index[1:],axis = 0, inplace=True)
            #prices.replace(",", ".", inplace=True)
        except:
            next
#writing the same csv with cleaned and encoded data
        prices.to_csv(entry, header=True, index=False, encoding='utf-8-sig')

print ("Data cleaned")

#writing to excel to avoid csv issues in prices_data
for entry in glob('Hotel_Region/*csv'):
    with open(entry, 'r') as f:
        data = pd.read_csv(entry)
        writer = pd.ExcelWriter(entry + 'output.xlsx', engine='xlsxwriter')
        data.to_excel(writer, index=False)
        writer.save()

print("Excel saved")
