###### author details: Taegyoon Kim, taegyoon@psu.edu
###### purpose: This script is used to filter-stream live tweets and save a txt file of json objects every N minutes
###### last edit: 1 Feb 2021


##### packages

import os, time
from tweepy import OAuthHandler, Stream, StreamListener, API
from datetime import datetime
os.chdir('') # directory to save json txt files in


##### authentification

auth = OAuthHandler('', '')
auth.set_access_token('', '')
api = API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)


##### stream

while True:

    txt = 'stream' + str(datetime.now().strftime('%Y_%m%d_%H%M_%S')) + '.txt'

    class Listener(StreamListener):

        def __init__(self, time_limit= 3600):
            self.start_time = time.time()
            self.limit = time_limit
            self.saveFile = open(txt, 'a')
            super(Listener, self).__init__()

        def on_data(self, tweet):
            if (time.time() - self.start_time) < self.limit:
                self.saveFile.write(tweet)
                self.saveFile.write('\n')
                return True
            else:
                self.saveFile.close()
                return False

        def on_error(self, status_code):
            if status_code == 420:
                global last_420
                global err_420
                if time.time() - last_420 > 43200:
                    err_420 = 0
                last_420 = time.time()
                stopsec = 60*(2**err_420)
                err_420 += 1
                print("Error 420. Pausing for " + str(stopsec) + " seconds before restarting.")
                time.sleep(stopsec)
            else:
                global last_err
                global err_other
                if time.time() - last_err > 7200:
                    err_other = 0
                last_err = time.time()
                stopsec = 5*(2**err_other)
                if err_other < 6:
                    err_other += 1
                print("Error " + str(status_code) + ". Pausing for " + str(stopsec) + " seconds before restarting.")
                time.sleep(stopsec)
            return True
    
        def on_disconnect(self, notice):
            global last_disc
            global disconnects
            if time.time() - last_disc > 7200:
                disconnects = 0
            last_disc = time.time()
            if disconnects < 16:
                disconnects += 0.25
            print("Stream disconnected: " + notice + " Waiting " + str(disconnects) + " seconds before restarting.")
            time.sleep(disconnects)
            return True

        def on_warning(self, notice):
            print("Warning: " + notice)
            return True

    listener = Listener()
    streamer = Stream(auth = api.auth, listener = listener)
    err_420 = 0
    err_other = 0
    disconnects = 0
    last_420 = time.time() - 43200
    last_err = time.time() - 7200
    last_disc = time.time() - 7200

    def Streaming(tags = None, follow = None, lang = None):
        try:
            print('Start streaming.')
            streamer.filter(track=['keyword'], encoding = 'utf8', languages = ['en'])
        except KeyboardInterrupt:
            print('Manually stopped.')
            streamer.disconnect()
        except Exception as e:
            global last_disc
            global disconnects
            if time.time() - last_disc > 7200:
                disconnects = 0
            last_disc = time.time()
            if disconnects < 16:
                disconnects += 0.25
            print("Stream stopped. Waiting " + str(disconnects) + " seconds before restarting.")
            time.sleep(disconnects)
            Streaming()

    Streaming()
    time.sleep(0)
    


