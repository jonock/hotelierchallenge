########                                    ########
########  Hotel Influencer Twitter Script   ########
########          19 March 2019             ########
########____________________________________########

### Description
### This script write a csv with tweets containing the given hashtags
### and adds info regarding followers count and retweets etc.


###Issues / Improvements:
    #amount of tweets is not ideal,
    #sort csv to show highest potential influencer first
    #show media url, issue with tweet.entities
    #filter out RTs



import tweepy
import csv
import operator
import datetime
from datetime import date, timedelta

# Authentifizierung mit Twitter
consumer_key = 'E7QiU0rxmcOTzU1BtBHmTwdqo'
consumer_secret = 'Wpq0iapw4mdgnuAbuRcTjUrAhCq2WUh9TEADj27JjUsnzPWPhy'
access_token = '17225770-a7eDWlIh9FbzcMeU0yawwfXo2gA5t6yJV5hzovefn'
access_token_secret = '6AvyV8iIcIvDmqCdPA3YtAsSw2nOx7EXV84bTy7XglHsA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# die Gross- /Kleinschreibung muss nicht berücksichtigt werden
hashtag = "#hotel OR #resort"

#date input for csv.writer and tweepy.cursor
today = datetime.datetime.now()
todaysdate = today.strftime("%y%m%d%H")
yesterday = date.today() - timedelta(1)
yesterdaysdate = yesterday.strftime("%Y-%m-%d")

#write CSV File
filename = todaysdate
csvFile = open('Exports/%s_influencer_hotelposts.csv' % filename, 'a')
csvWriter = csv.writer(csvFile)
#write CSV Headers
csvWriter.writerow (["TweetID", "Date", "User", "Followers", "Retweets","Favorites"])

#search for tweets with query = hashtag and a few other parameters, count in items
for tweet in tweepy.Cursor(api.search, show_user = True, q = hashtag,lang="en", since=yesterdaysdate).items(2000):
    #read metadata of tweets from JSON
    tweetinfo = (tweet.id_str,
                 tweet.created_at,
                 tweet.user.screen_name,
                 tweet.user.followers_count,
                 tweet.retweet_count,
                 tweet.favorite_count)
    print (tweetinfo)
    #write tweet-details in csv
    csvWriter.writerows ([tweetinfo])


print("Script is done - Influencer CSV is ready")

#tweet.text.encode('utf-8')])
