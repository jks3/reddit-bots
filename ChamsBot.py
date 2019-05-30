import traceback

import praw
import tweepy
import json
from tweepy import Stream

from termcolor import colored

nameToSubreddit = {"Mavericks" : "Mavericks",
                   "Dallas" : "Mavericks",
                   "Nuggets" : "denvernuggets",
                   "Denver" : "denvernuggets",
                   "Warriors" : "warriors",
                   "Golden State": "warriors",
                   "Rockets" : "rockets",
                   "Houston": "rockets",
                   "Clippers" : "LAClippers",
                   "Lakers" : "lakers",
                   "Grizzlies" : "memphisgrizzlies",
                   "Memphis": "memphisgrizzlies",
                   "Timberwolves" : "timberwolves",
                   "Minnesota": "timberwolves",
                   "Pelicans" : "NOLAPelicans",
                   "New Orleans": "NOLAPelicans",
                   "Thunder" : "Thunder",
                   "Oklahoma City": "Thunder",
                   "OKC": "Thunder",
                   "Suns" : "suns",
                   "Phoenix": "suns",
                   "Trail Blazers" : "ripcity",
                   "Portland": "ripcity",
                   "Kings" : "kings",
                   "Sacramento": "kings",
                   "Spurs" : "NBASpurs",
                   "San Antonio": "NBASpurs",
                   "Jazz" : "UtahJazz",
                   "Utah": "UtahJazz",
                   "Hawks" : "AtlantaHawks",
                   "Atlanta": "AtlantaHawks",
                   "Celtics" : "bostonceltics",
                   "Boston": "bostonceltics",
                   "Nets" : "GoNets",
                   "Brooklyn": "GoNets",
                   "Hornets" : "CharlotteHornets",
                   "Charlotte": "CharlotteHornets",
                   "Bulls" : "chicagobulls",
                   "Chicago": "chicagobulls",
                   "Cavaliers" : "clevelandcavs",
                   "Cleveland": "clevelandcavs",
                   "Pistons" : "DetroitPistons",
                   "Detroit": "DetroitPistons",
                   "Pacers" : "pacers",
                   "Indiana": "pacers",
                   "Heat" : "heat",
                   "Miami": "heat",
                   "Bucks" : "MkeBucks",
                   "Milwaukee": "MkeBucks",
                   "Knicks" : "NYKnicks",
                   "New York": "NYKnicks",
                   "Magic" : "OrlandoMagic",
                   "Orlando": "OrlandoMagic",
                   "76ers" : "sixers",
                   "Philadelphia": "sixers",
                   "Sixers" : "sixers",
                   "Raptors" : "torontoraptors",
                   "Toronto": "torontoraptors",
                   "Wizards" : "washingtonwizards",
                   "Washington" : "washingtonwizards"}

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
    elif endIndex < 85:
        return endIndex + getEndIndex(tweet[endIndex + 1:], 0) + 1
    else:
        return endIndex


class MyStreamListener(tweepy.StreamListener):
    auth1 = tweepy.OAuthHandler("BZ1mLujonEsiQ1nXHsQRL5qQQ",
                               "PeuWzllsoiXnQBxAgWLInNUM8BBY2I0eXQZ2yB2pIp59Fjt4Ul")
    auth1.set_access_token("615513817-1IxaVyxPfkxZ6jIO9CI89b4FJpSUYxUfw42iUZEH",
                          "aL5qn9629Q3kvCkWjRlKA6bYXwyTnKxaskTLMwsZvmBlI")

    #api1 = tweepy.API(auth1)
    def on_status(self, status, api1=tweepy.API(auth1)):
        self.stream = Stream(auth=api1.auth, listener=self, tweet_mode='extended')

        fulltweet = ""
        try:
            fulltweet = status.extended_tweet['full_text']
        except:
            fulltweet = status.text


        #endIndex = getEndIndex(fulltweet, 0)

        if (fulltweet.lower().find("rt @") == -1  and fulltweet.lower().find("@shamscharania") == -1 \
                and len(fulltweet) >= 5):
            print(colored(fulltweet, "green"))

            try:
                reddit.subreddit("nba").submit(
                    title="[Charania] "
                          + fulltweet
                          [0:fulltweet.lower().find("htt")],
                    url="https://twitter.com/ShamsCharania/status/"
                        + str(status.id), send_replies=False)
            except:
                print(colored("nba", "blue"))
                traceback.print_exc()

            subreddit = set()

            for key in nameToSubreddit:
                if ((" " + key.lower() + " ") or (key.lower() + "' ") or (" " + key.lower() + "' ")) in fulltweet.lower():
                    subreddit.add(nameToSubreddit[key])

            for sub in subreddit:
                try:
                    reddit.subreddit(sub).submit(
                title= "[Charania] "
                       + fulltweet
                    [0:fulltweet.lower().find("htt")],
                url="https://twitter.com/ShamsCharania/status/"
                                                   + str(status.id), send_replies=False)
                except:
                    print(colored(sub, "blue"))
                    traceback.print_exc()
                    continue
        else:
            print(colored("Caught retweet! The text was: "
                          + fulltweet, "red"))


def statusFollower():
    while True:
        try:
            myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener, tweet_mode="extended")
            myStream.filter(follow=["178580925"])
        except:
            continue

reddit = praw.Reddit(client_id='3DLVL7d7SS8_qQ',
                     client_secret='VAtp6-6RlqNZXItkl9wa-9iExVI',
                     user_agent='MaranHaGoanHaRav',
                     username='MKGandKembaFan',
                     password='Jkys1171998!?')

auth = tweepy.OAuthHandler("BZ1mLujonEsiQ1nXHsQRL5qQQ",
                           "PeuWzllsoiXnQBxAgWLInNUM8BBY2I0eXQZ2yB2pIp59Fjt4Ul")
auth.set_access_token("615513817-1IxaVyxPfkxZ6jIO9CI89b4FJpSUYxUfw42iUZEH",
                      "aL5qn9629Q3kvCkWjRlKA6bYXwyTnKxaskTLMwsZvmBlI")

api = tweepy.API(auth)

print(api.user_timeline(id = "wojespn", tweet_mode = "extended")[2].full_text)

print(type(api.user_timeline(id = "wojespn", tweet_mode = "extended")[2]))

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener, tweet_mode = "extended")

statusFollower()
