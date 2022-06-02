#coding utf-8
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to

tweets_list1 = []

total = 0

total_portugues = 0

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('viado since:2018-10-06 until:2018-10-08').get_items()):
    if i > 100000:
        break
    total += 1
    # tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username]) #declare the attributes to be returned
    if tweet.lang == "pt":
        total_portugues += 1
        # print("-\n %s \n Idioma: %s" % (tweet.content, tweet.lang))
        tweets_list1.append([tweet.date, tweet.id, tweet.content,
                            tweet.user.username, tweet.lang])

print("O total de tweets foi %i" % total)
print("O total de tweets em português foi %i" % total_portugues)

# Creating a dataframe from the tweets list above 
tweets_df1 = pd.DataFrame(tweets_list1, columns=[
                          'Datetime', 'TweetId', 'Text', 'Username', 'Language'])

tweets_df1.to_csv("./word-viado.csv")
