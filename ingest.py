import os
from pypdf import PdfReader

DATA_FOLDER = "data"

for file in os.listdir(DATA_FOLDER):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(DATA_FOLDER, file)

        print("\n" + "=" * 80)
        print(f"Processing: {file}")

        reader = PdfReader(pdf_path)

        print(f"Pages: {len(reader.pages)}")

        text = ""

        for page in reader.pages:
            try:
                text += page.extract_text()
            except Exception as e:
                print(f"Page extraction error: {e}")

        print(f"Characters extracted: {len(text)}")

        print("\nFirst 1000 Characters:\n")
        print(text[:1000])

        print("\n" + "=" * 80)