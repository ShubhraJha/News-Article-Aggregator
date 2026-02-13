# AI News Aggregator & Summarizer – Project Documentation

## 1. Project Overview
The **AI News Aggregator & Summarizer** is an intelligent platform that aggregates news from multiple global and Indian sources, compresses content, and delivers relevant results through embedding-based semantic search.  

It allows users to perform multi-query semantic searches, receive AI-style summaries, and access trending or personalized articles in real-time.  

This project combines web scraping, NLP, vector search, and Streamlit UI development into a cohesive news intelligence system.

---

## 2. Motivation
Traditional news platforms often rely on simple keyword searches, which may fail to capture context or relevance. This project leverages **Natural Language Processing (NLP)** and **vector embeddings** to:  

- Understand semantic meaning behind user queries  
- Provide concise and informative summaries  
- Enable multi-source news aggregation  
- Personalize results based on location and trending topics  

---

## 3. Features

### Core Features
1. **Multi-Query Semantic Search**  
   - Input multiple search queries (one per line)  
   - Semantic search using sentence embeddings and vector similarity  
   - Returns most relevant articles beyond keyword matching  

2. **Intelligent Article Extraction**  
   - RSS feed ingestion  
   - Full-text extraction using `newspaper3k`  
   - Fallback summaries if extraction fails  

3. **Smart Text Compression**  
   - Tokenization into sentences  
   - Key sentence selection for concise summaries  
   - Character limit for improved embedding accuracy  

4. **AI-Style Summarized Output**  
   - Clean, readable article summaries  
   - Shows source, publish date, and direct article link  

5. **Trending & Recommendations**  
   - Sorts articles by relevance score  
   - Suggests similar content dynamically  

6. **Live Weather Personalization**  
   - Detects user location via IP  
   - Fetches real-time weather using OpenWeather API  
   - Displays temperature and weather condition on the interface  

---

## 4. News Sources Integrated
The application currently supports a mix of global and Indian news sources:

- **Global:** BBC News, The New York Times, The Guardian, Al Jazeera, CNN, The Economist, The Washington Post, NPR  
- **India:** Hindustan Times, The Times of India, India Today, LiveMint, Indian Express  
- **Tech & Business:** TechCrunch  

---

## 5. Project Architecture
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


## 6. File Structure & Description

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit app. Handles UI, queries, result display, favorites, and weather info. |
| `fetch_news.py` | News ingestion pipeline. Fetches RSS feeds, extracts articles, compresses text, and saves `compressed_news.json`. |
| `semantic_search.py` | Embedding model loader and search engine. Creates FAISS index, performs similarity search. |
| `compressed_news.json` | Preprocessed dataset containing compressed news articles and metadata. |

## 7. Technologies Used
- **Programming Language:** Python  
- **Web Framework:** Streamlit  
- **RSS Parsing:** feedparser  
- **Article Extraction:** newspaper3k  
- **NLP:** NLTK, Sentence Transformers  
- **Vector Search:** FAISS  
- **Data Storage:** JSON  
- **APIs:** OpenWeather (for personalization)  

## 8. Installation & Setup
1. **Clone the repository**
   ```bash
   git clone <repo_url>
   cd AI-News-Aggregator  
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
3. **Download NLTK tokenize**
  import nltk
  nltk.download("punkt")
4. **Generate dataset**
  python fetch_news.py
5. **Run the Streamlit app**
  streamlit run app.py

## 9. Usage Instructions
-Enter one or multiple search queries in the search box.
-View ranked article results with AI-style summaries.
-Click article links to visit the original source.
-Personalized weather info displayed at the top.
-Trending and recommended articles appear dynamically.

## 10. Strengths of the Project
-Multi-source, real-time news aggregation
-NLP-based extractive summarization
-Semantic search beyond keywords
-Vector-based indexing and retrieval
-Interactive and user-friendly UI
-Personalization through live weather detection

## 11. Future Improvements
-Transformer-based abstractive summarization
-Cloud deployment (Streamlit Cloud or AWS)
-Integration with a database (PostgreSQL)
-User authentication and profiles
-News clustering for topic-based organization
-Auto-refresh to fetch latest news continuously

## 12. References
-Streamlit Documentation
-Newspaper3k Documentation
-Sentence Transformers
-FAISS Library
-OpenWeather API

## 13. Author
Shubhra Jha – AI & Web Developer
