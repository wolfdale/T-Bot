#create Handle DB for Following
from time import sleep
import tweepy

ckey= ' '
csecret= ' '
atoken=' '
asecret=' ' 

auth = tweepy.OAuthHandler(ckey,csecret) #Authenticating with twitter
auth.set_access_token(atoken,asecret)    #Access tokens

api = tweepy.API(auth)
print api.rate_limit_status()
name = raw_input('Enter name of text file: ')+'.txt'
seed_user='  ' # Enter Seed for creating a DB of twitter Handles
for counter in range(1,100000):
        print counter
        file = open(name,'a')
        user=api.get_user(seed_user)
        print user.screen_name
        print user.followers_count
        if(user.followers_count != 0):
                for follower in user.friends():
                        try:
                                file.write('\n')
                                name_of_foll=follower.screen_name
                                file.write(name_of_foll)
                                
                        except:
                                print('Something went wrong! Can\'t tell what?')
        else:
                pass
        seed_user=name_of_foll
        sleep(120)
file.close()



