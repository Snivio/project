import tweepy  # https://github.com/tweepy/tweepy
from textblob import TextBlob
import re

# Twitter API credentials
consumer_key = '*******************'
consumer_secret = '*******************'
access_key = '*******************'
access_secret = '*******************'


def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1


    for tweet in alltweets:
        result = re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet.text.encode("utf-8"))
        analysis = TextBlob(result)
        if analysis.sentiment.polarity > 0:
             print tweet.id_str, "\n", tweet.created_at, "\n",result
        else:
            print "normal"

    pass


if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("Razer")

