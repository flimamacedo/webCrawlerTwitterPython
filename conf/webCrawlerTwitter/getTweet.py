#!/usr/local/bin/python3
# -*- coding: iso-8859-15 -*-

from pymongo import MongoClient
import json
import time
while True:
    
    try:
        conn = MongoClient('mongo', 27017, username='root', password='root')
        print("Connected successfully!")
    except:
        print("Could not connect to MongoDB")
    
    # database
    db = conn.webCrallerTwitter
    
    # Created or Switched to collection names: my_gfg_collection
    collection = db.twitters
    
    import tweepy
    consumer_key="3GtyvpT4y4fvXwChThTp9tSbI"
    consumer_secret="2G9BCLXBILdtROpEi5XYwNGgGt31dx1W3hKKLq9W7AO0O02raY"
    access_token="1223849409273913344-0zJofFBiNnP5lMtoj6e8fixQDQOHus"
    access_token_secret="tR9HOWPOtJIUcE36ngKcZwAXCyaErVgqYN9jVCaAAXNZF"
    
    autenticacao = tweepy.OAuthHandler(consumer_key, consumer_secret)
    autenticacao.set_access_token(access_token, access_token_secret)
    print('Connectect to Twitter')
    twitter = tweepy.API(autenticacao)
    #if not twitter.test():
    #  print('Twitter API test failed')
    hashtags=["#openbanking", "#apifirst", "#devops", "#cloudfirst", "#microservices", "#apigateway", "#oauth", "#swagger", "#raml", "#openapis"]
    for hashtag in hashtags:
     registers = twitter.search(q=hashtag) 
    #registers = twitter.search(q='#openbanking')
    #for tweet in registers:
     for tweet in registers:
        collection.insert(tweet._json)
    time.sleep(300)  
