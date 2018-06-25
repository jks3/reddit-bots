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
    elif (numOfQuotes%2 == 1):
        return endIndex + getEndIndex(tweet[endIndex + 1:], numOfQuotes) + 1
    else:
        return endIndex

auth = tweepy.OAuthHandler("RedMTi3TGgGXrdsy4IC20gOX4",
                           "JV7EcbrXaW35lAOutz46gVhjWMP2o3ZhmySCUNgVY9meTmUKAU")
auth.set_access_token("615513817-tC4DYQokwF7euREQr5RUV0MFhNFhNak2raFD02os",
                      "SPeyjpNqThX1TFuxQcAZyJydqgQkYneJQXHfB2sIJs7ne")

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
    auth1 = tweepy.OAuthHandler("RedMTi3TGgGXrdsy4IC20gOX4",
                               "JV7EcbrXaW35lAOutz46gVhjWMP2o3ZhmySCUNgVY9meTmUKAU")
    auth1.set_access_token("615513817-tC4DYQokwF7euREQr5RUV0MFhNFhNak2raFD02os",
                          "SPeyjpNqThX1TFuxQcAZyJydqgQkYneJQXHfB2sIJs7ne")

    #api1 = tweepy.API(auth1)
    def on_status(self, status, api1=tweepy.API(auth1)):
        self.stream = Stream(auth=api1.auth, listener=self, tweet_mode='extended')

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
            print(status.extended_tweet['full_text'])
            print(subreddit)

            for sub in subreddit:
                try:
                    reddit.subreddit(sub).submit(
                title= "[Puma] "
                       + status.extended_tweet['full_text']
                    [0:endIndex + 1],
                url="https://twitter.com/JordanSimkovic/status/"
                    + str(status.id))
                except:
                    continue
        else:
            print("Caught retweet! The text was: "
                  +  fulltweet)

myStreamListener = MyStreamListener()

def statusFollower():
    try:
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener, tweet_mode="extended")
        myStream.filter(follow=["615513817"])
    except:
        statusFollower()

reddit = praw.Reddit(client_id='EzSNQk_RZGW2uQ',
                     client_secret='dt4FRLwj51O_4irHhZQ65j5Wi9c',
                     user_agent='Woj bot by u/mkgandkembafan',
                     username='mkgandkembafan',
                     password='Jkys1171998!?')



statusFollower()
