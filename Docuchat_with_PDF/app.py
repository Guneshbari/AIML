import os
import sys
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chat_models import init_chat_model

# Load .env file relative to script location
dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(dotenv_path)

# Fallback to GEMINI_API_KEY if GOOGLE_API_KEY is not defined
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
if not GOOGLE_API_KEY:
    print("Error: GOOGLE_API_KEY or GEMINI_API_KEY environment variable not set.")
    print("Please set it in your environment or a .env file.")
    sys.exit(1)

# Resolve path relative to the script's directory for portability
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "Attention_Is_All_You_Need.pdf")

if not os.path.exists(file_path):
    print(f"Error: PDF file not found at: {file_path}")
    print("Please place 'Attention_Is_All_You_Need.pdf' in the same directory as this script.")
    sys.exit(1)

loader = PyPDFLoader(file_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    add_start_index=True,
)

all_splits = text_splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

persist_dir = os.path.join(current_dir, "chroma_langchain_db")
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory=persist_dir,
)
document_ids = vector_store.add_documents(documents=all_splits)
sample = vector_store.get(limit=1, include=["embeddings", "documents"])

model = init_chat_model(
    "google_genai:gemini-2.5-flash",
    api_key=GOOGLE_API_KEY,
)


# Fixed k parameter in function signature to avoid TypeError/NameError
def retrieve_context(query, k=2):
    retrieved_docs = vector_store.similarity_search(query, k=k)
    docs_content = ""
    for doc in retrieved_docs:
        docs_content += f"Source: {doc.metadata}\n"
        docs_content += f"Content: {doc.page_content}\n\n"

    return docs_content, retrieved_docs


def ask_about_pdf(user_query):
    context, source_docs = retrieve_context(user_query, k=2)
    system_message = f"""You are a helpful chatbot.
                     Use only the following pieces of context to answer the 
                     question. Don't makeup any new information: {context} """

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_query},
    ]
    response = model.invoke(messages)
    return {
        "answer": response.content,
        "source_documents": source_docs,
        "context_used": context,
    }


result = ask_about_pdf(
    "What improvements have been made to attention mechanisms since 2017?"
)
print(result)
print(result["answer"])
