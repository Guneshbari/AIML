# Docuchat with Web Docs

A Python application demonstrating a Retrieval-Augmented Generation (RAG) pipeline that fetches documentation pages from the web, processes the content, generates vector embeddings, stores them inside a local Chroma database, and utilizes the Google GenAI SDK via LangChain to answer questions specifically based on the scraped pages.

## Project Files

*   [app.py](./app.py): Python script that configures `WebBaseLoader` to download web docs, chunks the text, creates embeddings, ingests them into Chroma DB, and runs conversational Q&A queries with Gemini.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `beautifulsoup4`, `langchain-chroma`, and `langchain-huggingface`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Docuchat_with_Web_Docs
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Key:**
    Create a `.env` file in this directory and add your Google Gemini API Key:
    ```env
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

## Usage

Run the web document chat script:
```bash
python app.py
```

The script will fetch the LangChain integration documentation URLs, segment the text, store the vectors in the local Chroma DB (`./chroma_langchain_db`), perform context-based similarity searches, and output Gemini's answers to several questions (e.g. regarding `HuggingFaceEmbeddings` and `OpenAIEmbeddings`) in the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API key using `python-dotenv`.
2.  **Document Scraper & Splitter**: Uses `WebBaseLoader` to scrape text from a list of URLs, and `RecursiveCharacterTextSplitter` to chunk the HTML text.
3.  **Vector Embeddings**: Uses `HuggingFaceEmbeddings` with the `sentence-transformers/all-mpnet-base-v2` model to turn text chunks into vectors.
4.  **Chroma DB Ingestion**: Ingests and stores vectors locally inside `./chroma_langchain_db`.
5.  **Conversational RAG Execution**: The `ask_about_pdf` function retrieves context chunks via similarity search, builds a system message with strict instruction to only rely on retrieved context, and invokes the `google_genai:gemini-2.5-flash` model.
