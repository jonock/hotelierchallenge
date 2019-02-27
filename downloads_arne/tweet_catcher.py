#!/usr/bin/env python
# encoding: utf-8
# PEP 263 -- Defining Python Source Code Encodings (Zielen davor nicht veraendern)

# Der folgende Skript basiert auf https://gist.github.com/yanofsky/5436496
# Welche Moelgichkeiten bietet die Twitter API http://docs.tweepy.org/en/v3.5.0/api.html#timeline-methods
# Bitte orientiert Euch fuer Anpassung an der Tweepy Dokumentation
# Dieser Code ist in Python 2.x geschrieben, daher muessen wir eine virtuelle Umgebung im Conda Navigator starten
# Zuerst muessen wir Tweepy importieren.
import tweepy # https://github.com/tweepy/tweepy
# Da wir den Output als Excel/csv Datei speichern wollen, importieren wir auch CSV
import csv

# Authentifizierung mit Twitter. Twitter API credentials. Sind auf der Twitter Developer Seite zu finden, wo ihr Euren Account gemacht habt.
consumer_key = "BuUVoZdKrZNF4yr2GE9a8osXd"
consumer_secret = "BTcNmcyesymsuz7Bvmzo7pTCwmSpzZempBrMs7sPKQo6viOJq9"
access_key = "1069878781110902784-1dMJjWSW0EzVpEusQSQhv5YhWadfrU"
access_secret = "oGy6RmMBSRQuVf2LBvHpYTfQVixcBkRVBGiaUOPtzqYlr"


def get_all_tweets(screen_name):
	# Twitter erlaubt es nur die letzten 3240 Tweets von einem User zu crawlen

	# Authentifizierung mit Twitter, Initialisierung Twitter
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	# Initialisieren einer leeren Liste, um alle Tweepy Tweets zu speichern.
	alltweets = []

	# Sende erste Anfrage für die neuesten Tweets stellen (200 ist die maximal zulässige Anzahl)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)

	# Speichern der Tweets in die oben erstellte Liste
	alltweets.extend(new_tweets)

	# Speichert die ID des ältesten Tweets weniger als einen.
	oldest = alltweets[-1].id - 1

	# Schleife: Tweets so lange sammeln, bis keine Tweets mehr zum Sammeln übrig sind.
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)

		# Alle subsiquenten Anfragen verwenden den max_id-Param, um Duplikate zu vermeiden.
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		# Speichern der neuesten Tweets
		alltweets.extend(new_tweets)

		# Aktualisieren der ID des ältesten Tweets weniger eines Tweets
		oldest = alltweets[-1].id - 1

		print "...%s tweets downloaded so far" % (len(alltweets))

	# Umwanndeln der Tweets in ein Array, damit wir es als csv ausgeben lassen koennen
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

	# Oeffnen und schreiben in die CSV Datei
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)

	pass


if __name__ == '__main__':
	# Hier muss der Username des Accounts eingegeben werden
	get_all_tweets("Arne85420832")
