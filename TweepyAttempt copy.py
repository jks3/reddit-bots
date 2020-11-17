import traceback

import praw
import tweepy
import time
import json
from tweepy import Stream

def getEndIndex(tweet, numOfQuotes):
    endIndex = tweet.find(".")

    numOfQuotes += tweet[0:endIndex + 1].count("\"")
    if endIndex == len(tweet) - 1:
        return endIndex
    elif endIndex == -1:
        return len(tweet) - 1
    elif (tweet[endIndex - 1].isdigit() and tweet[endIndex + 1].isdigit()):
        return endIndex + getEndIndex(tweet[endIndex + 1:], 0) + 1
    elif not(tweet[endIndex - 2: endIndex].lower().find("jr") == -1):
        return endIndex + getEndIndex(tweet[endIndex + 1:], 0) + 1
    elif (tweet[endIndex + 1:].count("\"") != 0):
        return endIndex + getEndIndex(tweet[endIndex + 1:], numOfQuotes) + 1
    else:
        return endIndex

auth = tweepy.OAuthHandler("QQudwo000fzahCOyDXHxSuuy8",
                           "6fJb3JbMp9MiM2Z9EUX3Fc7vJREqPSWzHzDR2kS2AHi797Frhp")
auth.set_access_token("615513817-KBbrJar0PY81rSOUCDwVuVLIHYdlJEkL9rmpv8V6",
                      "bQHcFwaoYastXquuWW294JKRqztaphCkngVm6TcTHDmVP")

api = tweepy.API(auth)

nameToSubreddit = {"Mavericks" : "Mavericks",
                   "Nuggets" : "denvernuggets",
                   "Warriors" : "warriors",
                   "Rockets" : "rockets",
                   "Clippers" : "LAClippers",
                   "Lakers" : "lakers",
                   "Grizzlies" : "memphisgrizzlies",
                   "Timberwolves" : "timberwolves",
                   "Pelicans" : "NOLAPelicans",
                   "Thunder" : "Thunder",
                   "Suns" : "suns",
                   "Trail Blazers" : "ripcity",
                   "Kings" : "kings",
                   "Spurs" : "NBASpurs",
                   "Jazz" : "UtahJazz",
                   "Hawks" : "AtlantaHawks",
                   "Celtics" : "bostonceltics",
                   "Nets" : "GoNets",
                   "Hornets" : "CharlotteHornets",
                   "Bulls" : "chicagobulls",
                   "Cavaliers" : "clevelandcavs",
                   "Pistons" : "DetroitPistons",
                   "Pacers" : "pacers",
                   "Heat" : "heat",
                   "Bucks" : "MkeBucks",
                   "Knicks" : "NYKnicks",
                   "Magic" : "OrlandoMagic",
                   "76ers" : "sixers",
                   "Sixers" : "sixers",
                   "Raptors" : "torontoraptors",
                   "Wizards" : "washingtonwizards"}

class MyStreamListener(tweepy.StreamListener):
    auth1 = tweepy.OAuthHandler("QQudwo000fzahCOyDXHxSuuy8",
                               "6fJb3JbMp9MiM2Z9EUX3Fc7vJREqPSWzHzDR2kS2AHi797Frhp")
    auth1.set_access_token("615513817-KBbrJar0PY81rSOUCDwVuVLIHYdlJEkL9rmpv8V6",
                          "bQHcFwaoYastXquuWW294JKRqztaphCkngVm6TcTHDmVP")

    #api1 = tweepy.API(auth1)
    def on_status(self, status, api1=tweepy.API(auth1)):
        #self.stream = Stream(auth=api1.auth, listener=self, tweet_mode='extended')

        fulltweet = ""

        try:
            fulltweet = status.extended_tweet['full_text']
        except:
            fulltweet = status.text

        subreddit = ["DebateWithStrawmen"]

        for key in nameToSubreddit:
            if key.lower() in fulltweet.lower():
                print(key)

                subreddit.append(nameToSubreddit[key])
        endIndex = getEndIndex(fulltweet, 0)
        if fulltweet.lower().find("@ShamsCharania".lower()) == -1 and \
                fulltweet.find("RT @") == -1 and fulltweet.lower().find("story") == -1 \
                and fulltweet.lower().find("stories") and len(fulltweet) >= 65:
            print(fulltweet)
            print(subreddit)

            for sub in subreddit:
                try:
                    reddit.subreddit(sub).submit(
                title= "[Puma] "
                       + fulltweet
                    [0:endIndex + 1],
                url="https://twitter.com/SherpaHerpa/status/"
                    + str(status.id))
                except:
                    print(traceback.print_exc())
                    continue
        else:
            print("Caught retweet! The text was: "
                  +  fulltweet)

myStreamListener = MyStreamListener()

def statusFollower():
    while(True):
        try:
            myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener, tweet_mode="extended")
            myStream.filter(follow=["1328523409941213184"])
            #print("Succesfully streamed")
        except:
            traceback.print_exc()
            statusFollower()

reddit = praw.Reddit(client_id='OcnQUoR3Kamkhw',
                     client_secret='yEfb-X4NP4VdX-BQiZsD-8-A2jI',
                     user_agent='MaranHaGoanHaRav',
                     refresh_token = "56880923-ftskICk1yOn8wa-5W2iQei-mZrU")




statusFollower()
