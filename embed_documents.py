import os
from dotenv import load_dotenv
from pypdf import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

from langchain_community.vectorstores import Chroma

load_dotenv()

DATA_FOLDER = "data"

all_docs = []

splitter = RecursiveCharacterTextSplitter(
    chunk_size=5000,
    chunk_overlap=500
)

print("Reading PDFs...")

for file in os.listdir(DATA_FOLDER)[0:1]:

    if file.endswith(".pdf"):

        pdf_path = os.path.join(DATA_FOLDER, file)

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

        chunks = splitter.split_text(text)

        # TEMPORARY LIMIT FOR TESTING
        chunks = chunks[:1]

        print(f"{file} -> {len(chunks)} chunks")

        for chunk in chunks:
            all_docs.append(
                Document(
                    page_content=chunk,
                    metadata={"source": file}
                )
            )

print(f"\nTotal Documents: {len(all_docs)}")

print("\nCreating Gemini Embeddings...")

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)
print(f"Embedding {len(all_docs)} chunks...")
vectorstore = Chroma.from_documents(
    documents=all_docs,
    embedding=embeddings,
    persist_directory="chroma_db"
)
print(f"Embedding {len(all_docs)} chunks...")
print("\nSUCCESS")
print("Vector database created.")