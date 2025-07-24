# app.py

import sys
import os

# --- THIS IS THE CRITICAL FIX ---
# Add the project root directory to the Python path
# This ensures that 'src' can be imported as a module
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
# --------------------------------

import streamlit as st
from src.generator.chain import generate_youtube_content
from src.generator.utils import get_wikipedia_summary

# --- Page Configuration ---
st.set_page_config(
    page_title="YouTube Script Generator 🤖",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Session State Initialization ---
if 'history' not in st.session_state:
    st.session_state.history = []

# --- App Header ---
st.title("YouTube Script Generator 🤖")
st.markdown("Turn any topic into an engaging YouTube video script, complete with a title and background research.")

# --- Sidebar for Advanced Options ---
with st.sidebar:
    st.header("⚙️ Advanced Options")
    tone_options = ["Informative", "Witty & Humorous", "Inspirational", "Casual & Conversational", "Formal & Academic"]
    length_options = ["~3 minutes (Short)", "~7 minutes (Medium)", "~12 minutes (Long)"]
    language_options = ["English", "Spanish", "French", "German", "Japanese", "Hindi"]

    selected_tone = st.selectbox("Select Script Tone:", tone_options)
    selected_length = st.selectbox("Select Script Length:", length_options)
    selected_language = st.selectbox("Select Language:", language_options)

# --- Main Content Area ---
with st.form("script_form"):
    topic_input = st.text_input(
        "Enter your YouTube video topic:",
        placeholder="e.g., The history of artificial intelligence"
    )
    submit_button = st.form_submit_button("Generate Script ✨")

# --- Logic on Form Submission ---
if submit_button and topic_input:
    with st.spinner('Generating your script... This might take a moment.'):
        try:
            wiki_summary = get_wikipedia_summary(topic_input, lang=selected_language.split()[0][:2].lower())
            generated_content = generate_youtube_content(
                topic=topic_input,
                tone=selected_tone,
                length=selected_length,
                language=selected_language,
                wikipedia_summary=wiki_summary
            )
            st.session_state.history.insert(0, generated_content)

        except Exception as e:
            st.error(f"An error occurred: {e}")

# --- Display Latest Generated Script ---
if st.session_state.history:
    latest_generation = st.session_state.history[0]
    st.subheader("✅ Here's Your Generated Content:")
    st.markdown("### Generated Title")
    st.write(latest_generation['title'])
    st.markdown("### Generated Script")
    st.markdown(latest_generation['script'])
    st.download_button(
        label="Download Script as .txt",
        data=f"Title: {latest_generation['title']}\n\n{latest_generation['script']}",
        file_name=f"{topic_input}_script.txt",
        mime="text/plain"
    )

# --- Display History of Generations ---
if len(st.session_state.history) > 1:
    with st.expander("📜 View Generation History"):
        for i, content in enumerate(st.session_state.history[1:], 1):
            with st.container():
                st.info(f"**{i}. Title:** {content['title']}")
                st.caption(f"Script Snippet: {content['script'][:100]}...")