import time
from selenium import webdriver
import csv
from datetime import datetime
from hashtaghandler import *

#Automatische Suche:
hashtags = importHashtagList('../TA/city.txt')
#Manuelle Suche:
#hashtags = getHashtags()

results = scrapeHashtags(hashtags)
writeHashtags(results)
