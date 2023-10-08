import Twiiter_Keys as keys
import tweepy as tw
# V2 APi Twitter Authentication
def V2_Auth():
     client = tw.Client(
        keys.bearer_token,
        keys.consumer_key,
        keys.consumer_secret,
        keys.access_token,
        keys.access_token_secret,
        wait_on_rate_limit=True
     )
     return client
     
        