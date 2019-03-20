import time
from selenium import webdriver
import csv
from datetime import datetime
from hashtaghandler import *

hashtags = importHashtagList('us-cities.txt')

#hashtags = getHashtags()
results = scrapeHashtags(hashtags)
writeHashtags(results)
