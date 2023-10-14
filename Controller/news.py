
from gnewsclient import gnewsclient
 
client = gnewsclient.NewsClient(language='english', 
                                location='in', 
                                topic='Entertaiment', 
                                max_results=50)

def get_news():
    news_list = client.get_news()
    print(news_list)
    return news_list