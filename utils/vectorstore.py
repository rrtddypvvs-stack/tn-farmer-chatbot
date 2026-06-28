from langchain_chroma import Chroma

from config.settings import CHROMA_DB_DIR

from utils.embeddings import get_embedding_model


def load_vectorstore():

    return Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=get_embedding_model()
    )