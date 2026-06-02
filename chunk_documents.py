from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

DATA_FOLDER = "data"

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

all_chunks = []

for file in os.listdir(DATA_FOLDER):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(DATA_FOLDER, file)

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

        chunks = splitter.split_text(text)

        print(f"\n{file}")
        print(f"Chunks Created: {len(chunks)}")

        all_chunks.extend(chunks)

print("\nTotal Chunks:", len(all_chunks))

print("\nSample Chunk:\n")
print(all_chunks[0][:1000])