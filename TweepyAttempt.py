import praw
import tweepy
import json
from tweepy import Stream

def getEndIndex(tweet):
    endIndex = tweet.find(".")

    if endIndex == len(tweet) - 1:
        return endIndex
    elif (tweet[endIndex - 1].isdigit() and tweet[endIndex + 1].isdigit()):
        return endIndex + getEndIndex(tweet[endIndex + 1:]) + 1
    elif not(tweet[endIndex - 2: endIndex].lower().find("jr") == -1):
        return endIndex + getEndIndex(tweet[endIndex + 1:]) + 1
    else:
        return endIndex

auth = tweepy.OAuthHandler("EzUsddbekYsLz4benZe5Y8Qjh",
                           "JGDpkkQMQifdcrm5Ra4Cu0LoLlajDOHKRs2VYb7jq29TNNbSpi")
auth.set_access_token("615513817-SmZwmbz1YzZcRtI4Czo1j1sU2Cnx94xQcqKuZ8oc",
                      "GFJWJQ9XO9ssnRti1NQiVa6kWkuRdsYWHSi0CJ4So4S47")

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    auth1 = tweepy.OAuthHandler("BZ1mLujonEsiQ1nXHsQRL5qQQ",
                               "PeuWzllsoiXnQBxAgWLInNUM8BBY2I0eXQZ2yB2pIp59Fjt4Ul")
    auth1.set_access_token("615513817-1IxaVyxPfkxZ6jIO9CI89b4FJpSUYxUfw42iUZEH",
                          "aL5qn9629Q3kvCkWjRlKA6bYXwyTnKxaskTLMwsZvmBlI")

    #api1 = tweepy.API(auth1)
    def on_status(self, status, api1=tweepy.API(auth1)):
        self.stream = Stream(auth=api1.auth, listener=self, tweet_mode='extended')

        try:
            fulltweet = status.extended_tweet['full_text']

            endIndex = getEndIndex(fulltweet)
            if status.extended_tweet['full_text'].find("RT @") == -1 \
                    and status.extended_tweet['full_text'].find("@NYPost_Mets") == -1:
                print(status.extended_tweet['full_text'])
                reddit.subreddit("DebateWithStrawmen").submit(
                    title= "[Puma] "
                           + status.extended_tweet['full_text']
                        [0:endIndex + 1],
                    url="https://twitter.com/JordanSimkovic/status/"
                                                       + str(status.id))
            else:
                print("Caught retweet! The text was more than 140 chars and was: "
                      +  status.extended_tweet['full_text'])
        except:
            endIndex = getEndIndex(status.text)

            if status.text.find("RT @") == -1 and status.text.find("@NYPost_Mets") == -1:
                print(status.text)
                reddit.subreddit("DebateWithStrawmen").submit(
                    title="[Puma] "
                          + status.text[0:endIndex + 1]
                    , url="https://twitter.com/JordanSimkovic/status/"
                                                      + str(status.id))
            else:
                print("Caught retweet! The text was less than 140 chars and was: "
                      +  status.text)

myStreamListener = MyStreamListener()

def statusFollower():
    try:
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener, tweet_mode="extended")
        myStream.filter(follow=["615513817"])
    except:
        statusFollower()

reddit = praw.Reddit(client_id='jvTpt-_A6Y_oTA',
                     client_secret='lMkkD-4s2fPkxE9Kp--VrCEHoMI',
                     user_agent='Woj bot by u/mkgandkembafan',
                     username='mkgandkembafan',
                     password='Jkys1171998!?')



statusFollower()
