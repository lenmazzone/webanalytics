import pandas as pd
import seaborn as sns
import tweepy
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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


# define a function to calculate the sentiment score for each tweet
def sentiment_analyzer_scores(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    return score['compound']


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

# followers = api.get_followers(screen_name='apo_filippas', count=200, cursor=20)
followers = client.get_users_following(user_id, user_fields=['id', 'name', 'username', 'location', 'description', 'url',
                                                             'public_metrics'],
                                       max_results=1000)

followers_list = []
# print(followers.data[0].public_metrics)
for follower in followers.data:
    followers_list.append({
        'id': follower.id,
        'name': follower.name,
        'screen_name': follower.username,
        'location': follower.location,
        'description': follower.description,
        'profile_url': follower.url,
        'followers_count': follower.public_metrics['followers_count'] or 0,
        'followee_count': follower.public_metrics['following_count'] or 0,
        'tweet_count': follower.public_metrics['tweet_count'] or 0
        # It doesn't looks like favorites/ likes is available anymore?
    })

# print(f"followers list length={len(followers_list)}")
followers_list_df = pd.DataFrame(followers_list)

print(followers_list_df.shape, "\n", followers_list_df.head())
print(followers_list_df)

elon_id = api.get_user(screen_name='elonmusk').id_str
elons_tweets = tweepy.Paginator(client.get_users_tweets, elon_id, max_results=100).flatten(400)
# print(elons_tweets)

elons_tweets_compiled = ""
elons_tweets_list = []

for tweet in elons_tweets:
    score = sentiment_analyzer_scores(tweet.text)
    score_str = ''

    if score > 0:
        score_str = 'positive'
    elif score < 0:
        score_str = 'negative'
    else:
        score_str = 'neutral'

    elons_tweets_list.append({
        'id': tweet.id,
        'text': tweet.text,
        'score': score,
        'score_str': score_str
    })

    if 'https://t.co' not in tweet.text:
        elons_tweets_compiled += tweet.text

print(elons_tweets_compiled)

elon_wordcloud = WordCloud(max_words=20).generate_from_text(elons_tweets_compiled)
plt.imshow(elon_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

print(elons_tweets_list[0])

plt.figure(figsize=(10, 8))
sns.set(style="darkgrid")
sns.countplot(x=elons_tweets_list, order=['positive', 'neutral', 'negative']).set_title('Musk Sentiment', fontsize=28)