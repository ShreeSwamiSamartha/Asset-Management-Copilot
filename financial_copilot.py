from dotenv import load_dotenv

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)

from langchain_community.vectorstores import Chroma

load_dotenv()

# --------------------------------------------------
# Load Embeddings
# --------------------------------------------------

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

# --------------------------------------------------
# Load Vector Database
# --------------------------------------------------

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

# --------------------------------------------------
# Load Gemini LLM
# --------------------------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# --------------------------------------------------
# Ask Question
# --------------------------------------------------

question = input(
    "\nAsk an Asset Management Question:\n> "
)

# --------------------------------------------------
# Retrieve Documents
# --------------------------------------------------

docs = retriever.invoke(question)

context = "\n\n".join(
    [doc.page_content for doc in docs]
)

# --------------------------------------------------
# Prompt
# --------------------------------------------------

prompt = f"""
You are a Senior Asset Management Research Analyst.

Answer ONLY from the provided context.

If the answer is not available in the context,
say:

'I could not find sufficient information in the retrieved documents.'

CONTEXT:
{context}

QUESTION:
{question}

Provide:

1. Direct Answer

2. Supporting Evidence

3. Risk Considerations

4. Analyst Summary
"""

# --------------------------------------------------
# Generate Response
# --------------------------------------------------

response = llm.invoke(prompt)

# --------------------------------------------------
# Output
# --------------------------------------------------

print("\n")
print("=" * 80)
print("ASSET MANAGEMENT RESEARCH COPILOT")
print("=" * 80)

print("\nQUESTION:")
print(question)

print("\nANSWER:\n")
print(response.content)

print("\n")
print("=" * 80)
print("SOURCE DOCUMENTS")
print("=" * 80)

for i, doc in enumerate(docs, start=1):

    print(f"\nSource {i}")

    if "source" in doc.metadata:
        print(f"Document: {doc.metadata['source']}")

    print("\nExcerpt:")
    print(doc.page_content[:500])