import traceback

import praw
import tweepy
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
    auth1 = tweepy.OAuthHandler("eODhcgjOj5eK5bzr9zzDgiFoY",
                           "ZYLxBnhJ7TaTwkkLR9zdmd20ql7VI1U9giS3FGXS81JSh7Vo3W")
    auth1.set_access_token("615513817-RsEbaXssZ0ZLgUWWDu3inKC68Ai1fVG96Jxcj86K",
                      "pjwiizzwrODF6SG1AKnpIYQb42dEyveFr9RJI365SBGHU")

    #api1 = tweepy.API(auth1)
    def on_status(self, status, api1=tweepy.API(auth1)):
        self.stream = Stream(auth=api1.auth, listener=self, tweet_mode='extended')

        fulltweet = ""

        try:
            fulltweet = status.extended_tweet['full_text']
        except:
            fulltweet = status.text

        subreddit = set()

        #endIndex = getEndIndex(fulltweet, 0)

        for key in nameToSubreddit:
            if key.lower() in fulltweet.lower():
                subreddit.add(nameToSubreddit[key])
                subreddit.add("nba")

        if fulltweet.lower().find("@") == -1 and fulltweet.lower().find("story") == -1 \
                and fulltweet.lower().find("stories") and len(fulltweet) >= 65:
            print(colored(fulltweet, "green"))
            try:
                reddit.subreddit(sub).submit(
                        title= "[Wojnarowski] "
                       + fulltweet
                    [0:fulltweet.lower().find("htt")],
                url="https://twitter.com/wojespn/status/"
                                                   + str(status.id))
            except:
                traceback.print_exc()
        else:
            print("Caught retweet! The text was: "
                  +  fulltweet)

def statusFollower():
    while (True):
        try:
            myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener, tweet_mode="extended")
            myStream.filter(follow=["50323173"])
        except:
            continue

reddit = praw.Reddit(client_id='43Y_8Z6s6n9htA',
                     client_secret='i6LDFau9AZpedKfYzjrlnS80t90',
                     user_agent='MaranHaGoanHaRav',
                     username='DovidHaMelechUShlomo',
                     password='Jkys1171998!?')

auth = tweepy.OAuthHandler("eODhcgjOj5eK5bzr9zzDgiFoY",
                           "ZYLxBnhJ7TaTwkkLR9zdmd20ql7VI1U9giS3FGXS81JSh7Vo3W")
auth.set_access_token("615513817-RsEbaXssZ0ZLgUWWDu3inKC68Ai1fVG96Jxcj86K",
                      "pjwiizzwrODF6SG1AKnpIYQb42dEyveFr9RJI365SBGHU")

api = tweepy.API(auth)

print(api.user_timeline(id = "wojespn", tweet_mode = "extended")[2].full_text)

print(type(api.user_timeline(id = "wojespn", tweet_mode = "extended")[2]))

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener, tweet_mode = "extended")

statusFollower()
