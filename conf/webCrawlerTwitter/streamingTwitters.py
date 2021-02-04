from __future__ import print_function
import tweepy
import json
#import MySQLdb 
import mysql.connector
from dateutil import parser
 
WORDS = ["#openbanking", "#apifirst", "#devops", "#cloudfirst", "#microservices", "#apigateway", "#oauth", "#swagger", "#raml", "#openapis"]
 
CONSUMER_KEY = "xZIqCraA06CYEzFqNOpubn1Ua"
CONSUMER_SECRET = "oq0QJShtqXDPIBJi9i0qpySlaBPHu3VI5OpQAajtZ9OuZlr7Vo"
ACCESS_TOKEN = "1226685332294393856-PjDlFNhoFvg4nGoNb3JhxCrWSSA5Kf"
ACCESS_TOKEN_SECRET = "PzJPrtn7kxMnNj6GBVwtIbbxNYVS500ZNmnkkdFsrJakL"
 
HOST = "db"
USER = "root"
PASSWD = "root"
DATABASE = "sarg"
 
# This function takes the 'created_at', 'text', 'screen_name' and 'tweet_id' and stores it
# into a MySQL database
def store_data(username, followers_count, lang, created_at, tweet, retweet_count, place, location):
    db=mysql.connector.connect(host=HOST, user=USER, passwd=PASSWD, db=DATABASE, charset="utf8")
    cursor = db.cursor()
    insert_query = "INSERT INTO apiRest_tweets (username, followers_count, lang, created_at, tweet, retweet_count,place, location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    username, created_at, tweet, retweet_count, place, location
    cursor.execute(insert_query, (username, followers_count, lang, created_at, tweet, retweet_count, place, location))
    db.commit()
    cursor.close()
    db.close()
    return
 
class StreamListener(tweepy.StreamListener):    
    #This is a class provided by tweepy to access the Twitter Streaming API. 
 
    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")
 
    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False
 
    def on_data(self, data):
        #This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:
           # Decode the JSON from Twitter
            datajson = json.loads(data)
            #grab the wanted data from the Tweet
            username = datajson['user']['screen_name']
            followers_count = datajson['user']['followers_count']
            lang = datajson['lang']
            created_at = parser.parse(datajson['created_at'])
            tweet = datajson['text']
            retweet_count = datajson['retweet_count']

            if datajson['place'] is not None:
                place = datajson['place']['country']
                print(place)
            else:
                place = None

            location = datajson['user']['location']
 
            #print out a message to the screen that we have collected a tweet
            print("Tweet collected at " + str(created_at))
            
            #insert the data into the MySQL database
            store_data(username, followers_count, lang, created_at, tweet, retweet_count, place, location)
        
        except Exception as e:
           print(e)
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True)) 
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)
