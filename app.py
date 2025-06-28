# --- Fix for asyncio event loop in Streamlit ---
import asyncio
import threading

if threading.current_thread() is not threading.main_thread():
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())
# -----------------------------------------------

import streamlit as st
from crewai import Crew, Process
from task import research_task, write_task
from agents import news_researcher, news_writer

# Set page config for better aesthetics
st.set_page_config(page_title="Crew AI News Generator", page_icon="📰", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 0 15px rgba(0,0,0,0.05);
    }
    .stTextInput > div > div > input, .stNumberInput > div > div > input {
        font-size: 18px;
        padding: 10px;
        border-radius: 8px;
    }
    .stButton > button {
        background-color: #0077ff;
        color: white;
        font-weight: bold;
        padding: 0.6em 1.5em;
        border-radius: 8px;
        margin-top: 1em;
    }
    </style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='main'>", unsafe_allow_html=True)

    st.title("📰 Crew AI News Generator")

    st.write("🚀 **Generate a tech-focused news article** using AI agents. Just enter a topic and desired word count!")

    topic = st.text_input("🎯 Enter a topic", "AI in healthcare")
    word_count = st.number_input("📝 Desired word count", min_value=100, max_value=1000, step=50, value=300)

    if st.button("✨ Generate Article"):
        with st.spinner("⏳ Generating article... please wait..."):
            crew = Crew(
                agents=[news_researcher, news_writer],
                tasks=[research_task, write_task],
                process=Process.sequential,
            )
            result = crew.kickoff(inputs={'topic': topic, 'word_count': word_count})
            st.success("✅ Article generated successfully!")
            st.markdown(result)

    st.markdown("</div>", unsafe_allow_html=True)
