import tweepy
from tweepy import OAuthHandler

api_key='ODr41lxd5IMDEbzQjLSUQLrzp'
api_secret='OJRmPSLzrtdBRPmUHdvYVQMNF64xxDshuXOFlUFxtGfJ96yxPy'
access_token='713586329729150976-wnjSNwLH90M1RQz5OI9rbnBJegdD5GA'
access_token_secret='DukQHd8yRf3qxixyyix4Fbg0V8JJDZ6OrK1nAeQNh3wF2'

 
auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)    
    
from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('tweets.json', 'a') as f:  
                f.write(data)
                print(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())

#change the keyword here
twitter_stream.filter(track=['sentimental analysis'])





