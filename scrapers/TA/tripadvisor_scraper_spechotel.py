#!/usr/bin/env python

#Modification of tripadvisor_scraper.py file from jonock to scrape for prices of a specific hotel

from __future__ import print_function
from datetime import datetime
from time import time
from lxml import html,etree
import requests,re
import os,sys
import unicodecsv as ucsv
import argparse
import csv as ccsv

timestamp = datetime.now()

def importHashtagList(filename):
    with open(filename) as csv_file:
        csv_reader = ccsv.reader(csv_file, delimiter=',')
        csv_reader = list(csv_reader)
        csv_list = list()
        for i in csv_reader:
            csv_list.append(i[0])
        print(csv_list)
        print(len(csv_list))
        return(list(csv_list))


#locality etc. are parameters of the function
def singleparse(full_url,checkin_date,checkout_date,sort):
    checkin_date = datetime.strptime(checkin_date,"%Y/%m/%d")
    checkout_date = datetime.strptime(checkout_date,"%Y/%m/%d")
    checkIn = checkin_date.strftime("%Y/%m/%d")
    checkOut = checkout_date.strftime("%Y/%m/%d")
    print("Scraper Inititated for Locality: %s"%full_url)
    # TA rendering the autocomplete list using this API
    print("Finding search result page URL")
    #url_from_autocomplete = "http://www.tripadvisor.com"+api_response['results'][0]['url']
    url_from_autocomplete = ""
    print('URL found %s'%url_from_autocomplete)    #Formating date for writing to file

    date = checkin_date.strftime("%Y_%m_%d")+"_"+checkout_date.strftime("%Y_%m_%d")
    #form data to get the hotels list from TA for the selected date
    form_data = {'changeSet': 'TRAVEL_INFO',
            'showSnippets': 'false',
            'staydates':date,
            'uguests': '2',
            'sortOrder':sort
    }
    #Referrer is necessary to get the correct response from TA if not provided they will redirect to home page
    headers = {
                            'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                            'Accept-Encoding': 'gzip,deflate',
                            'Accept-Language': 'en-US,en;q=0.5',
                            'Cache-Control': 'no-cache',
                            'Connection': 'keep-alive',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
                            'Host': 'www.tripadvisor.com',
                            'Pragma': 'no-cache',
                            'Referer': url_from_autocomplete,
                            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0',
                            'X-Requested-With': 'XMLHttpRequest'
                        }
    cookies=  {"SetCurrency":"CHF"}
    print("Downloading search results page")
    page_response  = requests.post(url = full_url, data=form_data,headers = headers, cookies = cookies, verify=False)
    print("Parsing results ")
    parser = html.fromstring(page_response.text)
#    print(page_response.text)
#    print(parser)
    hotel_lists = parser.xpath('//*')

    XPATH_PLATFORM_NAME = './/div[contains(@class,"vendor")]//text()'
    XPATH_HOTEL_PRICE = './/span[contains(@class,"price")]/text()'

#    raw_platform_name = hotel_lists.xpath(XPATH_PLATFORM_NAME)
    print(hotel_lists[5])
    hotel_data = []
    for i in hotel_lists:
        print(str(i.text)+' HIER')
        raw_hotel_price_per_night = i.xpath(XPATH_HOTEL_PRICE)
        raw_platform_name = i.xpath(XPATH_PLATFORM_NAME)
#        print(raw_platform_name)
#        print(raw_hotel_price_per_night)

        name = ''.join(raw_platform_name).strip() if raw_platform_name else None
#    timestamp = str(datetime.now())
        pricelen = (len(raw_hotel_price_per_night)) - 1
#        print(pricelen)
        if pricelen < 0:
            r_price_night = 0;
            print('LENGTHBUG')
        else:
            r_price_night = raw_hotel_price_per_night[pricelen]
        print(r_price_night)
        ra_price_night = str(r_price_night).replace('CHF','').replace(' ','')
        print(ra_price_night)
        price_per_night = ''.join(str(ra_price_night)) if ra_price_night else None

        data = {
                    #'platform_name':name,
                    'price_per_night':price_per_night,
                    'timestamp':timestamp
        }
        print(data)
        hotel_data.append(data)
    return hotel_data

def writeTripAdvisor(data,namestr):
    with open('scrapes/spechotel/tripadvisor_data_test' + str(namestr).replace('https://','_').replace('/','_') + '_' + str(datetime.now()).replace(':','-') +'.csv','wb') as csvfile:
        #'platform_name' deleted from csv for now
        fieldnames = ['price_per_night', 'timestamp']
        writer = ucsv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
        print(str(len(data)) + ' gespeichert.')

#
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('checkin_date',help = 'Hotel Check In Date (Format: YYYY/MM/DD)')
    parser.add_argument('checkout_date',help = 'Hotel Chek Out Date (Format: YYYY/MM/DD)')
    sortorder_help = """
    available sort orders are :\n
    priceLow - hotels with lowest price,
    distLow : Hotels located near to the search center,
    recommended: highest rated hotels based on traveler reviews,
    popularity :Most popular hotels as chosen by Tripadvisor users
    """
    parser.add_argument('sort',help = sortorder_help,default ='popularity ')
    parser.add_argument('locality',help = 'Search Locality')
    args = parser.parse_args()
    locality = args.locality
    checkin_date = datetime.strptime(args.checkin_date,"%Y/%m/%d")
    checkout_date = datetime.strptime(args.checkout_date,"%Y/%m/%d")
    sort= args.sort
    checkIn = checkin_date.strftime("%Y/%m/%d")
    checkOut = checkout_date.strftime("%Y/%m/%d")
    today = datetime.now()

    if today<datetime.strptime(checkIn,"%Y/%m/%d") and datetime.strptime(checkIn,"%Y/%m/%d")<datetime.strptime(checkOut,"%Y/%m/%d"):
        data = parse(locality,checkin_date,checkout_date,sort)
        print("Writing to output file tripadvisor_data.csv")
        with open('scrapes/tripadvisor_data_' + str(locality) + '_' + str(datetime.now())+'.csv','wb') as csvfile:
            fieldnames = ['hotel_name','url','locality','reviews','tripadvisor_rating','checkIn','checkOut','price_per_night','booking_provider','no_of_deals','hotel_features']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
            print(str(len(data)) + ' Hotels für ' + locality +' gespeichert.')
    #checking whether the entered date is already passed
    elif today>datetime.strptime(checkIn,"%Y/%m/%d") or today>datetime.strptime(checkOut,"%Y/%m/%d"):
        print("Invalid Checkin date: Please enter a valid checkin and checkout dates,entered date is already passed")
    elif datetime.strptime(checkIn,"%Y/%m/%d")>datetime.strptime(checkOut,"%Y/%m/%d"):
        print("Invalid Checkin date: CheckIn date must be less than checkOut date")
