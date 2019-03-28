import tripadvisor_scraper_spechotel
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Input-File
urls = tripadvisor_scraper_spechotel.importHashtagList('urls.txt')

#Daten:"%Y/%m/%d"
checkin_date = '2019/04/13'
checkout_date = '2019/04/14'
sort = 'recommended'

for url in urls:
    print(url + ' kommt nun')
    for _ in range(3):   #beim ersten scrapen nimmts die Preise nicht immer, deshalb der Loop hier.
        data = tripadvisor_scraper_spechotel.singleparse(url,checkin_date,checkout_date,sort)
    tripadvisor_scraper.writeTripAdvisor(data, 'TEST')


#Achtung: um den Überblick über die Meloneras price scrapes csv zu behalten werden sie in einen Unterordner in scrapes gespeichert
#dieser ist in der def writeTripAdvisor modifiziert.

#Notiz Hotel Meloneras
#Post 27.3 17:30
#First Scrape 27.3 18:30  (rough frequency: 30min)
#TR
