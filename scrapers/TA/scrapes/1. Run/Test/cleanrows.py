#this script will go through the hotel_price files and delete unnecessary RainbowClubSA

import pandas as pd

prices = pd.read_csv ('Aphrodite_Palace-Rajecke_Teplice_Zilina_Region_2019-04-04 13-01-05.265798.csv')

#To delete columns axis = 1
prices.drop('platform_name', axis=1, inplace=True)

#delete rows (axis = 0)
prices.drop(prices.index[1:],axis = 0, inplace=True)


prices.to_csv("Aphrodite_Palace-Rajecke_Teplice_Zilina_Region_2019-04-04 13-01-05.265798.csv")

print("Done")
