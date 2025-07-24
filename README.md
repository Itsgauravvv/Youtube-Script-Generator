# YouTube Script Generator 🚀

This project uses LangChain and Streamlit to automatically generate a title and a full video script for a YouTube video based on a user-provided topic.

## ✨ Features

-   **Topic-based Generation**: Simply provide a topic and get a script.
-   **AI-Powered Titles**: Generates creative, click-worthy titles.
-   **Factual Grounding**: Uses Wikipedia to fetch background information, ensuring the script is factually grounded.
-   **Customizable Output**: Adjust the script's tone, length, and language.
-   **Web Interface**: Easy-to-use UI built with Streamlit.
-   **History**: Keeps a log of your recent generations in the current session.

## ⚙️ Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd youtube-script-generator
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API Key:**
    -   Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey).
    -   Create a file named `.env` in the root directory of the project.
    -   Add your API key to the `.env` file like this:
        ```
        GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"
        ```

## ▶️ How to Run

Once you've installed the dependencies and set up your API key, run the Streamlit app with the following command:

```bash
streamlit run app.py