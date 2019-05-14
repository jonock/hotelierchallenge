#this script will go through the hotel_price files and create one file with all data

import pandas as pd
from glob import glob


for entry in glob('WEKA Hotels Backup/*.csv'):
    with open(entry, 'r') as f:
        df = pd.read_csv(entry)
        df['price_per_night'] = df['price_per_night'].str.strip()
        #print(df['price_per_night'])
        #df = pd.to_numeric(df['price_per_night'])
        indexNames = df[df['price_per_night'] == '0' ].index
        df.drop(indexNames, inplace=True)
        df.to_csv(entry, header=True, index=False, encoding='utf-8-sig' )
        print("Zero Values cleaned")
print("Completly All Zero Values cleaned")

all_data = pd.DataFrame()

for entry in glob('WEKA Hotels Backup/*.csv'):
    with open(entry, 'r') as f:
        df = pd.read_csv(entry)
        all_data = all_data.append(df, ignore_index=True)
        all_data.to_csv('All Hotels with Class', header=True, index=False, encoding='utf-8-sig' )

print('Data appended - Excel saved')
