import csv
import tweepy
import ssl
from datetime import datetime

#https://stackoverflow.com/questions/52307443/how-to-get-the-replies-for-a-given-tweet-with-tweepy-and-python

ssl._create_default_https_context = ssl._create_unverified_context

# Oauth keys
consumer_key = 'eC5TP6uUDa2s3MXXGaXvmLFmA'
consumer_secret = 'Oh1CFSAk0cfISybrw5rDe1g7WbeyWf0hARYnF5wEnsFegZtRD2'
access_token = '1397365651702829057-ExooHgpInX0DG0pj5CxPzsulufGXrX'
access_token_secret = '1UDeXdNey3jJIEiYLL4bnJfJ5wHRR0amv9v0daEeCUTlg'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

### Redirect user to Twitter to authorize
##redirect_user(auth.get_authorization_url())

# Get access token
# Construct the API
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True) # this is to avoid 429 error for too frequent request


def scraper_single(name,tweet_id,since_date,end_date):
    replies=[]
    for tweet in tweepy.Cursor(api.search,q='to:{}'.format(name), since_id = tweet_id, since=since_date,end=end_date,tweet_mode='extended').items(10000):
        # search for any tweets that are more recent than this id, and then only within this time peirod 
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            #print("has replies")
            #print(tweet.in_reply_to_status_id_str)
            if (tweet.in_reply_to_status_id_str==tweet_id):
                replies.append(tweet)
    print(len(replies))
              
    with open('replies.csv', 'a') as f:
        csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
        csv_writer.writeheader()
        for tweet in replies:
            tweet.full_text
            row = {'user': tweet.user.screen_name, 'text': tweet.full_text.replace('\n', ' ')}
            csv_writer.writerow(row)

def scraper_multiple(num_tweet):
    for j in range(num_tweet):
        scraper_single(name[j],tweet_id[j],since_date[j],end_date[j])

name = ['@nytimes','@GavinNewsom','CDCgov','thehill']
tweet_id = ['1398028759534551041','1400529612023558144','1392911350058323973','1400225221135810567']
since_date = ['2021-05-27','2021-06-03','2021-05-13','2021-06-02']
end_date = ['2021-05-28','2021-06-03','2021-05-14','2021-06-03']

#scraper_multiple(len(name))

startTime = datetime.now()
scraper_single(name[3],tweet_id[3],since_date[3],end_date[3])
print(datetime.now()-startTime)
