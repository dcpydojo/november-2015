import tweepy

consumer_key = input("Consumer key: ")
consumer_secret = input("Consumer secret: ")
access_token = input("Access token: ")
access_secret = input("Access secret: ")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

out = []
for i in range(0, 200):
  trumps = api.user_timeline("realDonaldTrump", page = i)
  print(trumps[1].text.encode('utf-8'))
  out.extend(trumps)

tweets = []
for tweet in out:
  tweets.append(tweet.text.encode('utf-8'))

with open('trump_tweets.csv', 'w', newline = '') as csvfile:
    outfile = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
    for row in tweets:
      outfile.writerow(row)
