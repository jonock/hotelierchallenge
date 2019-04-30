#!/bin/sh
echo Jetzt wird alles installiert
sudo apt-get install libxml2-dev -y libxslt1-dev -y
echo Erste Hürde halbwegs geschafft, jetzt kommt der Python Kram
pip install -r requirements.txt
echo ok, das wars
