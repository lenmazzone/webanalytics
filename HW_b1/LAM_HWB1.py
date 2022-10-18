import pandas as pd
import tweepy

consumer_key = "vVFYFJW5rMsSMZMvGcgFyq04O"
consumer_secret = "tthwgvgQFZSnqDIjLZNSomkthmwAK7ePjQZVfRGo59QKIRZqoZ"
access_key = "1355220096-VaSbSaAzCIqBBMNFPPEwlh0YdMpBVd3XNnV4InP"
access_secret = "NqCt5VpJLhdhY3uXKfOa82aBM3dfmoo7L8ZcI7GsUz3Yk"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAPDQiAEAAAAAzEHxOR5MHoAG4NWX%2Fw9eKC%2FuXGk%3DYwkvcIYApKLNMtcYxI7F4lFlFepajSPGE5RA8oiZBvc8Rlr8Eh"

# Setup access to API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# create the API object
api = tweepy.API(auth, wait_on_rate_limit=True)
client = tweepy.Client(bearer_token)
user_id = 981294161780510720

recent_tweets = api.user_timeline(screen_name='apo_filippas', count=100)

for i in range(10):
    print(recent_tweets[i].text)

tweet_list = []

for tweet in recent_tweets:
    tweet_list.append(
        {
            'id': tweet.id,
            'text': tweet.text,
            'created': tweet.created_at,
            'source': tweet.source,
            'retweets': tweet.retweet_count or 0,
            'likes': tweet.favorite_count or 0

        }
    )

# print(tweet_list)

tweet_list_df = pd.DataFrame(tweet_list)
print(tweet_list_df.shape, "\n", tweet_list_df.head())

# followers = tweepy.Cursor(api.get_followers, screen_name='apo_filippas', count=200 ).items(200)
followers = client.get_users_followers(user_id, user_fields=['location', 'description', 'url', 'public_metrics'],
                                       max_results=1000)
print(followers[0])
followers_list = []
# for follower in followers:
#     followers_list.append({
#         'id': follower.id,
#         'name': follower.name,
#         'screen_name': follower.screen_name,
#         'location': follower.location,
#         'description': follower.description,
#         'profile_url': follower.url,
#         'followers_count': follower.followers_count or 0,
#         'followee_count': follower.friends_count or 0,
#         'favourites_count': follower.favourites_count or 0
#     })
#
# print(f"followers list length={len(followers_list)}")
# followers_list_df = pd.DataFrame(followers_list)
#
# print(followers_list_df.shape, "\n", followers_list_df.head())
# print(followers_list_df)
