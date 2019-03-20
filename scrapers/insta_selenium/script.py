import time
from selenium import webdriver
import csv
from datetime import datetime


results = []
n = int(input('Wieviele Abfragen '))
hashtag = list(range(n))
print(hashtag)
for x in hashtag:
    message = ('Gib Hashtag ' + str(x+1) + ' von ' + str(n) + ' ')
    hash = str(input(message))
    print(hash)
    hashtag[x] = str(hash)

print('Deine Hashtags sind: ' + str(hashtag) + '. Jetzt gehts richtig los!')

for i in hashtag:
    driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
    driver.get('https://www.instagram.com/explore/tags/' + str(i));
    time.sleep(5) # Let the user actually see something!
    number=driver.find_element_by_xpath('//*[(@class = "-nal3 ")]')
    print(number.text)
    result = number.text
    result = result.replace(',','')
    result = result.replace(' posts','')
    results.append([str(i),result])
    time.sleep(0) # Let the user actually see something!
    driver.quit()

print(results)

filename = str('instahashtags' + str(datetime.now())+'.csv')
print("Writing to output file " + str(filename))
with open('scrapes/' + filename, "w") as f:
    writer = csv.writer(f)
    writer.writerows(results)
