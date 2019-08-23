import twitter
import praw
from twitter import Status

reddit = praw.Reddit(client_id='jvTpt-_A6Y_oTA',
                     client_secret='lMkkD-4s2fPkxE9Kp--VrCEHoMI',
                     user_agent='Woj bot by u/mkgandkembafan',
                     username='mkgandkembafan',
                     password='')

api = twitter.Api(consumer_key= "BZ1mLujonEsiQ1nXHsQRL5qQQ",
                  consumer_secret= "PeuWzllsoiXnQBxAgWLInNUM8BBY2I0eXQZ2yB2pIp59Fjt4Ul",
                  access_token_key= "615513817-1IxaVyxPfkxZ6jIO9CI89b4FJpSUYxUfw42iUZEH",
                  access_token_secret="aL5qn9629Q3kvCkWjRlKA6bYXwyTnKxaskTLMwsZvmBlI",
                  tweet_mode= 'extended')

statuses = api.GetUserTimeline("50323173")

print ([s.full_text for s in statuses])

print(statuses[2].full_text)

status = twitter.Status.__repr__(statuses[2])

statusStart = status.find("Text='") + 6

statusEnd = status.find(".") + 1

redditTitle = "[Adrian Wojnarowski]" + status[statusStart:statusEnd]

reddit.subreddit("nba").submit(title=redditTitle, url = "http://www.twitter.com/wojespn/status/" +
                                              status[status.find("ID=") + 3:status.find(",")])
