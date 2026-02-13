import json
from nltk.tokenize import sent_tokenize

def compress_text(text, max_sentences=5, max_chars=500):
    text = text.split("[+")[0]
    sentences = sent_tokenize(text)
    summary = " ".join(sentences[:max_sentences])
    return summary[:max_chars]

def compress_articles(input_file="articles_rss.json",output_file="compressed_news.json"):
    with open(input_file, "r", encoding="utf-8") as f:
        articles = json.load(f)
    compressed_articles = []
    for art in articles:
        compressed = compress_text(art["content"])
        compressed_articles.append({
            "title": art["title"],
            "source": art["source"],
            "link": art["link"],
            "published_at": art["published_at"],
            "compressed_text": compressed
        })
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(compressed_articles, f, indent=2)
    print(f"Saved {len(compressed_articles)} compressed articles to {output_file}")

if __name__ == "__main__":
    compress_articles()
