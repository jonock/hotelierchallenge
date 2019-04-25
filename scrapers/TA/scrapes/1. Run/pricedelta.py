#this script will help calculate the deltas of prices to be able to compare them more easily to different price levels

import pandas as pd
import numpy as np
import os
from glob import glob

#open xlsx in folder:
for entry in glob('Test/*.xlsx'):
    with open(entry, 'r') as f:
        df = pd.read_excel(entry, index_col=None)

        #make sure price_per_night is sorted from first date on
        
        #set first price to 0 value as baseline
