# src/generator/utils.py

import wikipediaapi
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def get_wikipedia_summary(topic: str, lang: str = 'en') -> str:
    """
    Fetches a concise summary of a topic from Wikipedia.

    Args:
        topic (str): The topic to search for.
        lang (str): The language code for Wikipedia (e.g., 'en', 'es', 'fr').

    Returns:
        str: A summary of the topic, or an error message if not found.
    """
    try:
        # Initialize Wikipedia API with a user-agent
        wiki_wiki = wikipediaapi.Wikipedia(
            user_agent="YouTubeScriptGenerator/1.0",
            language=lang
        )

        page = wiki_wiki.page(topic)

        if not page.exists():
            logging.warning(f"Wikipedia page for topic '{topic}' not found.")
            return f"No information found for '{topic}'. The topic might be too specific or misspelled."

        # Return the first 3 paragraphs of the summary (approx. 300-400 words)
        summary = "\n".join(page.summary.split('\n')[:3])
        logging.info(f"Successfully fetched Wikipedia summary for '{topic}'.")
        return summary

    except Exception as e:
        logging.error(f"An error occurred while fetching from Wikipedia: {e}")
        return f"An error occurred while fetching information for '{topic}'. Please check your connection or the topic."