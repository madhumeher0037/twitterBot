import Auth
import util
import news
import Palm
import time

client = Auth.V2_Auth()
articles = news.get_news()
for article in articles:
    try:
        title = article.get('title')
        print("title "+title)
        Hashtags = Palm.command(title+"Give three hastags in a single line without extra new lines.If you are not able to give just give an output #news")
        url = article.get('link')
        util.tweet(client,title+" "+Hashtags+" "+url)
        time.sleep(40)
    except Exception as inst:
        print(type(inst))    
