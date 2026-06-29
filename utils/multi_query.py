from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from utils.llm import get_llm

llm = get_llm()

prompt = ChatPromptTemplate.from_template("""
You are an expert Retrieval-Augmented Generation (RAG) search assistant.

Your task is to generate multiple search queries that maximize retrieval
from a vector database containing Tamil Nadu Farmer Welfare Schemes.

Generate FIVE different search queries.

Rules:

- One query per line.
- No numbering.
- No bullets.
- No explanations.
- Keep each query short.
- Preserve important keywords.
- Use terminology commonly found in government scheme documents.
- Include related scheme names or agricultural terms whenever appropriate.
- Each query should explore a different aspect of the user's question.

Examples

Question:
Explain livelihood of maize farmers

Queries:

Livelihood activities maize farmers
Income generation schemes maize farmers
Farm Production System maize
ISOPOM maize farmers
Certified Seeds of Maize subsidy

----------------------------------------

Question:
Gypsum

Queries:

Distribution of Gypsum
Gypsum subsidy farmers
Oil Seeds gypsum scheme
ISOPOM gypsum
Gypsum transport subsidy

----------------------------------------

Question:
Women farmers

Queries:

Women farmers schemes
Women farmer subsidy
Women farmer grants
Women farmer incentives
Women groups agriculture schemes

----------------------------------------

Question:
{question}
""")

multi_query_chain = (
    prompt
    | llm
    | StrOutputParser()
)


def generate_queries(question: str):

    output = multi_query_chain.invoke(
        {
            "question": question
        }
    )

    queries = []

    for line in output.split("\n"):

        line = line.strip()

        if not line:
            continue

        if line.startswith("-"):
            line = line[1:].strip()

        if line[0:2].isdigit():
            line = line[2:].strip()

        queries.append(line)

    # Remove duplicates while preserving order
    queries = list(dict.fromkeys(queries))

    print("\nGenerated Queries")
    print("=" * 60)

    for q in queries:
        print(q)

    return queries