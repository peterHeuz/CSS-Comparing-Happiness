from tweepy import Stream
from tweepy.streaming import StreamListener
import tweepy
from tweepy import OAuthHandler
 

#please keep these private, as they belong to  my personal twitter account
consumer_key = 'tCoHhTkxpOKi5zQqNTv9t5eu7'
consumer_secret = 'O7wzdFZxWAnWEBScv1rHZh73sysMWFb2DeJFPxRhdAoFvUQSbS'
access_token = '308424160-629KeKYT1EMooDZpHuNGJHxlrltqYYzFqPkpTTeD'
access_secret = 'A4EkmsxJMgxKh3Wf2xcQfyVxBga22AMYhJDfiWscUur0X'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
 
 
class MyListener(StreamListener):
 
	def on_data(self, data):
		try:
			with open('python.json', 'a') as f:
				f.write(data)
				return True
		except BaseException as e:
			print("Error on_data: %s" % str(e))
		return True
 
	def on_error(self, status):
		print(status)
		return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(locations=[5.6725,50.3543,9.5566,52.7248])
