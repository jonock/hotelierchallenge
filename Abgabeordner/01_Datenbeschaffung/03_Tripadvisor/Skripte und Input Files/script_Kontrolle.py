import tripadvisor_scraper_spechotel_Kontrolle
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Input-File
urls = tripadvisor_scraper_spechotel_Kontrolle.importHashtagList('urls_Kontrolle.txt')

#Daten:"%Y/%m/%d"
checkin_date = '2019/05/18'
checkout_date = '2019/05/19'
sort = 'recommended'

for url in urls:
    print(url + ' kommt nun')
    for _ in range(3):   #beim ersten scrapen nimmts die Preise nicht immer, deshalb der Loop hier.
        data = tripadvisor_scraper_spechotel_Kontrolle.singleparse(url,checkin_date,checkout_date,sort)
    tripadvisor_scraper_spechotel_Kontrolle.writeTripAdvisor(data, url)


#Achtung: um den Überblick über die Meloneras price scrapes csv zu behalten werden sie in einen Unterordner in scrapes gespeichert
#dieser ist in der def writeTripAdvisor modifiziert.

#Notiz Hotel Meloneras
#Post 27.3 17:30
#First Scrape 27.3 18:30  (rough frequency: 30min)
#TR
