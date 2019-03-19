########                                    ########
########  Hotel Influencer Twitter Script   ########
########          19 March 2019             ########
########________________T.R.________________########

### Description
### This script write a csv with tweets containing the given hashtags
### and adds info regarding followers count and retweets etc.


###Issues / Improvements:
    #amount of tweets is not ideal,
    #sort csv to show highest potential influencer first



import tweepy
import csv
import operator

# Authentifizierung mit Twitter
consumer_key = 'abc'
consumer_secret = 'abc'
access_token = 'abc'
access_token_secret = 'abc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# die Gross- /Kleinschreibung muss nicht berücksichtigt werden
hashtag = "#hotel OR #resort"

#write CSV File
filename = "influencer"
csvFile = open('%s_hotelposts.csv' % filename, 'a')
csvWriter = csv.writer(csvFile)
#write CSV Headers
csvWriter.writerow (["TweetID", "Date", "User", "Followers", "Retweets","Favorites"])

#search for tweets with query = hashtag and a few other parameters, count in items
for tweet in tweepy.Cursor(api.search, show_user = True, q = hashtag,lang="en", since="2019-03-19").items(1000):
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
