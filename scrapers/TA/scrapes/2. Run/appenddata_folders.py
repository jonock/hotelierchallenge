#this script will go through the hotel_price files and create one file with all data per hotel

import pandas as pd
from glob import glob
from glob import iglob
import os

rootdir = './1_SpecHotel'
#open every file in specified folder

for sfolder in os.listdir(rootdir):
#    print(sfolder)
    if sfolder == '.DS_Store':
        continue
    childdir = os.path.join(rootdir, sfolder)
    all_data = pd.DataFrame()
    all_data.drop(all_data.index, inplace=True)
    sfoler = childdir + '/*.csv'
    n=0
    for entry in glob(sfoler):
        n = n + 1
        with open(entry, 'r') as f:
            df = pd.read_csv(entry)
            all_data = all_data.append(df, ignore_index=True)
    print(str(n)+' mal geschrieben bei '+ sfolder)
    #print(len(all_data))
    filename = 'Appended/' + str(sfolder)+'_append.csv'
    all_data.to_csv(filename, header=True, index=False, encoding='utf-8-sig' )

print('Dates appended - Excel saved')
