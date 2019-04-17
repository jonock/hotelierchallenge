#this script will go through the hotel_price files and delete unnecessary RainbowClubSA

import pandas as pd

prices = pd.read_csv ('test.csv')

#To delete columns axis = 1
#prices.drop('column', axis=1, inplace=True)


prices.drop(prices.index[1:],axis = 0, inplace=True)

x = prices.head(3)
print(x)
