import os
import sys
from langchain_community.document_loaders import PyPDFLoader

# Resolve path relative to the script's directory for portability
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "attention_all_you_need.pdf")

if not os.path.exists(file_path):
    print(f"Error: PDF file not found at: {file_path}")
    print("Please place 'attention_all_you_need.pdf' in the same directory as this script.")
    sys.exit(1)

loader = PyPDFLoader(file_path)
docs = loader.load()
print(docs)
print(docs[0].metadata)
print(docs[0].page_content)
