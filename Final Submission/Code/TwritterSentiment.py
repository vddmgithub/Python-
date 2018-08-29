import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import codecs
from string import punctuation
from textblob import TextBlob

"""
This class is responsible for Listening to the tweets and prints out Sentiment using TextBlob module
"""
class TweetListener(StreamListener):
    api = 0
    search_words_list = []
    sentiment = dict()

    """
    This is to authenticate that is required for using Twitter Account
    """
    def authenticate(self):
        global api
        consumer_key = 'ZkIxjbsPacixuhTg7aclkQ'
        consumer_secret = 'yme0jG3UDhG0CFgqlc50UQFSspo3EkUfPziUf2FFo'
        access_token = '1635433267-29ZpqtvpBIzVOQTnz1wgCsaotyEBTgs4V4jkUEM'
        access_secret = '33ZEGzs7pR1M0AYnD0mwOaZJ8JIF1Nc183VOFNkeug'
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        #Get API handler for Twitter
        api = tweepy.API(auth)

    """
    API which uses TextBlob to print out the sentiment analyis
    """
    def tweetsAnalytics(self):
        self.authenticate()
        # auth.set_access_token(access_token, access_secret)
        # print search_words_list
        global api
        for celebrity in TweetListener.search_words_list:
            tweetsLists = api.search(celebrity)

            for tweets in tweetsLists:
                analysis = TextBlob(tweets.text)

            TweetListener.sentiment[celebrity] = celebrity,analysis.sentiment
            print("Overall sentiment of  ",celebrity,analysis.sentiment)

    """
    Setter method for list of professional for whom Sentiment Analysis needs to be performed.
    """
    def setCelebrityList(self, celebList):
        for item in celebList:
            TweetListener.search_words_list.append(item)

    @staticmethod
    def getSentiment(user):
        return TweetListener.sentiment[user]

"""
Sentimental Analysis based on rudimentary word count
"""


class SentimentAnalysisWC():
    search_words_list = []
    sentiment = dict()

    """
    Setter method for list of professional for whom Sentiment Analysis needs to be performed.
    """
    def setCelebrityList(this, celebList):
        for item in celebList:
            SentimentAnalysisWC.search_words_list.append(item)

    """
    API which does the core of sentiment analysis based on WordCount
    """

    def searchAndAnalyzeTweets(self):
        global search_words_list, counter, auth, indiv, outfile, file2, plt, access
        consumer_key = 'ZkIxjbsPacixuhTg7aclkQ'
        consumer_secret = 'yme0jG3UDhG0CFgqlc50UQFSspo3EkUfPziUf2FFo'
        access_token = '1635433267-29ZpqtvpBIzVOQTnz1wgCsaotyEBTgs4V4jkUEM'
        access_secret = '33ZEGzs7pR1M0AYnD0mwOaZJ8JIF1Nc183VOFNkeug'
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        api = tweepy.API(auth)

        # auth.set_access_token(access_token, access_secret)
        # print search_words_list
        for indiv in SentimentAnalysisWC.search_words_list:
            # indiv = indiv.split()
            print("Search Word - " + indiv + " - is being processed")
            counter = 0
            file2 = "Test_" + str(indiv) + ".txt"

            with codecs.open(file2, 'w', "utf-8") as outfile:
            #outfile = codecs.open(file2, 'w', "utf-8")
                tweetsLists = api.search(indiv)

                for tweets in tweetsLists:
                    outfile.write(tweets.text)

            self.sentiment_analysis()


    def sentiment_analysis(self):
        global file2, indiv, outfile, labels, colors, all_figs
        pos_sent = open("positive_words.txt").read()
        positive_words = pos_sent.split('\n')
        positive_counts = []
        neg_sent = open('negative_words.txt').read()
        negative_words = neg_sent.split('\n')
        #outfile.close()
        negative_counts = []
        conclusion = []

        tweets_list = []
        tot_pos = 0
        tot_neu = 0
        tot_neg = 0
        all_total = 0
        # print file2
        tweets = codecs.open(file2, 'r', "utf-8").read()
        tweet_list_dup = []

        tweets_list = tweets.split('\n')
        # print tweets_list

        for tweet in tweets_list:
            positive_counter = 0
            negative_counter = 0
            tweet = tweet.encode("utf-8")
            tweet = str(tweet)
            tweet_list_dup.append(tweet)
            tweet_processed = tweet.lower()

            for p in list(punctuation):
                tweet_processed = tweet_processed.replace(p, '')

            words = tweet_processed.split(' ')
            word_count = len(words)
            for word in words:
                if word in positive_words:
                    positive_counter = positive_counter + 1
                elif word in negative_words:
                    negative_counter = negative_counter + 1

            positive_counts.append(positive_counter)
            negative_counts.append(negative_counter)
            if positive_counter > negative_counter:
                conclusion.append("Positive")
                tot_pos += 1
            elif positive_counter == negative_counter:
                conclusion.append("Neutral")
                tot_neu += 0.5
            else:
                conclusion.append("Negative")
                tot_neg += 1

        # print len(positive_counts)
        output = zip(tweet_list_dup, positive_counts, negative_counts, conclusion)
        # output = output.encode('utf-8')

        #print("******** Overall Analysis **************")

        if tot_pos > tot_neg and tot_pos > tot_neu:
            #print("Overall Sentiment - Positive")
            SentimentAnalysisWC.sentiment[indiv]=  "Positive"
        elif tot_neg > tot_pos and tot_neg > tot_neu:
            #print("Overall Sentiment - Negative")
            SentimentAnalysisWC.sentiment[indiv] = "Negative"
        elif tot_neg == tot_neu and tot_neg > tot_pos:
            #print("Overall Sentiment - Negative")
            SentimentAnalysisWC.sentiment[indiv] = "Negative"
        elif tot_pos + tot_neg < tot_neu:
            #print("Overall Sentiment - Semi Positive ")
            SentimentAnalysisWC.sentiment[indiv] = "Semi Positive"
        else:
            #print("Overall Sentiment - Neutral")
            SentimentAnalysisWC.sentiment[indiv] = "Neutral"

        #print("%%%%%%%%%%%% End of stream - " + indiv + "   %%%%%%%%%%%%%%%%%%%%%")

    @staticmethod
    def getSentiment(user):
        return SentimentAnalysisWC.sentiment[user]


def main():
    twitterHandler =  TweetListener()
    twitterHandler.authenticate()
    gods = ["Sathya Sai Baba", "Jesus"]
    twitterHandler.setCelebrityList(gods)
    twitterHandler.search_tweets()

#main()
