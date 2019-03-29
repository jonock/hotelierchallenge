Der Ordner insta_selenium enthält das Skript im Bezug auf die Hashtag-Anzahl Scraping auf Instagram:

Input-Files:
- hashtaglist.txt = Dies ist der Input für script.py. Beim Input handelt es sich um eine Liste beliebiger Hashtags, für die die Anzahl gescrapt werden soll.

- Manuelle Abfrage = durch Anpassung des script.py können die Hashtags auch ohne Zusatzfile auf Abfrage hin direkt analysiert werden.

(- us-cities.txt = hier handelt es sich um ein test input file.)

Python-Skripte:
- script.py = Dieses Skript läuft mit Selenium und führt das Hashtag-Scraping für jeden beliebigen Hashtag aus und erstellt eine CSV-Datei mit den Anzahl gefundener Hashtags

=> die im Skript verwendeten Funktionen sind im folgenden .py File definiert:
	- hashtaghandler.py

Die CSV Ausgabedateien werden in den Unterordner des Ordners "Scrapes" abgespeichert.

// 29.3.2019
