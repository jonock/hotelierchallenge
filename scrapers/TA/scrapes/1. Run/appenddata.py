#this script will go through the hotel_price files and create one file with all data

import pandas as pd
from glob import glob

#store data in pandas DataFrame
all_data = pd.DataFrame()

#open every file in specified folder
for entry in glob('Paris/*.xlsx'):
    with open(entry, 'r') as f:
        df = pd.read_excel(entry)
        all_data = all_data.append(df, ignore_index=True)
        #x = all_data.describe()
        #write appended data to excel
        all_data.to_excel('Aphrodite_Prices_appended.xlsx')

print('Dates appended - Excel saved')
