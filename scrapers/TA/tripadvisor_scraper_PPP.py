#!/usr/bin/env python
from __future__ import print_function
from datetime import datetime
from time import time
from lxml import html,etree
import requests,re
import os,sys
import unicodecsv as ucsv
import argparse
import csv as ccsv

MAX_RETRY = 10
RETRY = 0

def URLS(filename):
    with open(filename) as csv_file:
        csv_reader = ccsv.reader(csv_file, delimiter=',')
        csv_reader = list(csv_reader)
        csv_list = list()
        for i in csv_reader:
            csv_list.append(i[0])
        print(csv_list)
        print(len(csv_list))
        return(list(csv_list))

def process_request(url,checkin_date,checkout_date):

    headers = {
                        'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                        'Accept-Encoding': 'gzip,deflate',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Cache-Control': 'no-cache',
                        'Connection': 'keep-alive',
                        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
                        'Host': 'www.tripadvisor.com',
                        'Pragma': 'no-cache',
                        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0',
                        'X-Requested-With': 'XMLHttpRequest'
                    }
    cookies=  {"SetCurrency":"CHF"}

    checkin_date = datetime.strptime(checkin_date,"%Y/%m/%d")
    checkout_date = datetime.strptime(checkout_date,"%Y/%m/%d")
    date = checkin_date.strftime("%Y_%m_%d")+"_"+checkout_date.strftime("%Y_%m_%d")
    #form data to get the hotels list from TA for the selected date
    form_data = {
    'changeSet': 'TRAVEL_INFO',
            'showSnippets': 'false',
            'staydates':date,
            'uguests': '2',
    }
    print("Downloading search results page")
    page_response  = requests.post(url = url,data=form_data,headers = headers, cookies = cookies, verify=False)

    parser = html.fromstring(page_response.text, url)
    return process_page(parser, url)

def process_page(parser, url):
    hotel_data = []
    hotel_page = parser.xpath('//div[contains(@class,"page")]')

    for hotel in hotel_page:
        XPATH_NAME = './/h1[@id="HEADING"]//text()'
        XPATH_RANK = './/span[contains(@class,"popularity")]//text()'
        XPATH_AMENITIES = ".//div[contains(text(),'HOTEL FEATURES')]/following-sibling::div//div[@class='textitem']//text()"
        XPATH_HIGHLIGHTS = './/div[contains(@class,"HighlightedAmenities__amenityItem")]//text()'
        XPATH_OFFICIAL_DESCRIPTION = './/div[contains(text(),"Description")]/following-sibling::div//span[contains(@class,"introText")]//text()'
        XPATH_ADDITIONAL_INFO = ".//div[@class='section_content']//div[@class='sub_title']"
        XPATH_HOTEL_PRICE = './/div//a[contains(@class="dominant offer)]"/following-sibling::div//a//[contains/(text(),"data-pernight")]'
        Xpath_DATA_VENDOR= './/div//a[contains(@class="dominant offer)]"/following-sibling::div//a//[contains/(text(),"data-vendorname")]'

        raw_name = hotel.xpath(XPATH_NAME)
        raw_rank = hotel.xpath(XPATH_RANK)
        amenities = hotel.xpath(XPATH_AMENITIES)
        raw_highlights = hotel.xpath(XPATH_HIGHLIGHTS)
        raw_official_description = hotel.xpath(XPATH_OFFICIAL_DESCRIPTION)
        raw_hotel_price_per_night = hotel.xpath(XPATH_HOTEL_PRICE)
        raw_data_vendor = hotel.xpath(Xpath_DATA_VENDOR)
        name = clean(raw_name)
        rank = clean(raw_rank)
        timestamp = str(datetime.now());
        hotel_features = ','.join(raw_hotel_features)
        checkIn = checkin_date.strftime("%Y/%m/%d")
        checkOut = checkout_date.strftime("%Y/%m/%d")
        pricelen = (len(raw_hotel_price_per_night)) - 1
    #       print(pricelen)
        if pricelen < 0:
            r_price_night = 0;
            print('LENGTHBUG')
        else:
                r_price_night = raw_hotel_price_per_night[pricelen]
        print(r_price_night)
        ra_price_night = str(r_price_night).replace('CHF','').replace(' ','')
        print(ra_price_night)
        price_per_night = ''.join(str(ra_price_night)) if ra_price_night else None
        data_vendor = ''.join(raw_data_vendor).strip() if raw_data_vendor else None

        data = {
                    'hotel_name':name,
                    'hotel_rank':rank,
                    'url':url,
                    'timestamp':timestamp,
                    'checkOut':checkOut,
                    'checkIn':checkIn,
                    'hotel_features':hotel_features,
                    'price_per_night':price_per_night,
                    'booking_provider':data_vendor
        }
        hotel_data.append(data)
    return hotel_data

def writeTripAdvisor(data,url):
    with open('scrapes/tripadvisor_data_' + str(url).replace(' ','_').replace('/','_') + '_' + str(datetime.now())+'.csv','wb') as csvfile:
        fieldnames = ['hotel_name','hotel_rank','url','timestamp','checkIn','checkOut','hotel_features','price_per_night','booking_provider']
        writer = ucsv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
        print(str(len(data)) + ' Hotels für ' + url + ' gespeichert.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('checkin_date',help = 'Hotel Check In Date (Format: YYYY/MM/DD')
    parser.add_argument('checkout_date',help = 'Hotel Chek Out Date (Format: YYYY/MM/DD)')
    parser.add_argument('url',help = 'Search url')

    args = parser.parse_args()
    url = args.url
    checkin_date = datetime.strptime(args.checkin_date,"%Y/%m/%d")
    checkout_date = datetime.strptime(args.checkout_date,"%Y/%m/%d")
    checkIn = checkin_date.strftime("%Y/%m/%d")
    checkOut = checkout_date.strftime("%Y/%m/%d")
    today = datetime.now()

    if today<datetime.strptime(checkIn,"%Y/%m/%d") and datetime.strptime(checkIn,"%Y/%m/%d")<datetime.strptime(checkOut,"%Y/%m/%d"):
        data = parse(url,checkin_date,checkout_date)
        print("Writing to output file tripadvisor_data.csv")
        with open('scrapes/tripadvisor_data_' + str(url) + '_' + str(datetime.now())+'.csv','wb') as csvfile:
            fieldnames = ['hotel_name','hotel_rank','url','timestamp','checkIn','checkOut','hotel_features','price_per_night','booking_provider']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
            print(str(len(data)) + ' Hotels für ' + url +' gespeichert.')
    #checking whether the entered date is already passed
    elif today>datetime.strptime(checkIn,"%Y/%m/%d") or today>datetime.strptime(checkOut,"%Y/%m/%d"):
        print("Invalid Checkin date: Please enter a valid checkin and checkout dates,entered date is already passed")
    elif datetime.strptime(checkIn,"%Y/%m/%d")>datetime.strptime(checkOut,"%Y/%m/%d"):
        print("Invalid Checkin date: CheckIn date must be less than checkOut date")
