# src/generator/chain.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables from .env file
load_dotenv()

# Ensure the Google API key is set
if "GOOGLE_API_KEY" not in os.environ:
    raise ValueError("Google API Key not found in .env file. Please set GOOGLE_API_KEY.")

# Initialize the LLM (Google's Gemini Pro)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.7)

def generate_youtube_content(topic: str, tone: str, length: str, language: str, wikipedia_summary: str):
    """
    Generates a YouTube video title and script using LLM chains.

    Args:
        topic (str): The main topic of the video.
        tone (str): The desired tone for the script (e.g., 'Witty', 'Informative').
        length (str): The desired length of the script (e.g., '5-minute', '10-minute').
        language (str): The language of the script.
        wikipedia_summary (str): Background information from Wikipedia.

    Returns:
        dict: A dictionary containing the generated 'title' and 'script'.
    """
    # --- Title Generation Chain ---
    title_template = PromptTemplate(
        input_variables=['topic', 'language'],
        template="Generate 5 creative, click-worthy YouTube video titles in {language} about the topic: '{topic}'."
    )
    title_chain = LLMChain(llm=llm, prompt=title_template, output_key="title")

    # --- Script Generation Chain ---
    script_template = PromptTemplate(
        input_variables=['title', 'wikipedia_summary', 'tone', 'length', 'language'],
        template="""
        You are an expert YouTube scriptwriter. Create a compelling and engaging video script in {language}.

        Video Title: {title}
        Background Research (from Wikipedia): {wikipedia_summary}

        Instructions:
        1.  **Introduction**: Start with a strong hook to grab the viewer's attention. Introduce the topic and what the video will cover.
        2.  **Main Body**: Expand on the topic using the background research provided. Structure it into clear, logical sections. Use a {tone} tone throughout.
        3.  **Conclusion**: Summarize the key points and end with a strong call to action (e.g., "subscribe," "comment," "watch another video").
        4.  **Formatting**: The script should be formatted clearly, with headings for Intro, Main Body, and Conclusion.
        5.  **Length**: The final script should be appropriate for a {length} video.
        """
    )
    script_chain = LLMChain(llm=llm, prompt=script_template, output_key="script")

    # Run the chains
    title_output = title_chain.run({'topic': topic, 'language': language})
    
    # We select the first title from the generated list
    first_title = title_output.split('\n')[0]

    script_output = script_chain.run({
        'title': first_title,
        'wikipedia_summary': wikipedia_summary,
        'tone': tone,
        'length': length,
        'language': language
    })

    return {'title': first_title, 'script': script_output}