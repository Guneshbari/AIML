from langchain_community.document_loaders import PyPDFLoader

file_path = "./attention_all_you_need.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()
print(docs)
print(docs[0].metadata)
print(docs[0].page_content)
