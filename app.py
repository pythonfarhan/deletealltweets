import twitter
from _constants import *
import time


# authentication
def auth():
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)
    return api

# get tweet IDs
def getTweetId(username):
    try:
        api = auth()
        tweets = api.GetUserTimeline(screen_name=username, count=200)
        result = list()
        for i in tweets:
            result.append(i['id'])
        return result
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


if __name__ == '__main__':
    deleteAllTweets()