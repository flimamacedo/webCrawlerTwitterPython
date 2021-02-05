#!/usr/local/bin/python3
# -*- coding: iso-8859-15 -*-
import mysql.connector
import json
import time
import tweepy
consumer_key = '3GtyvpT4y4fvXwChThTp9tSbI'
consumer_secret = '2G9BCLXBILdtROpEi5XYwNGgGt31dx1W3hKKLq9W7AO0O02raY'
access_token = '1223849409273913344-0zJofFBiNnP5lMtoj6e8fixQDQOHus'
access_token_secret = 'tR9HOWPOtJIUcE36ngKcZwAXCyaErVgqYN9jVCaAAXNZF'
password = 'root'


while True:
   
    try:
        con = mysql.connector.connect(host = 'localhost',
        database='sarg', user='root', password = password, charset = 'utf8')
        cursor = con.cursor()
    except:
        print("Could not connect to MySqlDB")
    
    autenticacao = tweepy.OAuthHandler(consumer_key, consumer_secret)
    autenticacao.set_access_token(access_token, access_token_secret)
    print('Connectect to Twitter')
    twitter = tweepy.API(autenticacao, parser=tweepy.parsers.JSONParser())
    hashtags=["#openbanking", "#apifirst", "#devops", "#cloudfirst", "#microservices", "#apigateway", "#oauth", "#swagger", "#raml", "#openapis"]
    for hashtag in hashtags:
      registers = twitter.search(q=hashtag)
      for tweet in registers:
        print(tweet)
        username = tweet['user']['screen_name']
        created_at = parser.parse(raw_data['created_at'])
        tweet = raw_data['text']
        retweet_count = raw_data['retweet_count']

        if raw_data['place'] is not None:
          place = raw_data['place']['country']
          print(place)
        else:
          place = None
        
        location = raw_data['user']['location']
        
        query = "INSERT INTO apiRest_tweets (username, created_at, tweet, retweet_count,place, location) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (username, created_at, tweet, retweet_count, place, location))
        con.commit()
        cursor.close()
        con.close()
       
      #for tweet in registers:
        #collection.insert(tweet._json)
      time.sleep(300)  
