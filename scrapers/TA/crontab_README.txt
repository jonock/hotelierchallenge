{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf600
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;}
{\*\expandedcolortbl;;\csgray\c0;\csgray\c100000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs22 \cf2 \cb3 \CocoaLigature0 # Das Dokument enth\'e4lt den Code f\'fcr das Programm crontab.\
# Damit ist ein automatisiertes Scrapen m\'f6glich\
\
## Input-Code:\
PATH=~/desktop/hotelierchallenge/scrapers/TA\
\
1 * * * * /usr/bin/git pull origin master \
\
1 * * * * cd ~/desktop/hotelierchallenge/scrapers/TA && ~/anaconda3/bin/python ~/desktop/hotelierchallenge/scrapers/TA/script_singlehotel.py\
\
PATH=~/desktop/hotelierchallenge/scrapers/TA\
\
1 * * * * cd ~/desktop/hotelierchallenge/scrapers/TA && ~/anaconda3/bin/python ~/desktop/hotelierchallenge/scrapers/TA/script.py\
\
1 * * * * cd ~/desktop/hotelierchallenge/scrapers/TA/scrapes/spechotel && /usr/bin/git commit -a -m "Neue Scrapes"\
\
1 * * * * cd ~/desktop/hotelierchallenge/scrapers/TA && /usr/bin/git push origin master\
\
// 11.04.2019}