#this script will go through the hotel_price files and create one file with all data

import pandas as pd
from glob import glob

#store data in pandas DataFrame
all_data = pd.DataFrame()
#open every file in specified folder

for entry in glob('Test/*.csv'):
    with open(entry, 'r') as f:
        df = pd.read_csv(entry)
        for i,v in df.items():
            if (isinstance(v, str)):
                df.iloc[i] = float(v.replace(' ',''))
        #newdf = pd.to_numeric(df['price_per_night'])
        indexNames = df[df['price_per_night'] == 0 ].index
        df.drop(indexNames, inplace=True)
        all_data.to_csv(entry, header=True, index=False, encoding='utf-8-sig' )

print("Zero Values cleaned")

#for entry in glob('WEKA Hotels Backup/*.csv'):
#    with open(entry, 'r') as f:
#        df = pd.read_csv(entry)
#        all_data = all_data.append(df, ignore_index=True)
#        all_data.to_csv('All Hotels with Class', header=True, index=False, encoding='utf-8-sig' )

#print('Data appended - Excel saved')
