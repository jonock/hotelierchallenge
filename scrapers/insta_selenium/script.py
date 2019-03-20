import time
from selenium import webdriver
import csv
from datetime import datetime
from hashtaghandler import *

hashtags = getHashtags()
results = scrapeHashtags()
writeHashtags(results)
