from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class StdOutListener(StreamListener):
    def on_data(self,data):
        print(data)
        return True

    def on_errors(self,status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler("JxLPnhf24gauUi0NK3GW0LhAE","f6sLVoTWTc1j7EoXZ9mWiE4JlEfSTFqyYEqqZu8FcReZ64jZmX")
    auth.set_access_token("1105124750194438144-FV46hY8J2bIczwJc3ETRE1KIq93cac","4iiCziNOckefd93O6UKn5YgG5WfcdgUIcVM53ZDSHUO0y")
    stream = Stream(auth,l)
    stream.filter(track=['NASA'])


