from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from utils.multi_query import generate_queries


def get_vector_db():

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding_model
    )


def get_retriever():

    vector_db = get_vector_db()

    return vector_db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 8,
            "fetch_k": 30,
            "lambda_mult": 0.3,
        },
    )


def retrieve_documents(question):

    vector_db = get_vector_db()

    queries = generate_queries(question)

    unique_docs = {}

    for query in queries:

        docs = vector_db.similarity_search(
            query,
            k=4,
        )

        for doc in docs:

            unique_docs[
                doc.page_content
            ] = doc

    return list(unique_docs.values())


def get_documents_with_scores(question):

    vector_db = get_vector_db()

    return vector_db.similarity_search_with_relevance_scores(
        question,
        k=5,
    )