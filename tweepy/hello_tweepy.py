import tweepy

client = tweepy.Client('')

query = 'bbb22'

# tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], expansions='author_id', max_results=10)

# users = {u["id"]: u for u in tweets.includes['users']}

# for tweet in tweets.data:
#     print("- %s" % tweet.text)
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                              tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=100000):
    print("- %s" % tweet.text)
