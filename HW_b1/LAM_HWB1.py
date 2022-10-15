import tweepy

consumer_key = "vVFYFJW5rMsSMZMvGcgFyq04O"
consumer_secret = "tthwgvgQFZSnqDIjLZNSomkthmwAK7ePjQZVfRGo59QKIRZqoZ"
access_key = "1355220096-VaSbSaAzCIqBBMNFPPEwlh0YdMpBVd3XNnV4InP"
access_secret = "NqCt5VpJLhdhY3uXKfOa82aBM3dfmoo7L8ZcI7GsUz3Yk"

# Setup access to API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# create the API object
api = tweepy.API(auth)

recent_tweets = api.home_timeline(count=5)
for tweet in recent_tweets:
    print(tweet.text)
