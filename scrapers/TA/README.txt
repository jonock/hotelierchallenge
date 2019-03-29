Der Ordner TA enthält alle Skripte im Bezug auf das Price Scraping auf Tripadvisor:

Input-Files:
- city.txt = Dies ist der Input für script.py. Beim Input handelt es sich um den Namen einer Stadt,
  für die Hotel-Preise gescrapt werden sollen.

- urls.txt = Dies ist der Input für script_singlehotel.py. Beim Input handelt es sich um den Tripadvisor-URL
  eines bestimmten Hotels für welches die Übernachtungspreise gescrapt werden.

- us-cities.txt = hier handelt es sich um ein test input file.


Python-Skripte:
- script.py = Dieses Skript führt das Price-Scraping für 30 Hotels aus (Input = city.txt) und erstellt eine CSV-Datei mit den Preisen

- script_singlehotel.py = Dieses Skript führt das Price-Scraping für 1 Hotel aus (Input = urls.txt) und erstellt eine CSV-Datei mit den Preisen

=> die in beiden Skripten verwendeten Funktionen sind in folgenden .py Files enthalten:
   - tripadvisor_scraper_spechotel.py &
   - tripadvisor_scraper.py

Die CSV Ausgabedateien werden in den Unterordnern des Ordners "Scrapes" abgespeichert.



// 29.3.2019
