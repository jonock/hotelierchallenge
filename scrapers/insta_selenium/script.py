import time
from selenium import webdriver
import csv
from datetime import datetime
from hashtaghandler import *

hashtags = importHashtagList('world-cities_csv.csv')

#hashtags = getHashtags()
results = scrapeHashtags(hashtags)
writeHashtags(results)
