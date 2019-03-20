import tripadvisor_scraper
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


localities = tripadvisor_scraper.importHashtagList('us-cities.txt')
#Daten:"%Y/%m/%d"
checkin_date = '2019/04/02'
checkout_date = '2019/04/04'
sort = 'recommended'

for locality in localities:
    print(locality + ' kommt nun')
    data = tripadvisor_scraper.parse(locality,checkin_date,checkout_date,sort)
    tripadvisor_scraper.writeTripAdvisor(data, locality)
