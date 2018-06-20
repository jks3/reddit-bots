import traceback

import praw
import tweepy
import json
from tweepy import Stream

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
    elif (numOfQuotes%2 == 1):
        return endIndex + getEndIndex(tweet[endIndex + 1:], numOfQuotes) + 1
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

        try:
            fulltweet = status.extended_tweet['full_text']

            subreddit = ["nba"]

            for key in nameToSubreddit:
                if key.lower() in fulltweet.lower():

                    subreddit.append(nameToSubreddit[key])

            endIndex = getEndIndex(fulltweet, 0)

            if status.extended_tweet['full_text'].lower().find("@ShamsCharania".lower()) == -1 and \
                    status.extended_tweet['full_text'].find("RT @") == -1:
                print(status.extended_tweet['full_text'])

                for sub in subreddit:
                    try:
                        reddit.subreddit("nba").submit(
                    title= "[Shams Charania] "
                           + status.extended_tweet['full_text']
                        [0:endIndex + 1],
                    url="https://twitter.com/ShamsCharania/status/"
                                                       + str(status.id))
                    except:
                        print(sub)
                        traceback.print_exc()
                        continue
            else:
                print("Caught retweet! The text was more than 140 chars and was: "
                      +  status.extended_tweet['full_text'])
        except:

            subreddit = ["nba"]

            for key in nameToSubreddit:
                if key.lower() in status.text.lower():
                    subreddit.append(nameToSubreddit[key])

            endIndex = getEndIndex(status.text, 0)

            if status.text.lower().find("@ShamsCharania".lower()) == -1 and status.text.find("RT @"):
                print(status.text)

                for sub in subreddit:
                    try:
                        reddit.subreddit(sub).submit(
                    title="[Shams Charania] "
                          + status.text[0:endIndex + 1]
                    , url="https://twitter.com/ShamsCharania/status/"
                                                      + str(status.id))
                    except:
                        print(sub)
                        traceback.print_exc()
                        continue
            else:
                print("Caught retweet! The text was less than 140 chars and was: "
                      +  status.text)


def statusFollower():
    while True:
        try:
            myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener, tweet_mode="extended")
            myStream.filter(follow=["178580925"])
        except:
            continue
reddit = praw.Reddit(client_id='jvTpt-_A6Y_oTA',
                     client_secret='lMkkD-4s2fPkxE9Kp--VrCEHoMI',
                     user_agent='Woj bot by u/mkgandkembafan',
                     username='mkgandkembafan',
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
