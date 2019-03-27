import tripadvisor_scraper
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Input-File
localities = tripadvisor_scraper.importHashtagList('city.txt')

#Daten:"%Y/%m/%d"
checkin_date = '2019/04/13'
checkout_date = '2019/04/14'
sort = 'recommended'

for locality in localities:
    print(locality + ' kommt nun')
    for _ in range(3):   #beim ersten scrapen nimmts die Preise nicht immer, deshalb der Loop hier.
        data = tripadvisor_scraper.parse(locality,checkin_date,checkout_date,sort)
    tripadvisor_scraper.writeTripAdvisor(data, locality)




#Notiz Hotel Meloneras
#Post 27.3 17:30
#First Scrape 27.3 18:30
#TR
