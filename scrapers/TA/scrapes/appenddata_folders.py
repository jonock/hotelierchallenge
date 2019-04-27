#this script will go through the hotel_price files and create one file with all data per hotel

import pandas as pd
from glob import glob
from glob import iglob
import os

rootdir_glob = '/Users/TobiasRordorf/Desktop/UNI/MBI\ HSG/4.\ Semester/Python/GitHub/hotelierchallenge/scrapers/TA/scrapes/Test/**/*'

#store data in pandas DataFrame
#all_data = pd.DataFrame()

file_list = [f for f in iglob('**/*', recursive=True) if os.path.isfile(f)]

#open every file in specified folder

for entry in file_list:
    all_data = pd.DataFrame()
    with open(entry, 'r') as f:
        df = pd.read_csv(entry)
        all_data = all_data.append(df, ignore_index=True)
        #x = all_data.describe()
        #write appended data to excel
        all_data.to_excel(entry + '_Prices_appended.csv')

print('Dates appended - Excel saved')
