import tweepy
from local import key

auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)

auth.set_access_token(key.access_token, key.access_token_secret)

api = tweepy.API(auth)





if __name__ == '__main__':
    for tweet in public_tweets:
        print tweet.text