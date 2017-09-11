import tweepy
import time

key1 = "******************"
key2 = "******************"
key3 = "******************"
key4 = "******************"

accountvar = raw_input("Account name: ")

auth = tweepy.OAuthHandler(key1, key2)
auth.set_access_token(key3, key4)

api = tweepy.API(auth)

users = tweepy.Cursor(api.followers, screen_name=accountvar).items()

while True:
    try:
        user = next(users)
    except tweepy.TweepError:
        time.sleep(60*15)
        user = next(users)
    except StopIteration:
        break
    print "@" + user.screen_name
