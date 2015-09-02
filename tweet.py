import tweepy
from time import sleep

ckey= ' '
csecret= ' '
atoken=' '
asecret= ' ' 

auth = tweepy.OAuthHandler(ckey,csecret) #Authenticating with twitter
auth.set_access_token(atoken,asecret)    #Access tokens

api = tweepy.API(auth) #Performing Auth
filename=open("tweet.txt",'r')
f=filename.readlines()
filename.close()
for line in f:
    print "Posting Lyrics Now"
    api.update_status(status=line)
    print "Entering Sleep Mode"
    sleep(840)
    print "Waking Up in 1 Min.."
    sleep(60)

