#coding utf-8
import snscrape.modules.twitter as sntwitter
import pandas

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('homofóbico since:2018-10-01 until:2018-11-01').get_items()):
    if i>100000:
        break
    # tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username]) #declare the attributes to be returned
    if tweet.lang == "pt":
      print("-\n %s \n Idioma: %s" % (tweet.content, tweet.lang))  
# Creating a dataframe from the tweets list above 
# tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])