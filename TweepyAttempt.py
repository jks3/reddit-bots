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

        subreddit = "DebateWithStrawmen"

        try:
            fulltweet = status.extended_tweet['full_text']

            for key in nameToSubreddit:
                if key.lower() in fulltweet.lower():

                    print(key)

                    subreddit += "+" + nameToSubreddit[key]
            endIndex = getEndIndex(fulltweet)
            if status.extended_tweet['full_text'].find("RT @") == -1 \
                    and status.extended_tweet['full_text'].find("@NYPost_Mets") == -1:
                print(status.extended_tweet['full_text'])
                reddit.subreddit(subreddit).submit(
                    title= "[Puma] "
                           + status.extended_tweet['full_text']
                        [0:endIndex + 1],
                    url="https://twitter.com/JordanSimkovic/status/"
                                                       + str(status.id))
            else:
                print("Caught retweet! The text was more than 140 chars and was: "
                      +  status.extended_tweet['full_text'])
        except:
            subreddit = "DebateWithStrawmen"
            for key in nameToSubreddit:
                if key.lower() in status.text.lower():
                    subreddit += "+" + nameToSubreddit[key]

            endIndex = getEndIndex(status.text)

            if status.text.find("RT @") == -1 and status.text.find("@NYPost_Mets") == -1:
                print(status.text)
                reddit.subreddit(subreddit).submit(
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

reddit = praw.Reddit(client_id='EzSNQk_RZGW2uQ',
                     client_secret='dt4FRLwj51O_4irHhZQ65j5Wi9c',
                     user_agent='Woj bot by u/mkgandkembafan',
                     username='mkgandkembafan',
                     password='Jkys1171998!?')



statusFollower()
