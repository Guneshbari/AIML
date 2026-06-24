# Docuchat with PDF

A Python application that demonstrates a Retrieval-Augmented Generation (RAG) pipeline. It reads a local PDF document, segments the text, generates vector embeddings using a HuggingFace model, indexes them in a local Chroma DB vector database, and uses the Google GenAI SDK via LangChain to answer questions about the document.

## Project Files

*   [app.py](./app.py): Python script that sets up document loading, splitting, vector database ingestion, query context retrieval, and conversational query invocation with Gemini.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `langchain-chroma` and `langchain-huggingface`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Docuchat_with_PDF
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Key:**
    Create a `.env` file in this directory and add your Google Gemini API Key:
    ```env
    GOOGLE_API_KEY=your_gemini_api_key_here
    ```

4.  **Place a PDF File:**
    Put a PDF file named `Attention_Is_All_You_Need.pdf` in this directory (or edit the path inside `app.py`).

## Usage

Run the document chat script:
```bash
python app.py
```

The script will index the document chunks into the local Chroma vector store inside `./chroma_langchain_db`, perform similarity search based on the query *"What improvements have been made to attention mechanisms since 2017?"*, send the matched chunks to Gemini, and output the final answer to the terminal.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API key using `python-dotenv`.
2.  **Document Loader & Splitter**: Imports `PyPDFLoader` to parse the PDF, and `RecursiveCharacterTextSplitter` to chunk the text.
3.  **Vector Embeddings**: Uses `HuggingFaceEmbeddings` with the `sentence-transformers/all-mpnet-base-v2` model to turn text chunks into vectors.
4.  **Chroma Storage**: Ingests and stores vectors into a local directory (`./chroma_langchain_db`) using `Chroma`.
5.  **Context Retrieval**: Implements `retrieve_context(query, k=2)` to find the top $k$ relevant chunks for the user's question.
6.  **Answer Generation**: Feeds the context chunks and user question as system and user messages into the `google_genai:gemini-2.5-flash` model using LangChain's `init_chat_model` and retrieves the final text response.
