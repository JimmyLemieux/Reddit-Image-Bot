import praw
import urllib
import tweepy
import requests
import time

r = praw.Reddit(client_id ='Lh-aoPW_0K9EgQ', client_secret='cW2SjCHdeBvO_izNizdSIf2ByK8',user_agent='PyBot 0.1',username='FaroJimmy',password='Jrrangers123321')
BASE_FILE_SIZE = 3072 #kb				
def twitter_bot(fileName):
		conKey = 'b0NpO7oEnYRcoW1VetA952Lts'
		conSec = 'XSOGK8gIFnLpAolAVqkfHsPVB4xjOYjCpuJMcHlwTnEBsnw6IK'
		accKey = '3016876398-NJbYG0JWpR1ERiuvyFlQX9Zk8ItNs3GpUsjeJLc'
		privAccKey = 'jkO3N6ae5M8yTQ967wzn9o0ib64DMfQfyAQ5yRq99HYmf'
		auth = tweepy.OAuthHandler(conKey,conSec)
		auth.set_access_token(accKey,privAccKey)
		twitter = tweepy.API(auth)
		
		twitter.update_with_media(fileName)
		
#In this you should get the actual post of the reddit thread, to add to a message of the post
def reddit_Image_Scrape():
		for sub in r.subreddit('Streetwear').top():
			if (sub.url).split('.')[-1] == 'jpg':
				#call the saver function
				#The file size meta data of the image
				web = urllib.urlopen(sub.url).info().getheaders('Content-Length')
				url_retreive(sub.url,web);
				time.sleep(900)
			else:
				print('bad link')

def url_retreive(URLID,metaData):
		
		#Get the size of the file
			for value in metaData:
				number = int(value) / 1000
				if number <= BASE_FILE_SIZE:
					#Send to twitter bot yo
					urllib.urlretrieve(URLID,'emp.jpg')
					twitter_bot('emp.jpg')

						
				
reddit_Image_Scrape();
#Next thing to do is check the size of a file, must be less than 3072 kb
#Try to get two scripts running at the same time 	
	
	
	
	
