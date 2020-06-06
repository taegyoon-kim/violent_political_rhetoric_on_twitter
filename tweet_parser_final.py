#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 23:16:43 2020

@author: taegyoon
"""


import json
import pandas as pd
import time
import pprint
import os
import csv


# from streamed tweet txt files to list
tweets_file = open("/Users/taegyoon/Google Drive/diss_detection/streamed_jsons/stream1_2020_0529_1425_37.txt", "r") # example txt file of tweets in json
tweets_data = [] # a list for tweet dictionaries
for line in tweets_file:
    try:
        tweet = json.loads(line) # get a line from json
        tweets_data.append(tweet) # append tweet dictionaries to the list
    except:
        continue


# examine the structure of json    
# pprint.pprint(tweets_data[6]) 


# create a dictionary to contain tweets
data = {'user_id':[], # original user
        'user_screen_name':[],
        'user_created_at':[],
        'user_favourites_count':[],
        'user_followers_count':[],
        'user_friends_count':[],
        'user_status_count':[],
        'status_id':[], # original status
        'status_created_at':[],
        'status_text':[], 
        'status_extended_text':[], 
        'status_reply_to_status_id':[], # status reply fields
        'status_reply_to_user_id':[],        
        'status_reply_to_screen_name':[],  
        'status_favorite_count':[], # status count fields
        'status_retweet_count':[],
        'status_quote_count':[],
        'status_reply_count':[],
        'stauts_is_retweet':[],# is this a retweet?
        'stauts_is_quote':[],# is this a quote?
        'retweet_user_id':[], # retweet user
        'retweet_user_screen_name':[],
        'retweet_user_created_at':[],
        'retweet_user_favourites_count':[],
        'retweet_user_followers_count':[],
        'retweet_user_friends_count':[],
        'retweet_user_status_count':[],
        'retweet_status_id':[], # retweet status
        'retweet_status_created_at':[],
        'retweet_status_text':[], 
        'retweet_status_extended_text':[], 
        'retweet_status_reply_to_status_id':[],
        'retweet_status_reply_to_user_id':[],        
        'retweet_status_reply_to_screen_name':[],  
        'retweet_status_favorite_count':[],
        'retweet_status_retweet_count':[],
        'retweet_status_quote_count':[],
        'retweet_status_reply_count':[],
        'quote_user_id':[], # quote user
        'quote_user_screen_name':[],
        'quote_user_created_at':[],
        'quote_user_favourites_count':[],
        'quote_user_followers_count':[],
        'quote_user_friends_count':[],
        'quote_user_status_count':[],
        'quote_status_id':[], # quote status
        'quote_status_created_at':[],
        'quote_status_text':[], 
        'quote_status_extended_text':[], 
        'quote_status_reply_to_status_id':[],
        'quote_status_reply_to_user_id':[],        
        'quote_status_reply_to_screen_name':[],  
        'quote_status_favorite_count':[],
        'quote_status_retweet_count':[],
        'quote_status_quote_count':[],
        'quote_status_reply_count':[]}
        

# fill in the dictionary by extracting relevant info 
for tweet in tweets_data:
    try:
        data['user_id'].append(tweet['user']["id_str"])
    except:
        data['user_id'].append(str('NA'))
    try:
        data['user_screen_name'].append(tweet['user']['screen_name'])
    except:
        data['user_screen_name'].append(str('NA'))
    try:
        data['user_created_at'].append(tweet['user']['created_at'])
    except:
        data['user_created_at'].append(str('NA'))
    try:
        data['user_favourites_count'].append(tweet['user']['favourites_count'])
    except:
        data['user_favourites_count'].append(str('NA'))
    try:
        data['user_followers_count'].append(tweet['user']['followers_count'])
    except:
        data['user_followers_count'].append(str('NA'))
    try:
        data['user_friends_count'].append(tweet['user']['friends_count'])
    except:
        data['user_friends_count'].append(str('NA'))
    try:
        data['user_status_count'].append(tweet['user']['statuses_count'])
    except:
        data['user_status_count'].append(str('NA'))
    try:
        data['status_id'].append(tweet['id_str'])
    except:
        data['status_id'].append(str('NA'))
    try:
        data['status_created_at'].append(tweet['created_at'])
    except:
        data['status_created_at'].append(str('NA'))
    try: 
        data['status_text'].append(tweet['text'])
    except:
        data['status_created_at'].append(str('NA'))
    try:
        data['status_extended_text'].append(tweet['extended_tweet']['full_text'])
    except:
        data['status_extended_text'].append(str('NA'))
    try:
        data['status_reply_to_status_id'].append(tweet['in_reply_to_status_id_str'])
    except:
        data['status_reply_to_status_id'].append(str('NA'))
    try:
        data['status_reply_to_user_id'].append(tweet['in_reply_to_user_id_str'])
    except:
        data['status_reply_to_user_id'].append(str('NA'))
    try:
        data['status_reply_to_screen_name'].append(tweet['in_reply_to_screen_name'])
    except:
        data['status_reply_to_screen_name'].append(str('NA'))
    try:
        data['status_favorite_count'].append(tweet['favorite_count'])
    except:
        data['status_favorite_count'].append(str('NA'))
    try:
        data['status_retweet_count'].append(tweet['retweet_count'])
    except:
        data['status_retweet_count'].append(str('NA'))
    try:
        data['status_quote_count'].append(tweet['quote_count'])
    except:
        data['status_quote_count'].append(str('NA'))
    try:
        data['status_reply_count'].append(tweet['reply_count'])
    except:
        data['status_reply_count'].append(str('NA'))
    if ('retweeted_status' in tweet):
        data['stauts_is_retweet'].append(1)
    else:
        data['stauts_is_retweet'].append(0)
    if (tweet['is_quote_status'] == True):
        data['stauts_is_quote'].append(1)
    else:
        data['stauts_is_quote'].append(0)
    try:
        data['retweet_user_id'].append(tweet['retweeted_status']['user']['id_str'])
    except:
        data['retweet_user_id'].append(str('NA'))
    try:
        data['retweet_user_screen_name'].append(tweet['retweeted_status']['user']['screen_name'])
    except:
        data['retweet_user_screen_name'].append(str('NA'))
    try:
        data['retweet_user_created_at'].append(tweet['retweeted_status']['user']['created_at'])
    except:
        data['retweet_user_created_at'].append(str('NA'))
    try:
        data['retweet_user_favourites_count'].append(tweet['retweeted_status']['user']['favourites_count'])
    except:
        data['retweet_user_favourites_count'].append(str('NA'))
    try:
        data['retweet_user_followers_count'].append(tweet['retweeted_status']['user']['followers_count'])
    except:
        data['retweet_user_followers_count'].append(str('NA'))
    try:
        data['retweet_user_friends_count'].append(tweet['retweeted_status']['user']['friends_count'])
    except:
        data['retweet_user_friends_count'].append(str('NA'))
    try:
        data['retweet_user_status_count'].append(tweet['retweeted_status']['user']['statuses_count'])
    except:
        data['retweet_user_status_count'].append(str('NA'))
    try:
        data['retweet_status_id'].append(tweet['retweeted_status']['id_str'])
    except:
        data['retweet_status_id'].append(str('NA'))
    try:
        data['retweet_status_created_at'].append(tweet['retweeted_status']['created_at'])
    except:
        data['retweet_status_created_at'].append(str('NA'))
    try:
        data['retweet_status_text'].append(tweet['retweeted_status']['text'])
    except:
        data['retweet_status_text'].append(str('NA'))
    try:
        data['retweet_status_extended_text'].append(tweet['retweeted_status']['extended_tweet']['full_text'])
    except:
        data['retweet_status_extended_text'].append(str('NA'))
    try:
        data['retweet_status_reply_to_status_id'].append(tweet['retweeted_status']['in_reply_to_status_id_str'])
    except:
        data['retweet_status_reply_to_status_id'].append(str('NA'))
    try:
        data['retweet_status_reply_to_user_id'].append(tweet['retweeted_status']['in_reply_to_user_id_str'])
    except:
        data['retweet_status_reply_to_user_id'].append(str('NA'))
    try:
        data['retweet_status_reply_to_screen_name'].append(tweet['retweeted_status']['in_reply_to_screen_name'])
    except:
        data['retweet_status_reply_to_screen_name'].append(str('NA'))
    try:    
        data['retweet_status_favorite_count'].append(tweet['retweeted_status']['favorite_count'])
    except:
        data['retweet_status_favorite_count'].append(str('NA'))
    try:
        data['retweet_status_retweet_count'].append(tweet['retweeted_status']['retweet_count'])
    except:
        data['retweet_status_retweet_count'].append(str('NA'))
    try:    
        data['retweet_status_quote_count'].append(tweet['retweeted_status']['quote_count'])
    except:
        data['retweet_status_quote_count'].append(str('NA'))
    try:
        data['retweet_status_reply_count'].append(tweet['retweeted_status']['reply_count'])
    except:
        data['retweet_status_reply_count'].append(str('NA'))
    try:
        data['quote_user_id'].append(tweet['quoted_status']['user']['id_str'])
    except:
        data['quote_user_id'].append(str('NA'))
    try:
        data['quote_user_screen_name'].append(tweet['quoted_status']['user']['screen_name'])
    except:
        data['quote_user_screen_name'].append(str('NA'))
    try:
        data['quote_user_created_at'].append(tweet['quoted_status']['user']['created_at'])
    except:
        data['quote_user_created_at'].append(str('NA'))
    try:
        data['quote_user_favourites_count'].append(tweet['quoted_status']['user']['favourites_count'])
    except:
        data['quote_user_favourites_count'].append(str('NA'))
    try:
        data['quote_user_followers_count'].append(tweet['quoted_status']['user']['followers_count'])
    except:
        data['quote_user_followers_count'].append(str('NA'))
    try:
        data['quote_user_friends_count'].append(tweet['quoted_status']['user']['friends_count'])
    except:
        data['quote_user_friends_count'].append(str('NA'))
    try:
        data['quote_user_status_count'].append(tweet['quoted_status']['user']['statuses_count'])
    except:
        data['quote_user_status_count'].append(str('NA'))
    try:
        data['quote_status_id'].append(tweet['quoted_status']['id_str'])
    except:
        data['quote_status_id'].append(str('NA'))
    try:
        data['quote_status_created_at'].append(tweet['quoted_status']['created_at'])
    except:
        data['quote_status_created_at'].append(str('NA'))
    try:
        data['quote_status_text'].append(tweet['quoted_status']['text'])
    except:
        data['quote_status_text'].append(str('NA'))
    try:
        data['quote_status_extended_text'].append(tweet['quoted_status']['extended_tweet']['full_text'])
    except:
        data['quote_status_extended_text'].append(str('NA'))
    try:
        data['quote_status_reply_to_status_id'].append(tweet['quoted_status']['in_reply_to_status_id_str'])
    except:
        data['quote_status_reply_to_status_id'].append(str('NA'))
    try:
        data['quote_status_reply_to_user_id'].append(tweet['quoted_status']['in_reply_to_user_id_str'])
    except:
        data['quote_status_reply_to_user_id'].append(str('NA'))
    try:
        data['quote_status_reply_to_screen_name'].append(tweet['quoted_status']['in_reply_to_screen_name'])
    except:
        data['quote_status_reply_to_screen_name'].append(str('NA'))
    try:    
        data['quote_status_favorite_count'].append(tweet['quoted_status']['favorite_count'])
    except:
        data['quote_status_favorite_count'].append(str('NA'))
    try:
        data['quote_status_retweet_count'].append(tweet['quoted_status']['retweet_count'])
    except:
        data['quote_status_retweet_count'].append(str('NA'))
    try:    
        data['quote_status_quote_count'].append(tweet['quote_status']['quote_count'])
    except:
        data['quote_status_quote_count'].append(str('NA'))
    try:
        data['quote_status_reply_count'].append(tweet['quote_status']['reply_count'])
    except:
        data['quote_status_reply_count'].append(str('NA'))


# dictionary to pandas dataframe
df = pd.DataFrame(data)
df.to_csv('df.csv')
df.to_csv('df.csv',encoding='utf-8-sig')
