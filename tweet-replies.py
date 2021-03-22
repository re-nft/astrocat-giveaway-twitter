import tweepy
import time
import os
from collections import defaultdict
from dotenv import load_dotenv, find_dotenv
env = load_dotenv(find_dotenv(), override=True)

# Save your tokens in .env file
con_key = os.getenv('TWITTER_API_KEY')
con_sec = os.getenv('TWITTER_API_SECRET_KEY')
acc_tok = os.getenv('TWITTER_ACCESS_TOKEN')
acc_sec = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')


# Initialize tweepy
auth = tweepy.OAuthHandler(con_key, con_sec)
auth.set_access_token(acc_tok, acc_sec)

api = tweepy.API(auth)


# Sample teets
# Tweet 1 (refer as T1)
# https://twitter.com/bozu_108/status/1090475718335578112
# Tweet 2 (refer as T2)
# https://twitter.com/bozu_108/status/1090501639625072640
# In this sample, we try to get replies to T1,
# since T1 until T2.


# Preparation
TARGET_TWEET_ID = 1373035871977410560  # T1
OLDEST_ID = 1373761360773849092 # T2 < this is wher Nick says closed. so we need all the replies
# in between the announcing tweet and the close tweet
search_term = '@renftlabs'  # Target tweet's user name
no_match, not_reply, match = 'No Match', 'Not Reply', 'Match'
counts = {no_match: 0, not_reply: 0, match: 0}
matched_texts = defaultdict(int)


# Repeat the api multiple times to try to get all replies
# You may want to change the repetition times, or stop it mannualy (if using jupyter notebook)
for i in range(1):
    print('loop', i, counts)
    time.sleep(5)  # API Limit: 180req / 15min(900sec)
    result_tweets = api.search(search_term, count=100, since_id=TARGET_TWEET_ID, max_id=OLDEST_ID)

    for tweet in result_tweets:
      	# Reflesh OLDEST_ID
        OLDEST_ID = min(tweet.id, OLDEST_ID)
        if tweet.in_reply_to_status_id == TARGET_TWEET_ID:
            counts[match] += 1
            matched_texts[tweet.text] += 1
        elif tweet.in_reply_to_status_id is None:
            counts[not_reply] += 1
        else:
            counts[no_match] += 1

f = open("responses-raw.csv", "a")
f_ = open("responses.csv", "a")

for tweet in matched_texts.keys():
  f.write(f"[START]{tweet}[END]\n")
  f_.write()

f.close()

# # Show results
# for text, count in sorted(matched_texts.items(), key=lambda x: x[1], reverse=True):
#     print('{:>4}\t{}'.format(count, text))
