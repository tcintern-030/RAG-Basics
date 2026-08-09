import os

from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI


load_dotenv()

def load_vector_db():
    embedding_model = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    vector_db = Chroma(
        persist_directory="vector_db",
        embedding_function=embedding_model
    )

    return vector_db

vector_db = load_vector_db()

def create_retriever(vector_db):
    retriever = vector_db.as_retriever(
        search_kwargs={"k": 2}
    )

    return retriever

retriever = create_retriever(vector_db)

query = input("Enter your query: ")

def retrieve_documents(query, retriever):
    documents = retriever.invoke(query)

    return documents

documents = retrieve_documents(query, retriever)

def create_llm():
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    return llm

llm = create_llm()

def generate_response(query, documents, llm):

    context = ""

    for document in documents:
        context += document.page_content + "\n\n"

    prompt = f"""
Answer the question using the following context.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content

generated_response = generate_response(query, documents, llm)

print("\n\nGenerated Response:\n")
print(generated_response)



