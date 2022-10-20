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


# Get tweets from screen name
def get_tweets_from_screen_name(name: str, results_per_page: int, total_results: int):
    twitter_id = api.get_user(screen_name=name).id_str
    tweets = tweepy.Paginator(client.get_users_tweets, twitter_id, max_results=results_per_page).flatten(total_results)
    return tweets


# Function for taking tweepy objects and making tweet lists 
def make_tweet_list(tweets_object):
    def convert_score(score):
        if score > 0:
            score_str = 'positive'
        elif score < 0:
            score_str = 'negative'
        else:
            score_str = 'neutral'

        return score_str

    user_tweet_list = []
    compiled_tweet_text = ""
    for t in tweets_object:
        tweet_score = sentiment_analyzer_scores(t.text)
        str_score = convert_score(tweet_score)

        user_tweet_list.append({
            'id': t.id,
            'text': t.text,
            'score': tweet_score,
            'score_str': str_score
        })

        if 'https://t.co' not in t.text:
            compiled_tweet_text += t.text

    #print(user_tweet_list, compiled_tweet_text)
    return {"user_tweet_list": user_tweet_list, "compiled_tweet_text": compiled_tweet_text}


# Question 2
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

# Question 3
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
        'tweet_count': follower.public_metrics['tweet_count'] or 0,
        # 'like_count': follower.public_metrics['like_count'] or 0
        # It doesn't looks like favorites/ likes is available anymore?
    })

# print(f"followers list length={len(followers_list)}")
followers_list_df = pd.DataFrame(followers_list)

print(followers_list_df.shape, "\n", followers_list_df.head())
print(followers_list_df)

# elon_id = api.get_user(screen_name='elonmusk').id_str
# elons_tweets = tweepy.Paginator(client.get_users_tweets, elon_id, max_results=100).flatten(400)

# Question 4
elons_tweets = get_tweets_from_screen_name('elonmusk', 100, 400)
elons_tweets_list, elons_tweets_compiled = make_tweet_list(elons_tweets).values()


elon_wordcloud = WordCloud(max_words=20).generate_from_text(elons_tweets_compiled)
plt.imshow(elon_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# print(elons_tweets_list[0], elons_tweets_list[0].get('score_str'))
elons_tweets_df = pd.DataFrame(elons_tweets_list)
# print(elons_tweets_df.head())
# print(elons_tweets_df['score_str'])

plt.figure(figsize=(10, 8))
sns.set(style="darkgrid")
sns.countplot(x=elons_tweets_df['score_str'], order=['positive', 'neutral', 'negative']).set_title('Musk Sentiment',
                                                                                                   fontsize=28)
plt.show()

# Question 5
tcs_tweets = get_tweets_from_screen_name('tim_cook', 100, 200)
tcs_tweet_list = make_tweet_list(tcs_tweets)['user_tweet_list']
print(tcs_tweet_list)

for tweet in tcs_tweet_list:
    t_id = tweet['id']
    print(t_id, tweet['id'], type(tweet['id']))
    liking_users = tweepy.Paginator(client.get_liking_users, t_id, max_results=100).flatten(400)
    count = 0
    for user in liking_users:
        count += 1

    print(count)
