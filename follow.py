import tweepy

# Your Key and Token 
ckey= ' '
csecret= ' '
atoken=' '
asecret= ' ' 

auth = tweepy.OAuthHandler(ckey,csecret) #Authenticating with twitter
auth.set_access_token(atoken,asecret)    #Access tokens

api = tweepy.API(auth) #Performing Auth

user=api.get_user('    ')  # Enter user name to follow its followers
print user.screen_name 
print user.followers_count
for friend in user.friends():
    print friend.screen_name
    x=friend.screen_name
    api.create_friendship(x)
