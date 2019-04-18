## Der Ordner TA enthält alle Skripte im Bezug auf das Price Scraping auf Tripadvisor:

## Generelle Information:
- Die Idee ist es, nicht nur Preise für einzelne Hotels zu scrapen sondern diese mit einer Kontrollgruppe zu vergleichen
  Aus diesem Grund, gibt es einige Skripte sowie Input-Files mehrfach.

!!! Wichtig: zur Zeit gibt es ein strukturelles Problem mit der Kontrollgruppe, da nicht zuverlässig die selben 30 Hotels über den
    Zeitraum gescrapt werden. Dateien und Skripte welche mit Kontrolle bezeichnet sind dienen dazu dieses Problem zu umgehen (WORK IN PROGRESS)

## Input-Files:
- city.txt = Dies ist der Input für script.py. Beim Input handelt es sich um den Namen einer Stadt,
  für die Hotel-Preise gescrapt werden sollen.

- urls.txt = Dies ist der Input für script_singlehotel.py. Beim Input handelt es sich um den Tripadvisor-URL
  eines bestimmten Hotels für welches die Übernachtungspreise gescrapt werden.

(- us-cities.txt = hier handelt es sich um ein test input file.)


## Python-Skripte:
- script.py = Dieses Skript führt das Price-Scraping für 30 Hotels aus (Input = city.txt) und erstellt eine CSV-Datei mit den Preisen

- script_singlehotel.py = Dieses Skript führt das Price-Scraping für 1 Hotel aus (Input = urls.txt) und erstellt eine CSV-Datei mit den Preisen

- cleanrows.py (im Unterordner scrapes/1.Run): bereinigt die CSV-Outputs aus script_singlehotel.py zur weiteren Datenverarbeitung

=> die in beiden Skripten verwendeten Funktionen sind in folgenden .py Files definiert:
   - tripadvisor_scraper_spechotel.py &
   - tripadvisor_scraper.py

## Ausgabedateien:
- Die CSV Ausgabedateien werden in den Unterordnern des Ordners "Scrapes" abgespeichert.
    - Ordner Region: enthält die gescrapten Preise der Kontrollgruppen-Hotels
    - Ordner spechotel: enthält die gescrapten Preise der einzelnen Hotels

## Aktuellste Anpassungen: 
- Veränderung der CSV Ausgaben (script.py und script_singlehotel.py) sodass nur für die
  Datenbereinigung und -visualisierung benötigte Angaben ausgegeben werden.

## Archiv:
- city_1.Run.txt => dies ist das Input-File des ersten Testlaufs (mehrere Hotels für Kontrollgruppe)
- ursl_1.Run.txt => dies ist das Input-File des ersten Testlaufs (einzelne Hotels)


// 18.4.2019
