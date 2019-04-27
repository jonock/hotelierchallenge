import time
from selenium import webdriver
import csv
from datetime import datetime
from selenium.webdriver.chrome.options import Options


def scrapeMariott():
    options = Options()
    options.headless = False
    hotels=[1]
#    driver = webdriver.Chrome(executable_path=os.path.abspath(“chromedriver"),chrome_options=chrome_options)
    results = []
    for i in hotels:
        driver = webdriver.Chrome('chromedriver', chrome_options=options)
        driver.get('www.mariott.de/hotels/travel/mlesi-sheraton-maldives-full-moon-resort-and-spa/')
        driver.click_element_by_xpath('//table[@id="6FDUWD3N_hotel-fromToDate_table"]/tbody/tr[3]/td[6]/div')
        driver.click_element_by_xpath('/table[@id="6FDUWD3N_hotel-fromToDate_table"]/tbody/tr[3]/td[7]/div')
        time.sleep(10) # Let the user actually see something!
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

def writeResults(results):
    filename = str('instahashtags' + str(datetime.now())+'.csv')
    print("Writing to output file " + str(filename))
    with open('scrapes/' + filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(results)
    print('CSV geschrieben, tschüss!')
