#!/bin/sh
echo Jetzt wird lxml installiert
export LC_ALL=C
sudo apt-get update
sudo apt-get install python3-pip -y
sudo apt-get install unzip -y
sudo apt-get install libxml2-dev -y libxslt1-dev -y
sudo apt-get install python3-lxml python-lxml -y
sudo apt-get install chromium-browser -y
echo Erste Huerde halbwegs geschafft, jetzt kommt der Python Kram
echo Es folgt Selenium
wget https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo chmod a+x chromedriver
mv ./chromedriver scrapers/specHotelChains/
rm chromedriver_linux64.zip
echo Ok, jetzt noch die Python extensions
pip3 install --upgrade pip
pip3 install -r requirements.txt
echo ok, das wars
