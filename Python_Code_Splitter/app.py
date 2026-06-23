from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

file_path = "./tool_calling.py"

loader = TextLoader(file_path)
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    language=Language.PYTHON, chunk_size=500, chunk_overlap=50
)

code_chunks = splitter.split_documents(documents)

print(len(code_chunks))
print(code_chunks[0].page_content)
print(code_chunks[1].page_content)
