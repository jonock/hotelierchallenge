# Der folgende Skript basiert auf https://gist.github.com/vickyqian/f70e9ab3910c7c290d9d715491cde44c
# Welche Moelgichkeiten bietet die Twitter API http://docs.tweepy.org/en/v3.5.0/api.html#timeline-methods
import tweepy
import csv
import pandas as pd

# Authentifizierung mit Twitter. Twitter API credentials. Sind auf der Twitter Developer Seite zu finden, wo ihr Euren Account gemacht habt.
consumer_key = 'eNzGxqtNGa7OKlUNgTwagQN1K'
consumer_secret = 'VZ7EawnfdNdWNx55h8qieiesjoOLBaQxE1lXs8qmFWVL0aiXJJ'
access_token = '1100733514914451458-ssGNd28UDNCzGfJCzhy5YMz8o8enGC'
access_token_secret = 'VBnFJgXRyaW7bdsYr27QHCBzd6CD8arcEOCRxdSpLCpeJ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Hashtag hier eingeben
deinhashtag = "#borussia"

# Oeffnen und schreiben in die CSV Datei
csvFile = open('%s_hashtag.csv' % deinhashtag, 'a')
csvWriter = csv.writer(csvFile)
# Durchsuchen der API nach Hashtag, Sprache und Datum
for tweet in tweepy.Cursor(api.search,q = deinhashtag,count=1,
                           lang="de",
                           since="2018-01-11").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])


print('ERFOLG!!!!!!')
