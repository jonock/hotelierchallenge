import time
from selenium import webdriver
import csv
from datetime import datetime
from booking import *

#Automatische Suche:
#travel = importHotelList('hotels.txt')
#Manuelle Suche:
travel = getTravelinformation()

results = scrapehotels(travel)
writetravel(results)
