from dotenv import load_dotenv

from utils.chain import get_chain
from utils.retriever import get_documents_with_scores

load_dotenv()

chain = get_chain()


def display_similarity_scores(results):

    print("\nSimilarity Scores")
    print("=" * 80)

    for i, (doc, score) in enumerate(results, start=1):

        print(f"\nResult {i}")
        print(f"Score : {score:.4f}")
        print(f"Scheme: {doc.metadata.get('scheme_name', 'N/A')}")


print("Knowledge Base Loaded Successfully!")

chat_history = []

while True:

    question = input("\nAsk a question (type 'exit' to quit): ").strip()

    if question.lower() == "exit":
        break

    results = get_documents_with_scores(question)

    display_similarity_scores(results)

    history = "\n".join(
        f"User: {q}\nAssistant: {a}"
        for q, a in chat_history
    )

    full_question = f"""
Conversation History:
{history}

Current Question:
{question}
"""

    try:

        answer = chain.invoke(full_question)

        print("\nAnswer")
        print("=" * 60)
        print(answer)

        chat_history.append((question, answer))

    except Exception as e:

        print("\nError")
        print("=" * 60)
        print(f"Unable to generate an answer: {e}")