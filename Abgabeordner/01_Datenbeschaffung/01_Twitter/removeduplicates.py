########  Twitter Script for Removing Duplicates   ########

### Description
### This script helps to clean the twitter posts by removing duplicates

#There are two steps to removing Duplicates
#1. Removing duplicates in TweetIDs to get unique tweets
#2. Removing duplicates in Users to get unique Users

import pandas as pd
import os
import xlsxwriter
from glob import glob


#duplicated_influencers = pd.DataFrame()


with open('Analyzed/Influencers_appended.csv') as g:
    influencers = pd.read_csv (g)
    #1. Step
    influencers.drop_duplicates(subset='TweetID', keep = 'first', inplace = True)
    influencers.sort_values('Followers', ascending=False, inplace = True)
    influencers.to_csv('Analyzed/Tweets_unique.csv', header=True, index=False, encoding='utf-8-sig')

    print('Tweet Duplicates removed')

    #Remove TweetIDs and sort User
    influencers.drop('TweetID', axis=1, inplace=True)
    influencers.sort_values('User', inplace=True)

    #Remove duplicates based on column TweetId
    influencers.drop_duplicates(subset = "User", keep = 'first', inplace = True)
    influencers.sort_values('Followers', ascending=False, inplace = True)

    print ('User Duplicates removed')

    influencers.to_csv('Analyzed/Users_unique.csv', header=True, index=False, encoding='utf-8-sig')

print ('Files saved')
