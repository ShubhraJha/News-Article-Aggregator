import feedparser
from newspaper import Article
import json
import nltk
from nltk.tokenize import sent_tokenize
from datetime import datetime
nltk.download("punkt")
FEEDS = [
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
def fetch_articles(query=None):
    all_articles = []
    for feed_url in FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            try:
                article = Article(entry.link)
                article.download()
                article.parse()
                content = article.text
            except:
                content = entry.summary if "summary" in entry else ""
            if not content:
                continue
            if query:
                if query.lower() not in entry.title.lower() and query.lower() not in content.lower():
                    continue
            all_articles.append({
                "title": entry.title,
                "source": feed.feed.title,
                "link": entry.link,
                "published_at": entry.get("published", ""),
                "content": content
            })
    return all_articles
def compress_text(text,max_sentences=5, max_chars=500):
    from nltk.tokenize import sent_tokenize
    sentences = sent_tokenize(text)
    summary = " ".join(sentences[:max_sentences])
    return summary[:max_chars]
def build_dataset(query=None):
    articles = fetch_articles(query=query)
    dataset = []
    for article in articles:
        compressed = compress_text(article["content"])
        dataset.append({
            "title": article["title"],
            "source": article["source"],
            "published_at": article["published_at"],
            "compressed_text": compressed,
             "link": article.get("url", "") 
        })
    return dataset
if __name__ == "__main__":
    data = build_dataset(query=None)  
    filename = "compressed_news.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Saved {len(data)} compressed articles to {filename}")
