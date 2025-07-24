# extractor.py
import fitz  # PyMuPDF
from utils import clean_text, get_heading_level

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = doc.metadata.get("title", "Untitled Document")

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    for s in l["spans"]:
                        text = clean_text(s["text"])
                        if not text:
                            continue

                        level = get_heading_level(round(s["size"]))
                        if level:
                            outline.append({
                                "level": level,
                                "text": text,
                                "page": page_num
                            })
    return {"title": title, "outline": outline}
