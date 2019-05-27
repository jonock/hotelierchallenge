# Der Ordner Influencer_Screening enthält alle Skripte im Bezug auf das Hotel-Post Monitoring auf Twitter

## Input-Files:

## Python-Skripte.
- InflScreeningcsv.py =
		Zweck: Das Skript sucht Posts anhand von Hashtags auf Twitter
		Input: Hashtags (#hotel; #resort)
		Ausgeführte Funktionen: –
		Output: CSV-Datei mit den Posts pro Hashtag
		Speicherort Output: ~/hotelierchallenge/Twitter_Scripts/Influencer_Screening/Exports

=> Die Datei beinhaltet den Tweet ID, Zeitpunkt des Posts, User-Name, Anzahl Follower des Users, Anzahl Retweets, Anzahl Likes.

Der Name der CSV-Dateien ist wie folgt zu verstehen:

Bspw.: 19032110, Export wurde um 10 Uhr am 21.3.19 getätigt

Mit folgendem Link kann der Tweet mittels TweetId in der CSV aufgerufen werden:

https://twitter.com/anyuser/status/ID      --> Einfügen der Tweet ID anstelle von "ID"
Bspw.: https://twitter.com/anyuser/status/1109407634686398465

Folgende Skripte wurden verwendet um die stündlichen Scrapes zu bereinigen und Duplikate zu entfernen:
- influencers_cleandata.py =
		Zweck: nicht verwendete Daten entfernen, alle Dateien zu einer Datei konsolidieren
- removeduplicates.py =
		Zweck: Duplikate entfernen 1. TweetID (entfernt duplikate Tweets) und 2. User (reduziert Tweets auf einen per Users)


## Quellen:
- InflScreeningcsv.py =
		Quelle: Vickyqian
		Author: Tobias Rordorf
		Link: Skript in Anlehnung an https://gist.github.com/vickyqian/f70e9ab3910c7c290d9d715491cde44c
