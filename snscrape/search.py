# coding utf-8
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to

tweets_list1 = []

total = 0

total_portugues = 0

palavras = ["#FUZILARGAYS"]

# palavras = ["baitola", "bichona", "bixa", "boiola", "gayzada",
#             "gayzismo", "homossexualismo", "viadagem", "viadao", "viadinho", "bicha"]

for p in palavras:
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(p + ' since:2018-09-01 until:2018-11-01').get_items()):
        if i > 100000:
            break
        total += 1
        # tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
        #  #declare the attributes to be returned
        if tweet.lang == "pt":
            total_portugues += 1
            # print("-\n %s \n Idioma: %s" % (tweet.content, tweet.lang))
            tweets_list1.append([tweet.date, tweet.id, tweet.content,
                                tweet.user.username, tweet.lang, p, tweet.user.description,
                                tweet.user.rawDescription, tweet.user.friendsCount, tweet.user.statusesCount,
                                tweet.retweetedTweet, tweet.quotedTweet])
    print("O total de tweets com a palavra " + p + " foi %i" % total)
    print("O total de tweets em português com a palavra " +
          p + " foi %i" % total_portugues)

# Using TwitterSearchScraper to scrape data and append tweets to list


# Creating a dataframe from the tweets list above
tweets_df1 = pd.DataFrame(tweets_list1, columns=[
                          'Datetime', 'TweetId', 'Texto', 'Username', 'Idioma', 'Palavra',
                          'UserDescription', 'UserDescriptionRaw', 'FriendsCount', 'Status', 'Retweet', 'Quoted'])

tweets_df1.to_csv("./coleta-fuzilagays.csv")
