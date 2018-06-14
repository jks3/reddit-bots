import praw
import tweepy
import json
from tweepy import Stream

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

            endIndex = getEndIndex(fulltweet)

            if status.extended_tweet['full_text'].find("@") == -1:
                print(status.extended_tweet['full_text'])

                for sub in subreddit:
                    reddit.subreddit("nba").submit(
                    title= "[Shams Charania] "
                           + status.extended_tweet['full_text']
                        [0:endIndex + 1],
                    url="https://twitter.com/ShamsCharania/status/"
                                                       + str(status.id))
            else:
                print("Caught retweet! The text was more than 140 chars and was: "
                      +  status.extended_tweet['full_text'])
        except:
            subreddit = ["nba"]

            for key in nameToSubreddit:
                if key.lower() in status.text.lower():
                    subreddit.append(nameToSubreddit[key])

            endIndex = getEndIndex(status.text)

            if status.text.find("@") == -1:
                print(status.text)

                for sub in subreddit:
                    reddit.subreddit(sub).submit(
                    title="[Shams Charania] "
                          + status.text[0:endIndex + 1]
                    , url="https://twitter.com/ShamsCharania/status/"
                                                      + str(status.id))
            else:
                print("Caught retweet! The text was less than 140 chars and was: "
                      +  status.text)


def statusFollower():
    try:
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener, tweet_mode="extended")
        myStream.filter(follow=["178580925"])
    except:
        statusFollower()

reddit = praw.Reddit(client_id='jvTpt-_A6Y_oTA',
                     client_secret='lMkkD-4s2fPkxE9Kp--VrCEHoMI',
                     user_agent='Woj bot by u/mkgandkembafan',
                     username='mkgandkembafan',
                     password='Jkys1171998!?!')

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
