# PDF Document Splitter

A simple Python application that uses the LangChain community loaders and text splitters to split a PDF document into smaller semantic chunks (sub-documents).

## Project Files

*   [app.py](./app.py): Python script that configures the PDF loader, initializes `RecursiveCharacterTextSplitter` with chunk size and overlap, and splits the documents.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `langchain-text-splitters` and `pypdf`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd PDF_Document_Splitter
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Place a PDF File:**
    Put a PDF file named `attention_all_you_need.pdf` in this directory (or edit the path inside `app.py`).

## Usage

Run the PDF document splitter:
```bash
python app.py
```

The script will load the PDF, split it recursively into smaller text chunks, and print the sub-documents array, the total count of sub-documents generated, and the metadata of the first chunk.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Document Loader**: Imports `PyPDFLoader` from `langchain_community.document_loaders`.
2.  **Text Splitter**: Imports `RecursiveCharacterTextSplitter` from `langchain_text_splitters`.
3.  **Splitting Parameters**: Configures `chunk_size=2000` characters and `chunk_overlap=200` characters to maintain context overlap.
4.  **Execution**: Calls `text_splitter.split_documents(doc)` to parse and chunk the loaded document pages.
