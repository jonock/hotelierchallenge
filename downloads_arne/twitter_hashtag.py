# Zuerst muessen wir Twython importieren.
from twython import Twython, TwythonError

# Authentifizierung mit Twitter. Twitter API credentials. Sind auf der Twitter Developer Seite zu finden, wo ihr Euren Account gemacht habt.
twitter = Twython('jNoyds3dIvolZmuwvKLl0lRI0', 'VZ7EawnfdNdWNx55h8qieiesjoOLBaQxE1lXs8qmFWVL0aiXJJ')
# Starte die Twittersuche nach @borussia
search_results = twitter.search(q='@HSGStGallen', count=50)
# Speichere die Ergebnisse in das Dictionary all_tweets
all_tweets = search_results['statuses']
# Ausgabe des Dictionaries in einer Schleife
for tweet in all_tweets:
    print (tweet['text'])
