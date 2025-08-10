# Web Whisper – LLM Powered Crawling & RAG Chat Application

Web-Whisper is an **LLM-powered Retrieval-Augmented Generation (RAG)** application that can **crawl websites, GitHub repositories, and official documents**, then let you **chat with the extracted content** in real-time.

Whether you want to explore documentation, understand a repository, or get insights from a live website — Web-Whisper makes it possible.

---

## 🚀 Features
- **URL Crawling** – Crawl any given URL up to a depth of 2 levels.
- **Chat with Crawled Data** – Ask questions and get context-aware answers.
- **Document-Friendly** – Upload or provide official documentation URLs and chat with them.
- **GitHub Repository Exploration** – Extract and query repository contents.
- **No Hallucination Mode** – If the answer is out of context, it will tell you directly.
- **Persistent Vector Store** – Data stored in a Chroma DB for fast retrieval.

---

## 📌 Example Use Cases
1. **Learn from Official Docs** – Provide a documentation URL (e.g., Crawl4AI docs) and ask detailed questions.
2. **GitHub Repo Analysis** – Explore repositories to understand all projects and code.
3. **Website Insights** – Crawl and chat with any live website to uncover in-depth details.
4. **Competitive Research** – Analyze competitors' public sites and repositories for insights.
5. **Knowledge Base Creation** – Turn any web content into a searchable, interactive knowledge base.

---

## 🛠 Tech Stack
- **Language:** Python
- **Web Crawling:** Crawl4AI
- **LLM:** Groq LLM (`openai/gpt-oss-120b`)
- **Embeddings:** OpenAI `text-embedding-3-small`
- **Vector Store:** ChromaDB
- **Framework:** LangChain
- **Frontend:** Streamlit
- **Parsing:** UnstructuredMarkdownLoader

---

## 📂 Project Structure
📦 CrawlMate
-- ┣ 📜 crawl_file.py # Async web crawler using Crawl4AI
-- ┣ 📜 main.py # Vector store creation & RAG pipeline
-- ┣ 📜 frontend.py # Streamlit chat UI
-- ┣ 📂 data # Crawled markdown files
-- ┣ 📂 chroma_db # Persistent vector store
-- ┗ 📜 requirements.txt # Dependencies

---

## 🖼 How To Use
- Input a URL in the sidebar.
- Ask Questions in the chat interface — get context-aware answers.

---

## 📌 Future Enhancements
- Support for PDF uploads.
- Integration with Jina AI for multi-page crawling.
- Support for multi-URL batch crawling.
- Adding summarization mode for quick overviews.

---

## ⚡ Installation & Usage

### 1️⃣ Clone the repo
```bash
git clone https://github.com/SunagMP/Web-Whisper.git
cd Web-Whisper
streamlit run frontend.py


