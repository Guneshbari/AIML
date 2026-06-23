import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

# Resolve path relative to the script's directory for portability
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "tool_calling.py")

# Create a dummy python file if it doesn't exist so the script runs out of the box
if not os.path.exists(file_path):
    dummy_code = """# Dummy tool calling python code for demonstration
def add_numbers(a: int, b: int) -> int:
    \"\"\"Add two numbers together.\"\"\"
    return a + b

def multiply_numbers(a: int, b: int) -> int:
    \"\"\"Multiply two numbers together.\"\"\"
    return a * b
"""
    with open(file_path, "w") as f:
        f.write(dummy_code)

loader = TextLoader(file_path)
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    language=Language.PYTHON, chunk_size=500, chunk_overlap=50
)

code_chunks = splitter.split_documents(documents)

print(len(code_chunks))
print(code_chunks[0].page_content)
if len(code_chunks) > 1:
    print(code_chunks[1].page_content)
