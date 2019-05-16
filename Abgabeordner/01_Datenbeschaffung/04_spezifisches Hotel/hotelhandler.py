import time
from selenium import webdriver
import csv
from datetime import datetime
from selenium.webdriver.chrome.options import Options

def scrapeAnantara():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)
    hotels=[1]
#    driver = webdriver.Chrome(executable_path=os.path.abspath(“chromedriver"),chrome_options=chrome_options)
    results = []
    for i in hotels:
#        driver = webdriver.Chrome('chromedriver', chrome_options=options)
        driver.get('https://secure.minorhotels.com/rooms.aspx?bc=AN&hc=AQA&checkin=18/05/2019&nights=1&adults=2&rooms=1&children=0&roomcode=&language=de&_ga=2.170835232.1890400155.1556293984-1478239563.1556293984')
        time.sleep(2) # Let the user actually see something!
        try:
            number = driver.find_element_by_xpath('//div[@class="right"]')
#            print(number)
#            print(str(" Output: ") + number.text)
            result = number.text
            resultStripped = result[:9]
            resultStripped = resultStripped.replace('CHF','').replace(' ','').replace('\np','').replace('\n','').replace('\\','')
#            print(resultStripped)

            results.append([str('Anantara (Qasr al Sarab)'),resultStripped,str(datetime.now())])
            time.sleep(0) # Let the user actually see something!
            driver.quit()
        except:
            result = 0
            print('Uiuiui, das hat nicht geklappt')
            results.append([str(i),result])
            driver.quit()
            pass

    print('Hotel Anantara (Qasr al Sarab): ' + str(results))
    return(results)



def scrapeMariott():
    options = Options()
    options.headless = False
    hotels=[1]
#    driver = webdriver.Chrome(executable_path=os.path.abspath(“chromedriver"),chrome_options=chrome_options)
    results = []
    for i in hotels:
        driver = webdriver.Chrome('chromedriver', chrome_options=options)
        driver.get('http://www.google.com')
        driver.get('https://www.marriott.com/search/submitSearch.mi?roomTypeCode=&recordsPerPage=20&autoSuggestItemType=&destinationAddress.types=country%2Cpolitical&destinationAddress.latitude=&propertyCode=&destinationAddress.stateProvinceShort=&isInternalSearch=true&destinationAddress.cityPopulation=&vsInitialRequest=false&searchType=InCity&destinationAddress.locality=&showAddressPin=&miniStoreFormSubmit=&destinationAddress.stateProvinceDisplayName=&destinationAddress.destinationPageDestinationAddress=&countryName=&destinationAddress.stateProvince=&searchRadius=50.0&singleSearchAutoSuggest=&missingcheckInDateMsg=Please+enter+a+check-in+date.&destinationAddress.placeId=ChIJvXv7qr-ZtSQRiWKVgeEJRUE&is-hotelsnearme-clicked=false&destinationAddress.addressline1=&airportName=&for-hotels-nearme=Near&missingcheckOutDateMsg=Please+enter+a+check-out+date.&pageType=advanced&destinationAddress.country=MV&destinationAddress.name=&poiCity=&destinationAddress.countryShort=&marriottBrands=SI&poiName=&destinationAddress.address=Maldives&search-countryRegion=&collapseAccordian=is-hidden&singleSearch=true&destinationAddress.cityPopulationDensity=&destinationAddress.secondaryText=&destinationAddress.postalCode=&destinationAddress.city=&destinationAddress.mainText=Maldives&airportCode=&isTransient=true&destinationAddress.longitude=&initialRequest=false&destinationAddress.website=&search-locality=&dimensions=0&roomTypeCode=&propertyCode=&flexibleDateSearchRateDisplay=false&propertyName=&isSearch=true&marriottRewardsNumber=&isRateCalendar=false&incentiveType_Number=&incentiveType=&flexibleDateLowestRateMonth=&flexibleDateLowestRateDate=&js-location-nearme-values=&destinationAddress.destination=Maldives&fromToDate=Sun%2C+May+19%2C+2019&fromToDate_submit=05%2F19%2F2019&fromDate=05%2F18%2F2019&toDate=05%2F19%2F2019&flexibleDateSearch=false&lengthOfStay=1&roomCountBox=1+Room&roomCount=1&guestCountBox=2+Adults+Per+Room&numAdultsPerRoom=2&childrenCountBox=0+Children+Per+Room&childrenCount=0&childrenAges=&clusterCode=none&corporateCode=')
        time.sleep(2) # Let the user actually see something!
        driver.find_element_by_xpath('//table[@id="6FDUWD3N_hotel-fromToDate_table"]/tbody/tr[3]/td[6]/div').click()
        driver.find_element_by_xpath('/table[@id="6FDUWD3N_hotel-fromToDate_table"]/tbody/tr[3]/td[7]/div').click()
        try:
            number = driver.find_element_by_xpath('//*[/html/body/div[2]/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/div[1]/ul/li[2]/a/span[2]')
            print(str(" Die Nummer: ") + number.text)
            result = number.text
            result = result.replace(',','')
            result = result.replace(' posts','')
            results.append([str(i),result])
            time.sleep(0) # Let the user actually see something!
            driver.quit()
        except:
            result = 0
            print('Uiuiui, das hat nicht geklappt')
            results.append([str(i),result])
            driver.quit()
            pass

    print(results)
    return(results)

def importLinks(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader = list(csv_reader)
        csv_list = list()
        for i in csv_reader:
            csv_list.append(i[0].replace(' ','').replace('-','').replace('/','').replace('.',''))
        print(csv_list)
        print(len(csv_list))
        return(list(csv_list))

def writeResults(results,hotelname):
    filename = str(str(hotelname) + str(datetime.now())+'.csv')
    print("Writing to output file " + str(filename))
    with open('scrapes/' + filename, "w") as f:
        fieldnames = ['hotel_name','price_per_night','timestamp']
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        writer.writerows(results)
    print('CSV geschrieben, tschüss!')
