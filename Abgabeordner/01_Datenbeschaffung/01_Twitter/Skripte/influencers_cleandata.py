########  Twitter Cleaning Influencer CSVs   ########

### Description
### This script cleans unnecessary information from influencer scripts
### and appends them to one dataframe to be written into a new csv


import pandas as pd
import os
import xlsxwriter
from glob import glob


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

        #Append seperate files of influencers to one Dataframe
        all_influencers = all_influencers.append(influencers, ignore_index=True)

        print(n, x, len(all_influencers))
        all_influencers.to_csv('Influencers_appended.csv', header=True, index=False, encoding='utf-8-sig')

print ('all appended')
