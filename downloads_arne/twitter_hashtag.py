# Zuerst muessen wir Twython importieren.
from twython import Twython, TwythonError

# Authentifizierung mit Twitter. Twitter API credentials. Sind auf der Twitter Developer Seite zu finden, wo ihr Euren Account gemacht habt.
twitter = Twython('eNzGxqtNGa7OKlUNgTwagQN1K', 'SHVEUvhtvb6WsezK4x8O4RHZeUchePEdjwKftWl1fNvTBhXS1J')
# Starte die Twittersuche nach @borussia
search_results = twitter.search(q='#bahamas', count=100000)
# Speichere die Ergebnisse in das Dictionary all_tweets
all_tweets = search_results['statuses']
# Ausgabe des Dictionaries in einer Schleife
for tweet in all_tweets:
    print (tweet['text'])
