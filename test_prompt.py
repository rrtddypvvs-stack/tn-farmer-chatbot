from utils.formatter import format_docs
from utils.prompts import prompt
from utils.retriever import get_retriever

retriever = get_retriever()

question = "Explain livelihood activities"

docs = retriever.invoke(question)

formatted_context = format_docs(docs)

final_prompt = prompt.invoke(
    {
        "context": formatted_context,
        "question": question
    }
)

print(final_prompt)