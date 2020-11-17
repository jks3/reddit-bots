import sys, os, datetime

import twint
import time
import traceback
#from .token import token
c = twint.Config()
#twint.token.Token(c).refresh()
c.Limit = 20
c.Username = "JordanSimkovic"
c.Pandas = True
c.Hide_output = True
#twint.token = token.Token(config)
#twint.token.refresh()

twint.run.Search(c)

Tweets_df1 = twint.storage.panda.Tweets_df

print(Tweets_df1.keys())

def streamer(Tweets_df):
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

            print("There are " + str(len(diff)) + " new tweets")

            i = 0
            for new_tweet in diff:
                i += 1
                print("New tweet number: " + str(i))
                print(new_tweet)
                picture_bool = not not Tweets_df["photos"][i]
                video_bool = bool(Tweets_df["video"][i])
                pod_bool = any("apple.co" in url for url in Tweets_df["urls"][i])

                if picture_bool == video_bool and not pod_bool:
                    print("This would be posted to Reddit")
                else:
                    print("This would not be posted to Reddit")
        else:
            print("No new tweets. Sleeping for 60 seconds")
            time.sleep(60)
            continue

        #dict_Tweets_df = dict(Tweets_df)


while(True):
    try:
        twint.run.Search(c)

        Tweets_df1 = twint.storage.panda.Tweets_df

        streamer(Tweets_df1)
    except:
        traceback.print_exc()
        time.sleep(60*5)
