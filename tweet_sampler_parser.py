import json
import pandas as pd
import time
import pprint
import os
import csv
import math
from random import sample 



# settings
os.chdir("/Users/taegyoon/Google Drive/diss_detection/streamed_jsons")
directory = "/Users/taegyoon/Google Drive/diss_detection/streamed_jsons"
files = os.listdir(directory) # this is the list of txt files containing tweets in json
files.remove('.DS_Store') # remove a custom-attirbute container in the Apple macOS operating system



# filename and the number of tweets
json_filename = [] # this is the list that contains the file names
json_number = [] # this is the list that contains the number of tweets
for filename in files:
    tweets_file = open(filename, "r")
    tweets_data = []
    try:
        for line in tweets_file:
            try:
                tweet = json.loads(line) # get a line from json
                tweets_data.append(tweet) # append tweet dictionaries to the list
            except:
                continue
    except:
        continue
    number = len(tweets_data) # get the number of tweets
    json_filename.append(filename)
    json_number.append(number)
    print(filename, "contains", number, "tweets")

# the number of tweets to be sampled 
json_sample_size = [] # this is the list that contains the number of tweets to be sampled from each batch
json_total = [32578934] * 730 # this is the total number of tweets collected
for element in json_number: # this line computes the number of tweets to be sampled from each batch
    a = math.ceil(element*0.030694681415911276) # this is a multiflier to get around 1,000,000 tweets
    json_sample_size.append(a)

# create a dataframe for the file name, tweet number, tweet number to be sampled
json_summary = pd.DataFrame(
    {'json_filename': json_filename,
     'json_number': json_number,
     'json_sample_size': json_sample_size
     })
json_summary.head(50)
json_summary.to_csv('json_summary.csv')

# load the json_summary and parse
json_summary = pd.read_csv("/Users/taegyoon/Google Drive/diss_detection/test/json_summary.csv") 
json_filename = json_summary['json_filename'].tolist()
appended_data = []
for filename in json_filename:
    #from streamed tweet txt files to list
    tweets_file = open(filename, "r") # example txt file of tweets in json
    tweets_data = [] # a list for tweet dictionaries
    for line in tweets_file:
        try:
            tweet = json.loads(line) # get a line from json
            tweets_data.append(tweet) # append tweet dictionaries to the list
        except:
            continue
    number = len(tweets_data)
    a = math.ceil(number*0.030694681415911276)
    tweets_data = sample(tweets_data, a)
    print('From', number, 'tweets in', filename,',', a,'tweets have been sampled.')
    #create a dictionary to contain tweets
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
            'status_is_retweet':[],# is this a retweet?
            'status_is_quote':[],# is this a quote?
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
            data['status_text'].append(str('NA'))
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
        try:
            if ('retweeted_status' in tweet):
                data['status_is_retweet'].append(1)
            else:
                data['status_is_retweet'].append(0)
        except:
            data['status_is_retweet'].append(str('NA'))
        try:
            if (tweet['is_quote_status'] == True):
                data['status_is_quote'].append(1)
            else:
                data['status_is_quote'].append(0)
        except:
            data['status_is_quote'].append(str('NA'))
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
        df = pd.DataFrame(data)
    appended_data.append(df)



# from parsed tweets to pd dataframe
pol_corpus_1st = pd.concat(appended_data)
pd.options.display.max_columns = None
pol_corpus_1st.head(30)
pol_corpus_test = pol_corpus_1st.sample(n=1000)
pol_corpus_1st.to_csv('pol_corpus_1st.csv', encoding='utf-8-sig', float_format='%.30f') # this is a random sample of tweets from the corpus collected for a week



