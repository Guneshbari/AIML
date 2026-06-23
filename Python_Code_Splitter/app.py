from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

python_code = """
def hello_world():
    print("Hello, World!")

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
"""

python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=100, chunk_overlap=0
)

docs = python_splitter.create_documents([python_code])

for i, doc in enumerate(docs):
    print(f"--- Chunk {i+1} ---")
    print(doc.page_content)
