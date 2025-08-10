import streamlit as st
import asyncio
import sys
from crawler_file import crawl
from main import query_vector_store, create_vector_store

# Windows fix for asyncio event loop
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

# --- Step 1: Input URL ---
st.sidebar.title("Upload URL Here")
url = st.sidebar.text_input("Provide the URL that you wish to talk with", value="")

# --- Step 2: Crawl Button ---
if st.sidebar.button("Upload"):
    if not url.strip():
        st.sidebar.error("Please provide a valid URL.")
    else:
        st.sidebar.info("Working on it... crawling website")
        # Run the async crawler
        asyncio.run(crawl(url))
        st.sidebar.success("Crawling completed! Data saved to /data folder")

        # Create the vector store from crawled data
        st.sidebar.info("Creating vector store...")
        create_vector_store()  # Pass your folder path
        st.sidebar.success("Vector store created successfully!")


st.title("WebWhisper")
st.header("Talk to any website like it’s a person")

#----------------------------- chat UI
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

user_chat = st.chat_input("ask something")

for chat in st.session_state["chat_history"]:
    with st.chat_message(chat['role']):
        st.write(chat['content'])

if user_chat:
    st.session_state["chat_history"].append({
        'role' : "human",
        'content' : user_chat
    })
    with st.chat_message("human"):
        st.text(user_chat)

    result = query_vector_store(user_chat)
    with st.chat_message("ai"):
        st.write(result)

    st.session_state["chat_history"].append({
        'role' : "ai",
        'content' : result
    })