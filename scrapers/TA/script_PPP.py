import tripadvisor_scraper_PPP
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Input-File
urls = tripadvisor_scraper_PPP.URLS('Hotels.txt')

#Daten:"%Y/%m/%d"
checkin_date = '2019/04/02'
checkout_date = '2019/04/04'

for url in urls:
    print(url + ' kommt nun')
    for _ in range(3):   #beim ersten scrapen nimmts die Preise nicht immer, deshalb der Loop hier.
        data = tripadvisor_scraper_PPP.process_request(url,checkin_date,checkout_date)
    tripadvisor_scraper_PPP.writeTripAdvisor(data,url)
