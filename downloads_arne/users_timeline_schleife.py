# Zuerst muessen wir Twython importieren.
from twython import Twython
# Authentifizierung mit Twitter. Hier speichern wir die Tokens erst in Variablen ab, die dann uebergeben werden.
APP_KEY = 'jNoyds3dIvolZmuwvKLl0lRI0'
APP_SECRET = 'VZ7EawnfdNdWNx55h8qieiesjoOLBaQxE1lXs8qmFWVL0aiXJJ'
# Senden der Authentifizierung
twitter = Twython(APP_KEY, APP_SECRET)
# Ueberpruefung, ob wir wirklich authentifiziert wurden
try:
    user_tweets = twitter.get_user_timeline(screen_name='Arne85420832', include_rts=True)
    for tweet in user_tweets:
        tweet['text'] = Twython.html_for_tweet(tweet)
        print(tweet['text'])

except TwythonError as e:
    print (e)
