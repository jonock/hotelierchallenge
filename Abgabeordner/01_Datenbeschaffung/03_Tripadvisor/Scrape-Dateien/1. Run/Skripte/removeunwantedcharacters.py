#Convert xlsx to csv because of numeric problems

import pandas as pd
from glob import glob
import numpy as np


#open every file in specified folder
for entry in glob('Test/*.xlsx'):
    with open(entry, 'r') as f:
        region_prices = pd.read_excel(entry, index_col=None)

        #region_prices.sort_values('price_per_night')
        region_prices.to_excel(entry, index=False)
print("Done")
