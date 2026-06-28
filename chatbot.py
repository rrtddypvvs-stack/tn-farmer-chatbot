from dotenv import load_dotenv

from utils.llm import llm

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load Vector Database
vector_db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

# Create Retriever
retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)

print("Knowledge Base Loaded Successfully!")

while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    # Retrieve relevant chunks
    results = retriever.invoke(question)

    # Combine chunks into one context
    context = "\n\n".join(
        doc.page_content for doc in results
    )

    # Prompt
    prompt = f"""
You are an expert assistant for Tamil Nadu Farmer Welfare Schemes.

Answer ONLY using the information provided in the context.

If the answer is not available, reply:

"I couldn't find this information in the knowledge base."

Context:
{context}

Question:
{question}

Answer:
"""

    # Ask Gemini
    response = llm.invoke(prompt)

    print("\nAnswer")
    print("=" * 60)
    print(response.content)