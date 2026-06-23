# Python Code Splitter

A Python application demonstrating code-splitting capabilities using LangChain text splitters. It loads a local Python source file and recursively splits it into semantic chunks based on Python syntax.

## Project Files

*   [app.py](./app.py): Python script that loads a file using `TextLoader`, configures `RecursiveCharacterTextSplitter` for Python language syntax with chunk size 500 and overlap 50, splits it, and prints the first two chunks.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `langchain-community` and `langchain-text-splitters`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Python_Code_Splitter
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Place a Python File:**
    Ensure a Python file named `tool_calling.py` is present in this directory (or edit the path inside `app.py`).

## Usage

Run the Python code splitter:
```bash
python app.py
```

The script will load the source file, split it into chunks, and output the total chunk count along with the contents of the first two chunks to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Document Loader**: Imports `TextLoader` from `langchain_community.document_loaders` to read the local code file.
2.  **Language Splitter**: Imports `Language` enum and `RecursiveCharacterTextSplitter` from `langchain_text_splitters`.
3.  **Language Rules Configuration**: Initializes `RecursiveCharacterTextSplitter` with `Language.PYTHON`, chunk size 500, and chunk overlap 50.
4.  **Splitting**: Calls `split_documents(documents)` to segment the loaded code document.
