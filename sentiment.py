import tweepy
from textblob import textblob


consumer_key='iA8XtD33RyfySXETKfFROVqvB'
consumar_secret='sD4e0oISB2XEBpEQWtt5oJRxDYtbRQWPj4vaPW9VUmOWxKjfFv '

access_token ='382441070-gMoVwamM2RaM6MWL0io3FWRPPM5hJZxHkgePYfs3 '
access_token_secret='GAsrYUfTuKkHZH25CIg35JQwYgYvefzazBdeeQ7x81dku'

auth=tweepy.OAuthHandler(consumer_key,consumar_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


public_tweets=api.search('Modi')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)