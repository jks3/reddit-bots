import tweepy
import traceback

print(tweepy.__version__)

class MyStreamListener(tweepy.StreamListener):

    #def on_status(self, status):
        #print(status.text)

    def on_error(self, status_code):
        #print(traceback.print_exc())
        print(status_code)

auth = tweepy.AppAuthHandler("33nl5R0LUYyeUmIzyGKBRerET",
                           "WPF5NJIjPya0E4d3IX57bdo4zAb26Xt1AggsGhT1rvyfI5kbbA")
#auth = tweepy.OAuthHandler("QQudwo000fzahCOyDXHxSuuy8",
                           #"6fJb3JbMp9MiM2Z9EUX3Fc7vJREqPSWzHzDR2kS2AHi797Frhp")
#auth.set_access_token("615513817-KBbrJar0PY81rSOUCDwVuVLIHYdlJEkL9rmpv8V6",
                      #"bQHcFwaoYastXquuWW294JKRqztaphCkngVm6TcTHDmVP")

api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

#while(True):
myStream.filter(follow=["1328523409941213184"])