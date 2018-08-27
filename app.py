import twitter
from _constants import *
import time
import datetime


# authentication
def auth():
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)
    return api

# get tweet IDs
def getTweetId(username):
    api = auth()
    try:
        tweets = api.GetUserTimeline(screen_name=username, count=200)
        result = list()
        ids = list()
        for i in range(len(tweets)):
            result.append(tweets[i])
        for id in range(len(result)):
            ids.append(result[id].id)
        return ids
    except Exception as e:
        print('Oops something error: ', e)
        print('Please wait..')
        time.sleep(60)
        pass

# delete tweets
def deleteAllTweets():
    tweetIds = []
    api = auth()
    while True:
        if len(tweetIds) != 0:
            try:
                for id in tweetIds:
                    api.DestroyStatus(id)
                    print('%s was deleted' % id)
                    time.sleep(5)
            except Exception as e:
                print('Oops something error: ', e)
                print('please wait..')
                time.sleep(60)
                pass
        else:
            try:
                tweetIds = getTweetId(username=username)
                print('tweets reloaded')
                if len(tweetIds) == 0:
                    print('---task done---')
                    break
            except Exception as e:
                print('Oops something error: ', e)
                print('please wait..')
                time.sleep(60)
                pass

def run():
    day = datetime.datetime.today().weekday()
    hour = datetime.datetime.today().time().hour
    minute = datetime.datetime.today().time().minute

    def switch(hari=str()):
        hari = hari.lower()
        switcher = {
            'senin': 0,
            'selasa': 1,
            'rabu': 2,
            'kamis': 3,
            'jumat': 4,
            'sabtu': 5,
            'minggu': 6
        }
        return switcher.get(hari, 6)

    while True:
        if day == switch(hari) and str(hour) == str(jam) and str(minute) == str(menit):
            deleteAllTweets()
        else:
            print('waiting..')
            time.sleep(5)


if __name__ == '__main__':
    deleteAllTweets()

