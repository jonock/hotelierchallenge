import time
from selenium import webdriver
import csv
from datetime import datetime
from selenium.webdriver.chrome.options import Options


def getTravelinformation():
    n = int(input('Wieviele Abfragen '))
    travel = list(range(n))
    print(travel)
    for x in travel:
        message = ("Gib Stadt " + str(x+1) + " von " + str(n) + " ")
        hotel = str(input(message))
        print(hotel)
        travel[x] = str(hotel)
    print("Deine Städte sind: " + str(travel) + ". Jetzt gehts richtig los!")
    return(travel)

def scrapehotels(travel):
    options = Options()
    options.headless = True
#    driver = webdriver.Chrome(executable_path=os.path.abspath(“chromedriver"),chrome_options=chrome_options)
    results = []
    for i in travel:
        driver = webdriver.Chrome('chromedriver', chrome_options=options)
        driver.get('https://www.booking.com' + str(n));
        time.sleep(10) # Let the user actually see something!
        try:
            price = driver.find_element_by_xpath('//*[(@class = "b ")]')
            print(n + str(" ") + price.text)
            result = price.text
            time.sleep(10) # Let the user actually see something!
            driver.quit()
        except:
            result = 0
            print(str(n) + ' hat kein Hotel')
            results.append([str(i),result])
            driver.quit()
            pass

    print(results)
    return(results)

def importHotelList(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader = list(csv_reader)
        csv_list = list()
        for n in csv_reader:
            csv_list.append(i[0].replace(' ','').replace('-','').replace('/','').replace('.',''))
        print(csv_list)
        print(len(csv_list))
        return(list(csv_list))

def writeHotels(results):
    filename = str('Hotelpreis' + str(datetime.now())+'.csv')
    print("Writing to output file " + str(filename))
    with open('scrapes/' + filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(results)
    print('CSV geschrieben, tschüss!')
