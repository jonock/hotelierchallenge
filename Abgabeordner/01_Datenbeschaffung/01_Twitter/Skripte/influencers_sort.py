########  Twitter Sorting Script   ########

### Description
### This script helps analyze the twitter scripts by sorting the Follower counts

import pandas as pd
import os
from glob import glob

sort_influencers = pd.DataFrame()

for entry in glob('*.csv'):
    with open(entry) as g:
        sort_influencers = pd.read_csv(entry)
        sort_influencers['Followers'] = sort_influencers['Followers'].apply(pd.to_numeric)
        sort_influencers.sort_values('Followers', ascending = False, inplace=True)
        sort_influencers.to_csv(entry + 'new.csv', header=True, index=False, encoding='utf-8-sig')

print('all sorted - Done')
