import tweepy
from time import sleep

ckey= ' '
csecret= ' '
atoken=' '
asecret= ' ' 

auth = tweepy.OAuthHandler(ckey,csecret) #Authenticating with twitter
auth.set_access_token(atoken,asecret)    #Access tokens

api = tweepy.API(auth) #Performing Auth

filename=open("follower.txt",'r')
#Follower file contain the list of Followers of user
f=filename.readlines()
filename.close()
for line in f:
    try:
        print line
        api.destroy_friendship(line)
    except:
        pass
