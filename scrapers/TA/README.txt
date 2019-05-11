## Der Ordner TA enthält alle Skripte im Bezug auf das Price Scraping auf Tripadvisor:


## Generelle Information:
- Die Idee ist es, nicht nur Preise für einzelne Hotels zu scrapen sondern diese mit einer Kontrollgruppe zu vergleichen
  Aus diesem Grund, gibt es einige Skripte sowie Input-Files mehrfach.

!!! Wichtig: zur Zeit gibt es ein strukturelles Problem mit der Kontrollgruppe, da nicht zuverlässig die selben 30 Hotels über den
    Zeitraum gescrapt werden. Dateien und Skripte welche mit Kontrolle bezeichnet sind dienen dazu dieses Problem zu umgehen (WORK IN PROGRESS)

## Input-Files:
- city.txt = 
			Dies ist der Input für script.py. Beim Input handelt es sich um den Namen einer Stadt, für die Hotel-Preise gescrapt werden sollen.

- city_1.Run.txt (Archiv) = 
			Gleiches Dokument wie city.txt, welches für den 1. Run genutzt wurde.

- urls.txt = 
			Dies ist der Input für script_singlehotel.py. Beim Input handelt es sich um den Tripadvisor-URL eines bestimmten Hotels für welches die Übernachtungspreise gescrapt werden.

- urls_1.Run.txt (Archiv) = 
			Gleiches Dokument wie urls.txt, welches für den 1. Run genutzt wurde.

- urls_Kontrolle.txt = 
			Dies ist der Input für script_Kontrolle.py. Beim Input handelt es sich um die Kontrollgruppe der Hotels aus urls.txt. Das Dokument enthält Tripadvisor-URL bestimmter Hotels für welche die Übernachtungspreise gescrapt werden.

(- us-cities.txt = hier handelt es sich um ein test input file.)


## Python-Skripte:
- script.py = 
			Zweck: Dieses Skript führt das Price-Scraping für 30 Hotels aus gewissen Regionen aus.
			Input: city.txt mit den Regionen  
			Ausgeführte Funktionen: tripadvisor_scraper.py 			
			Output: CSV-Datei mit Preisen der Hotels
			Speicherort Output: ~/hotelierchallenge/scrapers/TA/Scrapes/Region

- script_singlehotel.py =
			Zweck: Dieses Skript führt das Price-Scraping für 1 Hotel aus.
			Input: urls.txt mit den TripAdvisor-Urls der einzelnen Hotels
			Ausgeführte Funktionen: tripadvisor_scraper_spechotel.py
			Output: CSV-Datei mit Preisen der einzelnen Hotels
			Speicherort Output: ~/hotelierchallenge/scrapers/TA/Scrapes/spechotel

- script_Kontrolle.py = 
			Zweck: Dieses Skript führt das Price-Scraping für 5 Hotels aus der Kontrollgruppe aus.
			Input: urls_Kontrolle.txt mit den TripAdvisor-Urls der einzelnen Hotels der Kontrollgruppe
			Ausgeführte Funktionen: tripadvisor_scraper_spechotel_Kontrolle.py
			Output: CSV-Datei mit Preisen der einzelnen Hotels aus der Kontrollgruppe
			Speicherort Output: ~/hotelierchallenge/scrapers/TA/Scrapes/Kontrolle

- cleanrows.py =
			Zweck: Diese Skript bereinigt die CSV-Outputdateien zu Weiterverarbeitung 
			Input: CSV-Dateien von script_singlehotel.py
			Output: Bereinigte Daten
			Speicherort Output: ~/hotelierchallenge/scrapers/TA/Scrapes/...


## Ausgabedateien:
- Die CSV Ausgabedateien werden in den Unterordnern des Ordners "Scrapes" abgespeichert.
		    	Ordner Region: enthält die gescrapten Preise der Kontrollgruppen-Hotels
    			Ordner spechotel: enthält die gescrapten Preise der einzelnen Hotels
			Ordner Kontrolle: enthält die gescrapten Preise der Kontrollgruppe

## Aktuellste Anpassungen:
- Veränderung der CSV Ausgaben (script.py, script_singlehotel.py und script_singlehotel_Kontrolle.py) sodass nur für die Datenbereinigung und -visualisierung benötigte Angaben ausgegeben werden.


// 11.5.2019
