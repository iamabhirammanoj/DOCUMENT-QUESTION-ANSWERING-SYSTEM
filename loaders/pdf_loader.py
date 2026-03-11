import pdfplumber
from langchain_core.documents import Document

def custom_pdf_parser(path):
    sections = []

    with pdfplumber.open(path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if not text:
                continue

            sections.append({
                "title": f"Page {page_num}",
                "text": text,
                "page": page_num
            })

    return sections


def load_pdf_sections(path):
    sections = custom_pdf_parser(path)
    docs = []

    for sec in sections:
        docs.append(
            Document(
                page_content=sec["text"],
                metadata={
                    "source": path,
                    "section": sec["title"],
                    "page": sec["page"]
                }
            )
        )

    return docs
