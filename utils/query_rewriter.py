from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from utils.llm import get_llm

llm = get_llm()

rewrite_prompt = ChatPromptTemplate.from_template("""
You are an expert search query optimizer for a RAG system.

Rewrite the user's question into a search query that maximizes retrieval quality.

Rules:

- Preserve the user's intent.
- Use terminology likely to appear in government scheme documents.
- Expand vague phrases into domain-specific keywords.
- Keep important nouns.
- Do NOT answer the question.
- Return ONLY the rewritten search query.

Examples:

Question:
Explain the livelihood of maize farmers

Search Query:
Livelihood activities for maize farmers income generation schemes maize

Question:
Women welfare schemes

Search Query:
Women farmers welfare schemes subsidies grants incentives

Question:
Gypsum

Search Query:
Distribution of Gypsum subsidy farmers

Question:
Organic farming

Search Query:
Organic farming subsidy scheme farmers

User Question:
{question}
""")

rewrite_chain = (
    rewrite_prompt
    | llm
    | StrOutputParser()
)


def rewrite_query(question: str) -> str:

    rewritten = rewrite_chain.invoke(
        {
            "question": question
        }
    ).strip()

    print("\nRewritten Query")
    print("=" * 60)
    print(rewritten)

    return rewritten