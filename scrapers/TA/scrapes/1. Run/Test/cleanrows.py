#this script will go through the hotel_price files and delete unnecessary RainbowClubSA

import pandas as pd

prices = pd.read_csv ('tripadvisor_data_https___www.tripadvisor.ch_Hotel_Review-g60763-d1938661-Reviews-Row_NYC_Hotel-New_York_City_New_York.html_2019-04-04 13-01-08.431706.csv')

#To delete columns axis = 1
prices.drop('platform_name', axis=1, inplace=True)

#delete rows (axis = 0)
prices.drop(prices.index[1:],axis = 0, inplace=True)


prices.to_csv("testend.csv")

print("Done")
