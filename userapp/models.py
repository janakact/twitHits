from django.db import models
from django.utils import timezone

import tweepy
from operator import attrgetter

# Create your models here.
class TwitterUser(models.Model):
	user_name = models.CharField(max_length=100, default='');
	user_id = models.CharField(max_length=1000,default='');
	access_key = models.CharField(max_length=1000,default='');
	access_secret = models.CharField(max_length=1000,default='');
	
	
	def __str__(self): 
		return self.user_name;

	def setup(self):
		auth = tweepy.OAuthHandler('rD91Gf0aa7axAtDf5TKgQwMfm', 'xBy2wA0N1CTOoa56uEoBTmN7KpnAZniHfK9n2yLYjTQuNQ6AY7')
		auth.set_access_token(self.access_key, self.access_secret)
		self.api = tweepy.API(auth)
		
	def getTweets(self):
		tweets = tweepy.Cursor(self.api.user_timeline,include_rts =False).items(1000)
		tweets = sorted(tweets, key=lambda tweet: int(tweet.retweet_count)+int(tweet.favorite_count))
		return tweets[-10:]
	
	def getProfile(self):
		return self.api.me()