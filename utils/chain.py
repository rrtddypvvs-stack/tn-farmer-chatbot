from dotenv import load_dotenv

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

from utils.formatter import format_docs
from utils.llm import get_llm
from utils.prompts import prompt
from utils.retriever import get_retriever

load_dotenv()


def get_chain():

    retriever = get_retriever()

    llm = get_llm()

    chain = (
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain