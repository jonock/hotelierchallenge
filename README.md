# Hotelier Challenge - Dokumentation
## This repository contains all relevant scripts and data for the «Hotelier-Case»
The code was developed as a student project at the University of St. Gallen. 


## Dieses Repository enthält alle verwendeten Skripte für den Hotelier-Case

- Ordner "Scrapers"
    - enthält die Inputfiles, Skripte und Ausgabefiles von gescrapten Hotel-Preisen
    - enthält die Skripte für Instagram-Selenium (Hilfestellung um Influencer-Posts aufzuspüren)
    - enthält die Daten, die über mehrere Wochen gesammelt wurden 

- Ordner "Twitter-Scripts"
    - enthält die Skripte und Outputfiles zur "Überwachung" der Hashtags #Hotel und #Resort auf twitter
      und stellt dar wie viel Reach diese Posts potenziell haben können.

- Ordner "Tableau"
    - wird die Tableau Workbooks zur Datenvisualisierung enthalten
    
## Installation
- Clone auf einem Server mit Ubuntu 16.04 LTS


- Ausführen des install.sh Skripts
```
sudo bash ./install.sh
```

- Crontab für Files einrichten
(git pull und git push funktioniert nur mit SSH-Fingerprint)


```
11 * * * * cd ~/hotelierchallenge && git pull
12 * * * * cd ~/hotelierchallenge/scrapers/TA && python3 ./script.py
12 * * * * cd ~/hotelierchallenge/scrapers/TA && python3 ./spechotelscript.py
01 08 * * * cd ~/hotelierchallenge && bash gitCommitDigitalOcean.sh
```
