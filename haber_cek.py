import feedparser
import time

def news():

    rss_url = "https://www.cnnturk.com/feed/rss/ekonomi/news"
    feed = feedparser.parse(rss_url)
    for entry in feed.entries:
        baslik = entry.title 
        aciklama = entry.description
        hepsi = print(baslik + aciklama + "\n")

news()