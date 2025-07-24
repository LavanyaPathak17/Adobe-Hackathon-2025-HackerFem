# app/extractor.py
import fitz  # PyMuPDF

def extract_text_by_page(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []
    for page in doc:
        text = page.get_text()
        pages.append(text)
    return pages
