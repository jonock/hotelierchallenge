#this script will go through the hotel_price files and create one file with all data per hotel

import pandas as pd
from glob import glob
from glob import iglob
import os

rootdir = './2. Run'
#open every file in specified folder

for sfolder in os.listdir(rootdir):
#    print(sfolder)
    if sfolder == '.DS_Store':
        continue
    childdir = os.path.join(rootdir, sfolder)
    sfoler = childdir + '/*.csv'
    for entry in glob(sfoler):
        with open(entry, 'r') as f:
            os.remove(entry)
            print('file removed')

print('all files removed in: ', rootdir)
