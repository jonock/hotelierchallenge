#this script will go through the hotel_price files and delete unnecessary RainbowClubSA

import pandas as pd
import os
import xlsxwriter
from glob import glob

#First Clean Data

sort_influencers = pd.DataFrame()


for entry in glob('*.csv'):
    with open(entry) as g:
        sort_influencers = pd.read_csv(entry)
        #print(sort_influencers.tail())
        sort_influencers['Followers'] = sort_influencers['Followers'].apply(pd.to_numeric)
        sort_influencers.sort_values('Followers', ascending = False, inplace=True)
        sort_influencers.to_csv(entry + 'new.csv', header=True, index=False, encoding='utf-8-sig')

print('all sorted - Done')
