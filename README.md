# 🌾 TN Farmer Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot that helps farmers and citizens retrieve information about **Tamil Nadu Government Farmer Welfare Schemes** using natural language.

The chatbot leverages **Google Gemini**, **LangChain**, **Hugging Face Embeddings**, and **ChromaDB** to provide accurate, context-aware answers based on a curated knowledge base of government schemes.

---

## 📌 Features

* 🤖 AI-powered conversational assistant
* 🔍 Retrieval-Augmented Generation (RAG)
* 📚 Semantic search using vector embeddings
* 💬 Context-aware responses using Google Gemini
* 🌾 Answers questions about Tamil Nadu Farmer Welfare Schemes
* ⚡ Fast retrieval using ChromaDB Vector Database
* 🧠 Modular LangChain architecture

---

## 🛠️ Tech Stack

| Category        | Technology                         |
| --------------- | ---------------------------------- |
| Language        | Python 3.x                         |
| LLM             | Google Gemini                      |
| Framework       | LangChain                          |
| Embeddings      | Hugging Face Sentence Transformers |
| Vector Database | ChromaDB                           |
| Environment     | Python Virtual Environment (venv)  |

---

## 📂 Project Structure

```
tn-farmer-chatbot/
│
├── app.py                 # Application entry point
├── chatbot.py             # Chatbot implementation
├── build_kb.py            # Builds the vector database
├── scraper.py             # Scrapes government scheme information
├── requirements.txt
├── README.md
├── .gitignore
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── data/
│   ├── scheme_1.txt
│   ├── scheme_2.txt
│   └── ...
│
├── utils/
│   ├── chain.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── memory.py
│   ├── prompts.py
│   ├── retriever.py
│   └── vectorstore.py
│
└── chroma_db/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/rrtddypvvs-stack/tn-farmer-chatbot.git

cd tn-farmer-chatbot
```

---

### Create a Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a file named `.env` in the project root.

Example:

```text
GOOGLE_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY
```

> **Note:** Never commit your `.env` file or API keys to GitHub.

---

## 📚 Build the Knowledge Base

Before running the chatbot, generate the vector database.

```bash
python build_kb.py
```

This command:

* Reads all scheme documents
* Creates embeddings
* Stores them in ChromaDB

---

## ▶️ Run the Chatbot

```bash
python app.py
```

Example questions:

* What farmer welfare schemes are available in Tamil Nadu?
* Who is eligible for PM-KISAN?
* What documents are required for crop insurance?
* How can I apply for agricultural subsidies?

---

## 🔄 Workflow

```
Government Scheme Documents
            │
            ▼
      Text Processing
            │
            ▼
 Hugging Face Embeddings
            │
            ▼
        ChromaDB
            │
            ▼
User Question
            │
            ▼
   Similarity Search
            │
            ▼
    Relevant Context
            │
            ▼
     Google Gemini
            │
            ▼
     Final Response
```

---

## 🚀 Future Enhancements

* Voice-based interaction
* Multilingual support (Tamil & English)
* Streamlit web interface
* FastAPI REST API
* Conversation memory
* WhatsApp integration
* Docker deployment
* Cloud deployment (Azure / AWS / GCP)

---

## 📖 Learning Objectives

This project demonstrates practical implementation of:

* Retrieval-Augmented Generation (RAG)
* LangChain
* Google Gemini API
* Vector Databases
* Semantic Search
* Prompt Engineering
* AI Application Development

---

## 👨‍💻 Author

**Vinu S**

Software Engineer | AI & GenAI Enthusiast

GitHub: https://github.com/rrtddypvvs-stack

---

## 📄 License

This project is created for educational and learning purposes.

---

## ⭐ Acknowledgements

* Google Gemini
* LangChain
* Hugging Face
* ChromaDB
* Tamil Nadu Government Farmer Welfare Schemes
