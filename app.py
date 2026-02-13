import streamlit as st
from weather import get_weather
from datetime import datetime
from semantic_search import load_model_and_index, search_news
import json
import os

st.set_page_config(page_title="AI News Aggregator & Summarizer",layout="wide")
st.markdown("""
<style>
@keyframes gradientMove {
  0% {background-position: 0% 50%;}
  50% {background-position: 100% 50%;}
  100% {background-position: 0% 50%;}
}
.main-title {
    font-size: 42px;
    font-weight: 800;
    background: linear-gradient(90deg, #00C9FF, #92FE9D, #FF6B6B, #FFD93D);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientMove 6s ease infinite;
    margin-bottom: 10px;
}
.section-container {
    background:linear-gradient(90deg, #00C9FF, #92FE9D);
    padding:12px 20px;
    border-radius:10px;
    margin-top:30px;
    margin-bottom:5px;
}
.section-text { font-size: 20px; font-weight: 700; color: black; }

.result-card {
    padding: 20px;
    border-radius:14px;
    background-color:#1E222B;
    margin-bottom:15px;
    color:#F5F5F5;
    transition:transform 0.2s, box-shadow 0.2s;
}
.result-card:hover {
    transform:translateY(-5px);
    box-shadow:0 10px 25px rgba(0,0,0,0.6);
}

.summary-box {
    padding: 20px;
    border-radius: 14px;
    background-color: #16213E;
    color: white;
    margin-bottom: 20px;
}

.meta { 
        font-size: 14px; 
        color: #B0B3B8;
        margin-bottom: 10px;
        }
.score-badge { 
        float: right; 
        background-color: #00C9FF; 
        color: black; 
        padding: 4px 10px; 
        border-radius: 20px; 
        font-size: 13px; 
        font-weight: 600;
        }

.category-badge { 
    padding: 4px 10px; 
    border-radius: 12px;
    font-size: 12px; 
    font-weight: bold; 
    }
.category-sports { 
    background-color:#F6B6B; 
    color: white; 
    }
.category-politics { 
    background-color:#FFD93D; 
    color: black; 
    }
.category-technology {
    background-color:#4ECDC4;
    color: black; 
    }
.category-business { 
    background-color:#1A535C;
    color: white; 
    }
.category-entertainment { 
    background-color:#FF6BFF; 
    color: white; }
.category-all { 
    background-color:#92FE9D;
    color: black; }

.read-more { 
    color: #00C9FF; 
    text-decoration:none; 
    font-weight:bold; }

h3 { 
    border-bottom: 2px solid #00C9FF;
    padding-bottom:5px;
    margin-top:30px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📰 AI-Powered News Explorer</div>',unsafe_allow_html=True)
today = datetime.now()
current_day = today.strftime("%A")
current_date = today.strftime("%d %B %Y")

weather_info, detected_city = get_weather()

st.markdown(f"""
<style>
.weather-bar {{
    font-size:16px;
    margin-bottom:18px;
    padding:8px 0;
    font-weight:500;
    color:#111111 !important;
    opacity:1 !important;
    letter-spacing:0.4px;
    display:flex;
    gap:18px;
    align-items:center;
    animation: fadeIn 0.8s ease-in-out;
}}

.weather-item {{
    display:flex;
    align-items:center;
    gap:6px;
    transition: all 0.3s ease;
}}

.weather-item:hover {{
    transform: translateY(-2px);
    color:#000000;
}}

@keyframes fadeIn {{
    from {{ opacity:0; transform: translateY(-5px); }}
    to {{ opacity:1; transform: translateY(0); }}
}}
</style>
<div class="weather-bar">
📅 {current_day}, {current_date}
&nbsp;&nbsp; | &nbsp;&nbsp;
📍 {detected_city if detected_city else "Unknown"}
&nbsp;&nbsp; | &nbsp;&nbsp;
🌤 {weather_info}
</div>
""", unsafe_allow_html=True)
st.write("Multi-query semantic search with AI-style summaries.")

st.sidebar.title("⚙️ Settings")
top_k = st.sidebar.slider("Results per query", 1, 10, 5)
categories = ["All", "Sports", "Politics", "Technology", "Business", "Entertainment","Health","Weather"]
selected_category = st.sidebar.selectbox("Filter by Category", categories)

FAV_FILE = "favorites.json"

if 'favorites' not in st.session_state:
    if os.path.exists(FAV_FILE):
        with open(FAV_FILE, "r", encoding="utf-8") as f:
            st.session_state.favorites = json.load(f)
    else:
        st.session_state.favorites = []

st.sidebar.markdown("### 💾 Favorites")
if st.session_state.favorites:
    for fav in st.session_state.favorites[-5:]:
        st.sidebar.markdown(f"- [{fav['title']}]({fav.get('link','#')})")
else:
    st.sidebar.write("No favorites yet.")

@st.cache_resource
def load_resources():
    return load_model_and_index()
model, index, news = load_resources()

def parse_date(pub_date_str):
    try:
        return datetime.fromisoformat(pub_date_str.replace("Z","")).strftime("%b %d, %Y %H:%M")
    except:
        return pub_date_str

def get_category_class(category):
    cat = category.lower() if category else "all"
    return f"category-{cat}" if cat in ["sports","politics","technology","business","entertainment","Health","Weather"] else "category-all"

def fav_key(item, section):
    safe_title = item['title'].replace(" ", "_")
    safe_source = item['source'].replace(" ", "_")
    return f"{section}_{safe_title}_{safe_source}"

def toggle_favorite(item):
    is_fav = any(
        f['title']==item['title'] and f['source']==item['source']
        for f in st.session_state.favorites
    )
    if is_fav:
        st.session_state.favorites = [
            f for f in st.session_state.favorites
            if not (f['title']==item['title'] and f['source']==item['source'])
        ]
    else:
        st.session_state.favorites.append(item)

    with open(FAV_FILE, "w", encoding="utf-8") as f:
        json.dump(st.session_state.favorites, f, ensure_ascii=False, indent=2)

    st.rerun()

if 'queries' not in st.session_state:
    st.session_state.queries = []

query = st.text_area("🔍Search for topics (one per line)",
                     value="\n".join(st.session_state.queries))

if st.button("Search"):
    st.session_state.queries = [q.strip() for q in query.split("\n") if q.strip()]

for q in st.session_state.queries:
    st.markdown(f"""
    <div class="section-container">
        <div class="section-text">
            🔎 Results for: {q} | Category: {selected_category}
        </div>
    </div>
    """, unsafe_allow_html=True)

    results_all = search_news(q, model, index, news, k=len(news))

    results = [
        r for r in results_all
        if selected_category=="All" or
        selected_category.lower() in (r['title']+r.get('summary','')).lower()
    ][:top_k]

    if not results:
        st.error("No relevant articles found.")
        continue

    summary_lines = []
    for idx, r in enumerate(results, start=1):
        summary_text = r.get("summary","").strip() or r.get("title","")
        summary_lines.append(f"{idx}. {summary_text}")

    st.markdown(f"""
    <div class="summary-box">
        <b>🤖 AI Generated Summary</b><br><br>
        {"<br>".join(summary_lines)}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3>🔥 Trending Articles</h3>", unsafe_allow_html=True)
    trending_sorted = sorted(results, key=lambda x: x["score"], reverse=True)[:3]

    for item in trending_sorted:
        pub_time = parse_date(item.get("published_at",""))
        category_class = get_category_class(item.get("category","All"))

        key = fav_key(item, "trend")
        is_fav = any(f['title']==item['title'] and f['source']==item['source']
                     for f in st.session_state.favorites)

        heart = "💖" if is_fav else "🤍"
        col1, col2 = st.columns([0.05,0.95])
        with col1:
            if st.button(heart, key=key):
                toggle_favorite(item)

        with col2:
            st.markdown(f"""
            <div class="result-card">
                <span class="category-badge {category_class}">
                {item.get("category","All")}</span>
                <span class="score-badge">Relevance: {item['score']}</span>
                <h4>{item['title']}</h4>
                <div class="meta">
                🌐 {item['source']} | 📅 {pub_time}
                </div>
                <div>{item.get('summary','')}</div>
                <a href="{item.get('link','#')}" target="_blank"
                class="read-more">🔗 Read More</a>
            </div>
            """, unsafe_allow_html=True)

    rec_results = search_news(q, model, index, news, k=10)
    recommended = [r for r in rec_results if r not in results][:5]

    if recommended:
        st.markdown("<h3>💡 You Might Also Like</h3>", unsafe_allow_html=True)

        for item in recommended:
            pub_time = parse_date(item.get("published_at",""))
            category_class = get_category_class(item.get("category","All"))

            key = fav_key(item, "rec")
            is_fav = any(f['title']==item['title'] and f['source']==item['source']
                         for f in st.session_state.favorites)

            heart = "💖" if is_fav else "🤍"
            col1, col2 = st.columns([0.05,0.95])
            with col1:
                if st.button(heart, key=key):
                    toggle_favorite(item)
            with col2:
                st.markdown(f"""
                <div class="result-card">
                    <span class="category-badge {category_class}">
                    {item.get("category","All")}</span>
                    <span class="score-badge">Relevance: {item['score']}</span>
                    <h4>{item['title']}</h4>
                    <div class="meta">
                    🌐 {item['source']} | 📅 {pub_time}
                    </div>
                    <div>{item.get('summary','')}</div>
                    <a href="{item.get('link','#')}" target="_blank"
                    class="read-more">🔗 Read More</a>
                </div>
             """, unsafe_allow_html=True)
