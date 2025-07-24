# app/main.py
import os, json
from datetime import datetime
from extractor import extract_text_by_page
from analyzer import rank_relevant_sections
from utils import load_persona_job, write_output

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"

    persona_file = os.path.join(input_dir, "persona.json")
    persona, job = load_persona_job(persona_file)

    documents = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]
    full_data = []

    for doc in documents:
        print(f"📄 Reading {doc}")
        doc_path = os.path.join(input_dir, doc)
        text_pages = extract_text_by_page(doc_path)
        full_data.append((doc, text_pages))

    ranked_sections, subsection_analysis = rank_relevant_sections(full_data, persona, job)

    output = {
        "metadata": {
            "documents": documents,
            "persona": persona,
            "job_to_be_done": job,
            "timestamp": datetime.now().isoformat()
        },
        "extracted_sections": ranked_sections,
        "subsection_analysis": subsection_analysis
    }

    write_output(output, os.path.join(output_dir, "output.json"))
    print("✅ Done. Output saved.")

if __name__ == "__main__":
    main()
