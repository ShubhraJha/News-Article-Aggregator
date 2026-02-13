📰 AI News Aggregator & Summarizer

An AI-powered news aggregation and semantic search platform that collects real-time articles from multiple global news sources, intelligently compresses content, and delivers relevant results using embedding-based semantic search.

Built with Streamlit, RSS feeds, NLP, and vector similarity search.

🚀 Overview

- AI News Aggregator & Summarizer is a full-stack AI news application that:

- Aggregates news from multiple global RSS feeds

- Extracts full article content automatically

- Compresses articles using NLP

- Performs semantic similarity search

- Displays AI-style summarized results

- Provides trending and recommended articles

- Personalizes with live weather detection

This project combines web scraping, NLP, vector search, and UI development into one intelligent system.

🌍 News Sources Integrated

Articles are collected from major international and Indian sources including:

- BBC News

- The New York Times

- The Guardian

- Al Jazeera

- CNN

- Hindustan Times

- The Times of India

- India Today

- LiveMint

- The Economist

- The Washington Post

- NPR

- Indian Express

- TechCrunch

🧠 Core Features
🔎 Multi-Query Semantic Search

- Enter multiple search queries (one per line)

- Uses sentence embeddings + vector similarity

- Returns most relevant articles (not keyword match)

📰 Intelligent Article Extraction

- Uses RSS feeds

- Extracts full article text using newspaper3k

- Handles fallback summaries if extraction fails

✂️ Smart Text Compression

- Tokenizes article into sentences

- Selects first key sentences

- Limits max characters

- Improves embedding accuracy

🤖 AI-Style Summarized Output

- Displays compressed article text

- Clean readable format

- Shows source and publish date

- Provides direct article link

🔥 Trending & Recommendations

- Sorted by relevance score

- Suggested similar content

- Dynamic display logic

🌤 Live Weather Personalization

- Detects user location via IP

- Fetches real-time weather

- Displays temperature and condition

Powered by:

OpenWeather

🏗 Project Architecture
RSS Feeds
    ↓
Article Extraction
    ↓
Text Compression
    ↓
Embedding Generation
    ↓
FAISS Vector Index
    ↓
User Query
    ↓
Semantic Similarity Search
    ↓
Ranked Results Displayed in Streamlit

📂 Project Structure
AI-News-Aggregator-Summarizer/
│
├── app.py                # Main Streamlit UI
├── fetch_news.py         # RSS + article extraction + compression
├── semantic_search.py    # Embeddings + FAISS search engine
├── weather.py            # Location-based weather
├── compressed_news.json  # Stored compressed dataset
├── favorites.json        # Saved articles
└── requirements.txt

🔍 File Explanation
🔹 app.py

Main application file.

- Builds UI

- Handles user queries

- Calls semantic search

- Displays results

- Manages favorites

- Shows weather info

🔹 fetch_news.py

News ingestion pipeline.

- Fetches RSS feeds

- Extracts full article content

- Compresses text

- Builds dataset

- Saves to compressed_news.json

🔹 semantic_search.py

- Search engine logic.

- Loads embedding model

- Creates vector embeddings

- Builds FAISS index

- Performs similarity search
- 
🛠 Technologies Used

- Python

- Streamlit

- feedparser

- newspaper3k

- NLTK

- Sentence Transformers

- FAISS

- JSON storage

- REST APIs

▶️ How to Run
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Download NLTK tokenizer
import nltk
nltk.download("punkt")

3️⃣ Generate dataset
py fetch_news.py

4️⃣ Run the website
streamlit run app.py

🎯 What Makes This Project Strong

This project demonstrates:

- NLP-based preprocessing

- Extractive summarization

- Semantic retrieval

- Vector search indexing

- Multi-source web scraping

- Real-time data aggregation

- Interactive UI design

🔮 Future Improvements

- Transformer-based summarization

- Cloud deployment

- Database integration (MongoDB / PostgreSQL)

- User authentication

- News clustering

- Real-time auto refresh

- Deploy on Streamlit Cloud / AWS
  
👩‍💻 Author
Shubhra Jha