# Boolean querying basd on the initial list of violent keywords
keyword = 'kill|shoot|hang|die|exterminate|execute|executed|stab|killing|castration|kick|hanged|castrate|bullet|burn|fire this|starve|punch|choke|slap|suicide|throat|neutered|shot|death to|shooting|killed|death|fire the|bang on|shoots|guillotine|bomb|spank|kills|spanking|exterminated|be hung|torture|crush|fire|deserves|kicked|slaughter|burned|be dead|punched|light em|kill it|destroy|drown|be exterminated|execution|destroy them|run over|stake|smash|dies|euthanized|firing|execute him|stabbing|stop breathing|castrated|bombing|head off|explode|eradicate|invade|beheading|fired the|cull|hung|be neutered|killing it|kicking|go kill|beating|females|tortured|burn them|remove|dead|her with|fester|should die|invade canada|beat|be shot|go jump|shotgun|heads|be blood|be castrated|eliminate these|neck|eliminate|tear it|head|be euthanized|kill all|be destroyed|nail that|executing|be killed|the missiles|kill em|start killing|beat up|lynching|bash|agonizing|electric chair|just fire|destroyed|hammered|hang the|crucify|punk|fire that|some countries|hit|be eliminated|them then|burn the|throttled|burn it|punching|over with|hanging|to murder|fry|human life|lynched|destroy females|poison|be executed|piffle|bastards|hanged for|strike|cull the|nuke|traitors|neighbours|and be|taken out|beast|be burned|gas chamber|starving the|get shot|on killing|be incinerated|cut|let kill|shotgun would|house down|incinerated|butts out|we kill|the trigger|bury|kill yourself|get hammered|tear|slay|the face|kill them|bite|killing people|fire those|you all|are dead|be removed|don\'t like|what was|burning|nazis|it over|as long|been shot|murdering|about killing|the lynching|alive|gun up|hammer|or in|cutting|this kind|just run|raped|catch them|slapping|bullets|em|getting shot|eliminated|head shake'
keyword_start = r'\bkill|\bshoot|\bhang|\bdie|\bexterminate|\bexecute|\bexecuted|\bstab|\bkilling|\bcastration|\bkick|\bhanged|\bcastrate|\bbullet|\bburn|\bfire this|\bstarve|\bpunch|\bchoke|\bslap|\bsuicide|\bthroat|\bneutered|\bshot|\bdeath to|\bshooting|\bkilled|\bdeath|\bfire the|\bbang on|\bshoots|\bguillotine|\bbomb|\bspank|\bkills|\bspanking|\bexterminated|\bbe hung|\btorture|\bcrush|\bfire|\bdeserves|\bkicked|\bslaughter|\bburned|\bbe dead|\bpunched|\blight em|\bkill it|\bdestroy|\bdrown|\bbe exterminated|\bexecution|\bdestroy them|\brun over|\bstake|\bsmash|\bdies|\beuthanized|\bfiring|\bexecute him|\bstabbing|\bstop breathing|\bcastrated|\bbombing|\bhead off|\bexplode|\beradicate|\binvade|\bbeheading|\bfired the|\bcull|\bhung|\bbe neutered|\bkilling it|\bkicking|\bgo kill|\bbeating|\bfemales|\btortured|\bburn them|\bremove|\bdead|\bher with|\bfester|\bshould die|\binvade canada|\bbeat|\bbe shot|\bgo jump|\bshotgun|\bheads|\bbe blood|\bbe castrated|\beliminate these|\bneck|\beliminate|\btear it|\bhead|\bbe euthanized|\bkill all|\bbe destroyed|\bnail that|\bexecuting|\bbe killed|\bthe missiles|\bkill em|\bstart killing|\bbeat up|\blynching|\bbash|\bagonizing|\belectric chair|\bjust fire|\bdestroyed|\bhammered|\bhang the|\bcrucify|\bpunk|\bfire that|\bsome countries|\bhit|\bbe eliminated|\bthem then|\bburn the|\bthrottled|\bburn it|\bpunching|\bover with|\bhanging|\bto murder|\bfry|\bhuman life|\blynched|\bdestroy females|\bpoison|\bbe executed|\bpiffle|\bbastards|\bhanged for|\bstrike|\bcull the|\bnuke|\btraitors|\bneighbours|\band be|\btaken out|\bbeast|\bbe burned|\bgas chamber|\bstarving the|\bget shot|\bon killing|\bbe incinerated|\bcut|\blet kill|\bshotgun would|\bhouse down|\bincinerated|\bbutts out|\bwe kill|\bthe trigger|\bbury|\bkill yourself|\bget hammered|\btear|\bslay|\bthe face|\bkill them|\bbite|\bkilling people|\bfire those|\byou all|\bare dead|\bbe removed|\bdon\'t like|\bwhat was|\bburning|\bnazis|\bit over|\bas long|\bbeen shot|\bmurdering|\babout killing|\bthe lynching|\balive|\bgun up|\bhammer|\bor in|\bcutting|\bthis kind|\bjust run|\braped|\bcatch them|\bslapping|\bbullets|\bem|\bgetting shot|\beliminated|\bhead shake'
keyword_both = r'\bkill\b|\bshoot\b|\bhang\b|\bdie\b|\bexterminate\b|\bexecute\b|\bexecuted\b|\bstab\b|\bkilling\b|\bcastration\b|\bkick\b|\bhanged\b|\bcastrate\b|\bbullet\b|\bburn\b|\bfire this\b|\bstarve\b|\bpunch\b|\bchoke\b|\bslap\b|\bsuicide\b|\bthroat\b|\bneutered\b|\bshot\b|\bdeath to\b|\bshooting\b|\bkilled\b|\bdeath\b|\bfire the\b|\bbang on\b|\bshoots\b|\bguillotine\b|\bbomb\b|\bspank\b|\bkills\b|\bspanking\b|\bexterminated\b|\bbe hung\b|\btorture\b|\bcrush\b|\bfire\b|\bdeserves\b|\bkicked\b|\bslaughter\b|\bburned\b|\bbe dead\b|\bpunched\b|\blight em\b|\bkill it\b|\bdestroy\b|\bdrown\b|\bbe exterminated\b|\bexecution\b|\bdestroy them\b|\brun over\b|\bstake\b|\bsmash\b|\bdies\b|\beuthanized\b|\bfiring\b|\bexecute him\b|\bstabbing\b|\bstop breathing\b|\bcastrated\b|\bbombing\b|\bhead off\b|\bexplode\b|\beradicate\b|\binvade\b|\bbeheading\b|\bfired the\b|\bcull\b|\bhung\b|\bbe neutered\b|\bkilling it\b|\bkicking\b|\bgo kill\b|\bbeating\b|\bfemales\b|\btortured\b|\bburn them\b|\bremove\b|\bdead\b|\bher with\b|\bfester\b|\bshould die\b|\binvade canada\b|\bbeat\b|\bbe shot\b|\bgo jump\b|\bshotgun\b|\bheads\b|\bbe blood\b|\bbe castrated\b|\beliminate these\b|\bneck\b|\beliminate\b|\btear it\b|\bhead\b|\bbe euthanized\b|\bkill all\b|\bbe destroyed\b|\bnail that\b|\bexecuting\b|\bbe killed\b|\bthe missiles\b|\bkill em\b|\bstart killing\b|\bbeat up\b|\blynching\b|\bbash\b|\bagonizing\b|\belectric chair\b|\bjust fire\b|\bdestroyed\b|\bhammered\b|\bhang the\b|\bcrucify\b|\bpunk\b|\bfire that\b|\bsome countries\b|\bhit\b|\bbe eliminated\b|\bthem then\b|\bburn the\b|\bthrottled\b|\bburn it\b|\bpunching\b|\bover with\b|\bhanging\b|\bto murder\b|\bfry\b|\bhuman life\b|\blynched\b|\bdestroy females\b|\bpoison\b|\bbe executed\b|\bpiffle\b|\bbastards\b|\bhanged for\b|\bstrike\b|\bcull the\b|\bnuke\b|\btraitors\b|\bneighbours\b|\band be\b|\btaken out\b|\bbeast\b|\bbe burned\b|\bgas chamber\b|\bstarving the\b|\bget shot\b|\bon killing\b|\bbe incinerated\b|\bcut\b|\blet kill\b|\bshotgun would\b|\bhouse down\b|\bincinerated\b|\bbutts out\b|\bwe kill\b|\bthe trigger\b|\bbury\b|\bkill yourself\b|\bget hammered\b|\btear\b|\bslay\b|\bthe face\b|\bkill them\b|\bbite\b|\bkilling people\b|\bfire those\b|\byou all\b|\bare dead\b|\bbe removed\b|\bdon\'t like\b|\bwhat was\b|\bburning\b|\bnazis\b|\bit over\b|\bas long\b|\bbeen shot\b|\bmurdering\b|\babout killing\b|\bthe lynching\b|\balive\b|\bgun up\b|\bhammer\b|\bor in\b|\bcutting\b|\bthis kind\b|\bjust run\b|\braped\b|\bcatch them\b|\bslapping\b|\bbullets\b|\bem\b|\bgetting shot\b|\beliminated\b|\bhead shake'
pol_corpus_1st_violent = pol_corpus_1st[
    pol_corpus_1st['status_text'].str.contains(keyword_both, case=False)|
    pol_corpus_1st['status_extended_text'].str.contains(keyword_both, case=False)|
    pol_corpus_1st['retweet_status_text'].str.contains(keyword_both, case=False)|
    pol_corpus_1st['retweet_status_extended_text'].str.contains(keyword_both, case=False)|
    pol_corpus_1st['quote_status_text'].str.contains(keyword_both, case=False)|
    pol_corpus_1st['quote_status_extended_text'].str.contains(keyword_both, case=False)]



# remove retweets
pol_corpus_1st_violent['status_is_retweet'].mean()
pol_corpus_1st_violent_nonrt = pol_corpus_1st_violent[pol_corpus_1st_violent["status_is_retweet"] == 0]


