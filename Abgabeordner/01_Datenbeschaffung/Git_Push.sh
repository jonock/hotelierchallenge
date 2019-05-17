#!/bin/bash
#Git: Add and commit changes
cd ~/desktop/hotelierchallenge/scrapers/TA/scrapes/spechotel && git commit -a -m "Neue Scrapes"
#send data to Git Server
cd ~/desktop/hotelierchallenge/scrapers/TA && git push origin master
