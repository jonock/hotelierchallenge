#!/bin/sh
echo Jetzt wird lxml installiert
sudo apt-get install libxml2-dev -y libxslt1-dev -y
sudo apt-get install python3-lxml python-lxml -y
echo Erste Hürde halbwegs geschafft, jetzt kommt der Python Kram
echo Es folgt Selenium
wget https://chromedriver.storage.googleapis.com/75.0.3770.8/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
./chromedriver
sudo chmod a+x chromedriver
cp chromedriver /scrapers/specHotelChains
echo Ok, jetzt noch die Python extensions
pip install -r requirements.txt
echo ok, das wars
