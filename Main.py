import Auth
import util
import news
import Bard

client = Auth.V2_Auth()
articles = news.get_news()
for article in articles:
    try:
        title = article.get('title')
        print("title "+title)
        Hashtags = Bard.command(title+"Give three hastags in a single line without extra new lines")
        url = article.get('link')
        util.tweet(client,title+" "+Hashtags+" "+url)
    except Exception as inst:
        print(type(inst))    
