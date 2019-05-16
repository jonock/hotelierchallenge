#this script will go through the hotel_price files and delete unnecessary RainbowClubSA

import pandas as pd
import os
import xlsxwriter
from glob import glob

#First Clean Data


duplicated_influencers = pd.DataFrame()

for entry in glob('*sorted.csv'):
    with open(entry) as g:
        influencers = pd.read_csv (entry)
        influencers.drop('TweetID', axis=1, inplace=True)

        influencers.sort_values('User', inplace=True)
        #Remove duplicates based on column TweetId
        influencers.drop_duplicates(subset = "User", keep = 'first', inplace = True)

        influencers.sort_values('Followers', ascending=False, inplace = True)


        influencers.to_csv(entry + 'Followers_unique.csv', header=True, index=False, encoding='utf-8-sig')

print ('duplicates removed')
