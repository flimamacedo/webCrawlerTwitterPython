from django.db import models

# Create your models here.
class Tweets(models.Model):
   twitterId = models.AutoField(primary_key=True)  #models.CharField(max_length = 100, unique=True, primary_key=True) 
   created_at = models.DateField() 
   #created_at = models.CharField(max_length = 45)
   username =  models.CharField(max_length = 255)
   followers_count = models.IntegerField()
   lang = models.CharField(max_length= 255)
   tweet = models.TextField()
   retweet_count = models.IntegerField()
   location = models.CharField(max_length = 100, blank=True, null=True)  
   place = models.CharField(max_length = 100, blank=True, null=True)   

