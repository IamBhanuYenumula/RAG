import os
import tempfile
from pathlib import Path
from langchain_core.documents import Document
import pypdf

def load_text_file():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(b"Hello, this is a sample text file.\nThis file is used to demonstrate the TextLoader")
        temp_file_path = temp_file.name

    try:
        with open(temp_file_path, encoding="utf-8") as f:
            text = f.read()
        documents = [Document(page_content=text, metadata={"source": temp_file_path})]

        for doc in documents:
            print("Document Content:")
            print(doc)
            print(doc.page_content)

    finally:
        os.remove(temp_file_path)

def pdf_loader(pdf_path: str):
    with open(pdf_path, "rb") as f:
        reader = pypdf.PdfReader(f)
        documents = [
            Document(
                page_content=page.extract_text() or "",
                metadata={"source": pdf_path, "page": i},
            )
            for i, page in enumerate(reader.pages)
        ]

    print(f"Loaded {len(documents)} document(s) from PDF")
    for i, doc in enumerate(documents):
        print(f"Document {i+1} Content Preview: {doc.page_content[:20]}")
        print(f"Metadata: {doc.metadata}")
if __name__ == "__main__":
    # load_text_file()
    pdf_loader("./docs/DW.pdf")