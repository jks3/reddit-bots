import sys, os, datetime

import twint
import time
import traceback

import praw
import tweepy
import json
from tweepy import Stream

from termcolor import colored

nameToSubreddit = {"Mavericks" : "Mavericks",
                   "Mavs" : "Mavericks",
                   "Dallas" : "Mavericks",
                   "Nuggets" : "denvernuggets",
                   "Denver" : "denvernuggets",
                   "Warriors" : "warriors",
                   "Golden State": "warriors",
                   "Rockets" : "rockets",
                   "Houston": "rockets",
                   "Clippers" : "LAClippers",
                   "Clips" : "LAClippers",
                   "Lakers" : "lakers",
                   "Grizzlies" : "memphisgrizzlies",
                   "Memphis": "memphisgrizzlies",
                   "Timberwolves" : "timberwolves",
                   "Wolves" : "timberwolves",
                   "T-wolves" : "timberwolves",
                   "Minnesota": "timberwolves",
                   "Pelicans" : "NOLAPelicans",
                   "Pels" : "NOLAPelicans",
                   "New Orleans": "NOLAPelicans",
                   "Thunder" : "Thunder",
                   "Oklahoma City": "Thunder",
                   "OKC": "Thunder",
                   "Suns" : "suns",
                   "Phoenix": "suns",
                   "Trail Blazers" : "ripcity",
                   "Blazers" : "ripcity",
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
                   "Cavs" : "clevelandcavs",
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

#from .token import token
c = twint.Config()
#twint.token.Token(c).refresh()
c.Limit = 20
c.Username = "ShamsCharania"
c.Pandas = True
c.Hide_output = True
#twint.token = token.Token(config)
#twint.token.refresh()

twint.run.Search(c)

Tweets_df1 = twint.storage.panda.Tweets_df

Reddit = praw.Reddit(client_id='OcnQUoR3Kamkhw',
                     client_secret='yEfb-X4NP4VdX-BQiZsD-8-A2jI',
                     user_agent='MaranHaGoanHaRav',
                     refresh_token = "56880923-ftskICk1yOn8wa-5W2iQei-mZrU")

print(Reddit.user.me())

print(Tweets_df1["tweet"])

def streamer(Tweets_df, reddit):
    while(True):
        #twint.token = token.Token(config)
        #twint.token.refresh()
        twint.token.Token(c).refresh()

        twint.run.Search(c)

        Tweets_df_temp = twint.storage.panda.Tweets_df

        text_df_temp = set(Tweets_df_temp["tweet"])
        text_df = set(Tweets_df["tweet"])

        diff = text_df_temp - text_df

        if not diff == set():
            Tweets_df = Tweets_df_temp

            print(colored(str(datetime.datetime.now()) + " There are " + str(len(diff)) + " new tweets", "green"))

            i = 0
            for new_tweet in diff:
                i += 1
                print(colored(str(datetime.datetime.now()) + " New tweet number: " + str(i), "green"))
                print(colored(str(datetime.datetime.now()) + " " + new_tweet, "green"))
                picture_bool = not not Tweets_df["photos"][i]
                video_bool = bool(Tweets_df["video"][i])
                pod_bool = any("apple.co" in url for url in Tweets_df["urls"][i])

                if picture_bool == video_bool and not pod_bool:
                    subreddit = set()

                    subreddit.add("nba")
                    #subreddit.add("DebateWithStrawmen")
                    #subreddit_test = set()

                    http = len(new_tweet)
                    try:
                        http = str(new_tweet).index("https")
                    except:
                        traceback.print_exc()

                    for key in nameToSubreddit:
                        if (" " + key.lower() + " ") in new_tweet.lower():
                            subreddit.add(nameToSubreddit[key])
                        elif (key.lower() + "'") in new_tweet.lower():
                            subreddit.add(nameToSubreddit[key])
                        elif (" " + key.lower() + "'") in new_tweet.lower():
                            subreddit.add(nameToSubreddit[key])
                        elif (key.lower() + " ") in new_tweet.lower():
                            subreddit.add(nameToSubreddit[key])
                        elif (" " + key.lower()) in new_tweet.lower():
                            subreddit.add(nameToSubreddit[key])
                        elif(" " + key.lower() + ".") in new_tweet.lower():
                            subreddit.add(nameToSubreddit[key])
                        elif(" " + key.lower() + ",") in new_tweet.lower():
                            subreddit.add(nameToSubreddit[key])
                        elif(key.lower() + ",") in new_tweet.lower():
                            subreddit.add(nameToSubreddit[key])
                    #print(subreddit_test)

                    for sub in subreddit:
                        try:
                            reddit.subreddit(sub).submit(
                        title= "[Charania] "
                               + new_tweet[:http],
                        url=Tweets_df["link"][list(Tweets_df["tweet"]).index(new_tweet)], send_replies=False)
                            print(colored(str(datetime.datetime.now()) + " " + sub, "green"))
                        except:
                            print(colored(str(datetime.datetime.now()) + " " + sub, "blue"))
                            traceback.print_exc()
                            continue
                else:
                    print(colored(str(datetime.datetime.now()) + " " + "Caught video or podcast! The text was: "
                                  + new_tweet, "red"))
        else:
            print(colored(str(datetime.datetime.now()) + " " + "No new tweets. Sleeping for 2 seconds", "magenta"))
            time.sleep(2)
            continue

        #dict_Tweets_df = dict(Tweets_df)


while(True):
    try:
        twint.run.Search(c)

        Tweets_df1 = twint.storage.panda.Tweets_df

        streamer(Tweets_df1, Reddit)
    except:
        print(str(datetime.datetime.now()))
        traceback.print_exc()
        time.sleep(60*5)
