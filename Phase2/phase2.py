import tweepy

auth = tweepy.OAuth1UserHandler(
   "UPQ8fdxW3DcaMIVT4MUJoWfzD", "pAdwr6zK7pCOtIUbrkq7JEe4VxnBW5CLhRNf2Je1TGXAHdpU9T","1562646739521511429-u9Cpv7E9rHucS3GMxrwk8kn1i4LC8O", "ywsmtVa7jiQ71ey0Ocqlkv1DfWVZmg9txuzqGy0YthG6H"
)

api = tweepy.API(auth)

keywords="wireless power transfer"
limit=100
tweets=api.search_tweets(q=keywords,count=limit)

for tweet in tweets:
   print(tweet.text)