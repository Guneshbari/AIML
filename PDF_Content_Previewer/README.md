# PDF Content Previewer

A simple Python application that uses the LangChain community document loaders to read, parse, and preview the contents and metadata of a PDF file (e.g., standard academic papers like *Attention Is All You Need*).

## Project Files

*   [app.py](./app.py): Python script that configures the PDF loader and prints metadata and page content of the first page.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `langchain-community` and `pypdf`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd PDF_Content_Previewer
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Place a PDF File:**
    Put a PDF file named `attention_all_you_need.pdf` in this directory (or edit the path inside `app.py`).

## Usage

Run the PDF content previewer:
```bash
python app.py
```

The script will load the PDF, print the document representations, print the metadata of the first page, and print the parsed text content of the first page to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Document Loader**: Imports `PyPDFLoader` from `langchain_community.document_loaders`.
2.  **Loading**: Initializes the loader with a local file path (`./attention_all_you_need.pdf`) and executes `loader.load()`.
3.  **Previewing**: Prints parsed document page representations, page metadata dictionary (e.g., source and page number), and the raw string content of the first page.
