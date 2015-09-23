import tweepy
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import textwrap
from time import sleep 

def TweetToImage(Tweet,count):
        Tweet = Tweet.encode('ascii', 'ignore').decode('ascii')
        para = textwrap.wrap(tweet, width=30)
        im = Image.new ( "RGB", (600,500), "#000" )
        draw = ImageDraw.Draw ( im )
        height_top, line_spacing = 50, 10
        for line in para:
            w, h = draw.textsize(line)
            draw.text(((600 - w) / 2, height_top), line)
            height_top += h + line_spacing
        im.save(str(count)+'.png')

ckey= ' '
csecret= ' '
atoken='  '
asecret= ' ' 

auth = tweepy.OAuthHandler(ckey,csecret) #Authenticating with twitter
auth.set_access_token(atoken,asecret)    #Access tokens

api = tweepy.API(auth)
user='ThatsSarcasm'
tweets = api.user_timeline(user)
count = 0
for tweet in tweets:
	print tweet.text
	string = str(tweet.text)
	s = string.decode('ascii', 'ignore')
	
	print 'Converting Tweet to Image'
	count=count+1
	TweetToImage(s,count)
	print '\n\n'




        
