import tweepy
from time import sleep 
#insert your token and keys
ckey= ' '
csecret= ' '
atoken=' '
asecret= ' ' 

auth = tweepy.OAuthHandler(ckey,csecret) #Authenticating with twitter
auth.set_access_token(atoken,asecret)    #Access tokens

api = tweepy.API(auth)
#getting tweets of other user
filename=open("handles.txt",'r')
handle_file=filename.readlines()
filename.close()
#Retweet Latest 20 tweets of a user
for handle in handle_file:
        print handle
        for status in api.user_timeline(handle):
                print status.id
                api.retweet(status.id)
                print 'Enter Sleep Mode (2 min)'
                sleep(10)
                print('Wake up in 10 seconds')
                sleep(10)

