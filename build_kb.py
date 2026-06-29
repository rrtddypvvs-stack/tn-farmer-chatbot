from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Load all text files
loader = DirectoryLoader(
    "data",
    glob="*.txt",
    loader_cls=TextLoader
)

documents = loader.load()

from utils.metadata import extract_metadata

for document in documents:

    metadata = extract_metadata(
        document.page_content
    )

    document.metadata.update(metadata)

print("doc0 page content: ", documents[0].page_content) 
print("Metadata: ", documents[0].metadata)  

print(f"Documents Loaded : {len(documents)}")

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=900,
    chunk_overlap=250
)
)

chunks = text_splitter.split_documents(documents)

print(f"Total Chunks Created : {len(chunks)}")

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("\nCreating Vector Database...\n")

# Build Chroma DB
vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)

print("Vector Database Created Successfully!")

print(f"Total Chunks Stored : {vector_db._collection.count()}")