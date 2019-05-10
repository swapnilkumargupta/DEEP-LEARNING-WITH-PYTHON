import tweepy
from textblob import textblob


consumer_key='C_K'
consumar_secret='C_S'

access_token ='A_T'
access_token_secret='_T_S'

auth=tweepy.OAuthHandler(consumer_key,consumar_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


public_tweets=api.search('Modi')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
