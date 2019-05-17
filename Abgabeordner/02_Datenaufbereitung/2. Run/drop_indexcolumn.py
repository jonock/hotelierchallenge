#this script will go through the hotel_price files and create one file with all data

import pandas as pd
from glob import glob

#store data in pandas DataFrame
all_data = pd.DataFrame()
#open every file in specified folder

for entry in glob('WEKA Hotels/*.csv'):
    with open(entry, 'r') as f:
        df = pd.read_csv(entry)
        df.drop('Index', axis=1, inplace=True)

        all_data.to_csv(entry, header=True, index=False, encoding='utf-8-sig' )

print('Data appended - Excel saved')
