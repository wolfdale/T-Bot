import tweepy
from time import sleep

ckey= ''
csecret= ''
atoken=''
asecret= '' 

auth = tweepy.OAuthHandler(ckey,csecret) #Authenticating with twitter
auth.set_access_token(atoken,asecret)    #Access tokens

api = tweepy.API(auth) #Performing Auth
#Supply Username to make their tweet your own
public_tweets = api.user_timeline('We_TweetLyrics')
for tweet in public_tweets:
	text = tweet.text
	print text
	api.update_status(status=text)
	sleep(10)
	
    
