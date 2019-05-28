#this script will go through the WEKA hotel files with classes and delete rows that contain
#a zero value in the column "price_per_night" and then appends all the data into one csv.

import pandas as pd
from glob import glob


for entry in glob('WEKA Hotels Backup/*.csv'):
    with open(entry, 'r') as f:
        df = pd.read_csv(entry)
        df['price_per_night'] = df['price_per_night'].astype(str)
        df['price_per_night'] = df['price_per_night'].str.strip()
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
        all_data.to_csv('All Hotels with Class_without Zero values', header=True, index=False, encoding='utf-8-sig' )

print('Data appended - Excel saved')
