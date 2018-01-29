import tweepy
from tweepy import OAuthHandler
from config import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_SECRET)


def get_twitter_api():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)


def fetch_statues(api, screen_name, count=20):
    user = None
    statuses = []

    _i = 0
    for c in tweepy.Cursor(
            api.user_timeline, screen_name=screen_name, lang='en',
            tweet_mode='extended').items():
        if not user:
            user = c.user

        if c.full_text.startswith('RT @'):  # Skip Re-tweets
            continue
        if 'https:' in c.full_text:         # Skip images/links
            continue

        statuses.append(c.full_text)
        _i += 1

        if _i == count:
            break

    return statuses, user
