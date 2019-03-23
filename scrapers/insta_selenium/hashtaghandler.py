import time
from selenium import webdriver
import csv
from datetime import datetime
from selenium.webdriver.chrome.options import Options


def getHashtags():
    n = int(input('Wieviele Abfragen '))
    hashtag = list(range(n))
    print(hashtag)
    for x in hashtag:
        message = ('Gib Hashtag ' + str(x+1) + ' von ' + str(n) + ' ')
        hash = str(input(message))
        print(hash)
        hashtag[x] = str(hash)
    print('Deine Hashtags sind: ' + str(hashtag) + '. Jetzt gehts richtig los!')
    return(hashtag)

def scrapeHashtags(hashtag):
    options = Options()
    options.headless = True
#    driver = webdriver.Chrome(executable_path=os.path.abspath(“chromedriver"),chrome_options=chrome_options)
    results = []
    for i in hashtag:
        driver = webdriver.Chrome('chromedriver', chrome_options=options)
        driver.get('https://www.instagram.com/explore/tags/' + str(i));
        time.sleep(0) # Let the user actually see something!
        try:
            number = driver.find_element_by_xpath('//*[(@class = "-nal3 ")]')
            print(i + str(" ") + number.text)
            result = number.text
            result = result.replace(',','')
            result = result.replace(' posts','')
            results.append([str(i),result])
            time.sleep(0) # Let the user actually see something!
            driver.quit()
        except:
            result = 0
            print(str(i) + ' hat keine Hashtags')
            results.append([str(i),result])
            driver.quit()
            pass

    print(results)
    return(results)

def importHashtagList(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader = list(csv_reader)
        csv_list = list()
        for i in csv_reader:
            csv_list.append(i[0].replace(' ','').replace('-','').replace('/','').replace('.',''))
        print(csv_list)
        print(len(csv_list))
        return(list(csv_list))

def writeHashtags(results):
    filename = str('instahashtags' + str(datetime.now())+'.csv')
    print("Writing to output file " + str(filename))
    with open('scrapes/' + filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(results)
    print('CSV geschrieben, tschüss!')
