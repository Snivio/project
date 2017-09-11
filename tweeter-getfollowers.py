import tweepy
import time

key1 = "VSX6nhq60PKprHFwZdDr8H3Uj"
key2 = "ufYxF2mULObpMeVUPdTeT8Stg5409DWO75UQ9QvGaNg0QPVYc3"
key3 = "292170020-brwmXdVgn89cfAMj8m41lJSklNiHirxpKmjVj1iM"
key4 = "yIGQS8dB3CVRKsCqDNfnp16G1uFgsIKATj6ErUql2jy3l"

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
