import os

from dotenv import load_dotenv

load_dotenv()


def get_llm():

    provider = os.getenv("LLM_PROVIDER", "openai").strip().lower()
    temperature = float(os.getenv("LLM_TEMPERATURE", "0"))

    if provider == "openai":

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set.")

        from langchain_openai import ChatOpenAI

        return ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-5"),
            temperature=temperature,
            api_key=api_key
        )

    elif provider == "google":

        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError("GOOGLE_API_KEY is not set.")

        from langchain_google_genai import ChatGoogleGenerativeAI

        return ChatGoogleGenerativeAI(
            model=os.getenv("GOOGLE_MODEL", "gemini-2.5-flash"),
            temperature=temperature,
            google_api_key=api_key
        )

    raise ValueError(
        f"Unsupported LLM_PROVIDER: {provider}"
    )