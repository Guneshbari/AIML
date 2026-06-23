from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

file_path = "./attention_all_you_need.pdf"
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
