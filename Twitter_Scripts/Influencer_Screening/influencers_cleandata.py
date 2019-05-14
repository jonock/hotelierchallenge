#this script will go through the hotel_price files and delete unnecessary RainbowClubSA

import pandas as pd
import os
import xlsxwriter
from glob import glob

#First Clean Data

influencers = pd.DataFrame()
all_influencers = pd.DataFrame()

n = 0
x = 0
for entry in glob('Exports/*.csv'):
    with open(entry, 'r') as f:
        influencers = pd.read_csv (entry)
        #influencers.sort_values('Followers', ascending = False, inplace=True)
        n = n + 1
        x = x + len(influencers)

        try:
            #influencers.drop('Date', axis=1, inplace=True)    -> to remove exact duplicates, this is still needed
            influencers.drop('Retweets', axis=1, inplace=True)
            influencers.drop('Favorites', axis=1, inplace=True)
            influencers.drop('Date', axis=1, inplace=True)
        except:
            next
        #n = n + 1
        #print(n, 'dropped')

        all_influencers = all_influencers.append(influencers, ignore_index=True)

        #Remove duplicates based on column TweetId
        #duplicated_influencers = all_influencers.duplicated(subset=['TweetID'], keep='first')
        #all_influencers = all_influencers[~duplicated_influencers]

        #influencers.drop('TweetID', axis=1, inplace=True)

        print(n, x, len(all_influencers))
        all_influencers.to_csv('Influencers_appended.csv', header=True, index=False, encoding='utf-8-sig')

print ('all appended')
