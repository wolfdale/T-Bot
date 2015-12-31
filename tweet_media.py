import tweepy
import os
import sys
ckey= ''
csecret= ''
atoken=''
asecret= '' 

auth = tweepy.OAuthHandler(ckey,csecret) #Authenticating with twitter
auth.set_access_token(atoken,asecret)    #Access tokens

api = tweepy.API(auth) #Performing Auth
filename = os.path.abspath(sys.argv[1])
status = sys.argv[2]
print "Posting Now"
api.update_with_media(filename,status=status)

