from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from config.settings import (
    TOP_K,
    FETCH_K,
    LAMBDA_MULT
)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

def get_retriever():

    return vector_db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": TOP_K,
            "fetch_k": FETCH_K,
            "lambda_mult": LAMBDA_MULT
        }
    )

def get_documents_with_scores(question):

    results = vector_db.similarity_search_with_score(
        question,
        k=5
    )

    return results