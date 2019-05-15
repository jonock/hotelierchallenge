## Der Ordner specHotelChains enthält das Skript im Bezug auf das Preis-Scraping auf der Seite der Hotels:

## Input-Files:
- hashtaglist.txt = 
		Dies ist der Input für script.py. Beim Input handelt es sich um eine Liste beliebiger Hashtags, für die die Anzahl gescrapt werden soll.

- Manuelle Abfrage =
		Durch Anpassung des script.py können die Hashtags auch ohne Zusatzfile auf Abfrage hin direkt analysiert werden.

(- us-cities.txt = hier handelt es sich um ein test input file.)

Python-Skripte:
- script.py = 
		Zweck: Dieses Skript läuft aus Selenium und führt ein Scraping für Hashtags durch.
		Input: hashtaglist.txt mit Hashtags für Regionen
		Ausgeführte Funktionen: hashtaghandler.py
		Output: CSV-Datei mit Anzahl an gefundenen Hashtags
		Speicherort Output: ~/hotelierchallenge/scrapers/insta_selenium/scrapes


Die CSV Ausgabedateien werden in den Unterordner des Ordners "Scrapes" abgespeichert.

## Quellen:
- hashtaghandler.py =
		Quelle: –
		Author: Jonathan Noack
		Link: –

// 13.5.2019
