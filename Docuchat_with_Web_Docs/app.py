import os
import sys
from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chat_models import init_chat_model

# Load .env file relative to script location
dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(dotenv_path)

# Retrieve and check API key
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY or GOOGLE_API_KEY environment variable not set.")
    print("Please set it in your environment or a .env file.")
    sys.exit(1)

urls = [
    "https://docs.langchain.com/oss/python/integrations/document_loaders",
    "https://docs.langchain.com/oss/python/integrations/vectorstores",
    "https://docs.langchain.com/oss/python/integrations/text_embedding",
]

loader = WebBaseLoader(urls)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)

all_splits = text_splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

current_dir = os.path.dirname(os.path.abspath(__file__))
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
    api_key=api_key,
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
    system_message = f"""You are a helpful AI assistant specialized in explaining LangChain documentation.
                    Use the following context extracted from the LangChain documentation webpages to answer the user's question:
                    {context}
                    INSTRUCTIONS:
                    1. Answer based ONLY on the provided context from the LangChain documentation.
                    2. Do NOT use outside knowledge beyond the documentation.
                    3. If the answer is not present in the context, say:
                        \"This information is not available in the provided LangChain documentation context.\"
                    4. Use exact terminology, class names, method names, and concepts as described.
                    5. Keep explanations clear and technically accurate.
                    6. Mention specific modules, classes, or configuration options when relevant.
                    7. If code snippets are present, explain without modifying logic."""

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


result = ask_about_pdf("How to use the HuggingFaceEmbeddings?")
print(result["answer"])

result = ask_about_pdf(
    "Explain the use this value : sentence-transformers/all-mpnet-base-v2"
)
print(result["answer"])

result = ask_about_pdf("How to use Open AI Embeddings")
print(result["answer"])

result = ask_about_pdf("Explain about this: OpenAIEmbeddings")
print(result["answer"])
