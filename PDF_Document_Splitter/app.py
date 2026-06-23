import os
import sys
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Resolve path relative to the script's directory for portability
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "attention_all_you_need.pdf")

if not os.path.exists(file_path):
    print(f"Error: PDF file not found at: {file_path}")
    print("Please place 'attention_all_you_need.pdf' in the same directory as this script.")
    sys.exit(1)

loader = PyPDFLoader(file_path)
doc = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=200,
)

all_splits = text_splitter.split_documents(doc)
print(all_splits)
print(f"Paper split into {len(all_splits)} sub-documents.")
print(f"Metadata: {all_splits[0].metadata}")
