def tweet(client,message):
    client.create_tweet(text = message)
    print('tweeted')