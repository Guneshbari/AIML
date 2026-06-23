# Python Code Splitter

A Python application demonstrating code-splitting capabilities using LangChain text splitters. It dynamically parses and splits Python source code into separate logical chunks (functions/classes) based on Python syntax rules.

## Project Files

*   [app.py](./app.py): Python script that configures `RecursiveCharacterTextSplitter` from language rules, splits dummy code, and prints chunks.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `langchain-text-splitters`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Python_Code_Splitter
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the Python code splitter:
```bash
python app.py
```

The script will split the provided Python code block into semantic chunks and print each chunk output separated by boundaries to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Language Splitter**: Imports `Language` enum and `RecursiveCharacterTextSplitter` from `langchain_text_splitters`.
2.  **Language Rules Configuration**: Uses `RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON, chunk_size=100, chunk_overlap=0)` to create a splitter configured with python-specific separator tokens (like `def` or `class`).
3.  **Splitting**: Calls `create_documents` to segment the source code string.
