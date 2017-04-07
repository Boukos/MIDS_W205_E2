import tweepy

consumer_key = "07u598kFNd8DvnMe2QXKbjen7";

consumer_secret = "s2othH0iKZIZOBowsWJrszplwdaAxFM2LkBPYkcW9HslnHp8rR";

access_token = "843949480885940224-fE9RXQfcOzHdKMKljDNb7RdGRWn4MDw";

access_token_secret = "b3RYo2qRHVgoFpUYp8WHUKGtmlJkEwODyil3xPbu6hUXH";



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



