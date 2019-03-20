import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.instagram.com/explore/tags/berlin/');
time.sleep(1) # Let the user actually see something!
number=driver.find_element_by_xpath('//*[(@class = "-nal3 ")]')
print(number.text)
time.sleep(1) # Let the user actually see something!
driver.quit()
