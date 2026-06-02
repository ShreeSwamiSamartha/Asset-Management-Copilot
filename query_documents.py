from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

question = "What is the investment objective of the fund?"

docs = retriever.invoke(question)

print("\nQUESTION:")
print(question)

print("\nRETRIEVED CHUNKS:\n")

for i, doc in enumerate(docs, start=1):
    print("=" * 80)
    print(f"Chunk {i}")
    print(doc.page_content[:1000])
    print()