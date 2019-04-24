#Convert xlsx to csv because of numeric problems

import pandas as pd
from glob import glob


#open every file in specified folder
for entry in glob('Test3/*.xlsx'):
    with open(entry, 'r') as f:
        region_prices = pd.read_excel(entry, index_col=None)

        region_prices['price_per_night'] = region_prices['price_per_night'].str.replace(',','')
        #region_prices = region_prices['price_per_night'].apply(pd.to_numeric).combine_first(region_prices)
        #avg = region_prices.loc[:, "price_per_night"].mean()
        #print(avg)
        region_prices.to_excel(entry + "_removed.xlsx", index=False)
print("Done")
