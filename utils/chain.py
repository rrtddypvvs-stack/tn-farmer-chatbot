from dotenv import load_dotenv

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from utils.prompts import prompt
from utils.llm import get_llm
from utils.query_rewriter import rewrite_query
from utils.retriever import retrieve_documents
from utils.formatter import format_docs

load_dotenv()


def get_chain():

    llm = get_llm()

    chain = (

        {

            "question": lambda question: question,

            "context":

                RunnableLambda(rewrite_query)

                | RunnableLambda(retrieve_documents)

                | RunnableLambda(format_docs)

        }

        | prompt
        | llm
        | StrOutputParser()

    )

    return chain