import feedparser
from newspaper import Article
import json
import nltk
nltk.download("punkt")
FEEDS =[
    "http://feeds.bbci.co.uk/news/rss.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://www.theguardian.com/world/rss",
    "https://www.aljazeera.com/xml/rss/all.xml",
    "https://abcnews.com",
    "https://www.cnn.com/services/rss/",
    "https://www.hindustantimes.com/rss/topnews/rssfeed.xml",
    "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
    "https://www.indiatoday.in/rss/1206576",
    "https://www.livemint.com/rss/news",
    "https://www.economist.com/latest/rss.xml",
    "https://www.washingtonpost.com/rss/world",
    "https://www.npr.org/rss/rss.php?id=1001",
     "https://indianexpress.com", 
    "https://techcrunch.com/feed/"
]
def fetch_articles_from_feeds(feeds):
    articles=[]
    for feed_url in feeds:
        feed=feedparser.parse(feed_url)
        for entry in feed.entries:
            try:
                article = Article(entry.link)
                article.download()
                article.parse()
                content = article.text
            except:
                content = entry.summary if "summary" in entry else ""
            if content:
                articles.append({
                    "title": entry.title,
                    "source": feed.feed.title,
                    "link": entry.link,
                    "published_at": entry.get("published", ""),
                    "content": content
                })
    return articles
def save_articles(articles, filename="articles_rss.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2)
    print(f"Saved {len(articles)} articles to {filename}")

if __name__ == "__main__":
    articles = fetch_articles_from_feeds(FEEDS)
    save_articles(articles)
