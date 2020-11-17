import sys, os, datetime

import twint
import time
import traceback
#from .token import token
c = twint.Config()
#twint.token.Token(c).refresh()
c.Limit = 20
c.Username = "wojespn"
c.Pandas = True
c.Hide_output = True
#twint.token = token.Token(config)
#twint.token.refresh()

twint.run.Search(c)

Tweets_df1 = twint.storage.panda.Tweets_df

pod_bool_list = list(0 for i in range(100))

for i in range(len(Tweets_df1["urls"])):
    pod_bool_list[i] = any("apple" in url for url in Tweets_df1["urls"][i])

indexs = list(j for j in range(100) if pod_bool_list[j] == True)
print(indexs)

for ind in indexs:
    print(Tweets_df1["urls"][ind])
    print(Tweets_df1["tweet"][ind])
