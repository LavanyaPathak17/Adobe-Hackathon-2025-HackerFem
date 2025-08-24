import os, json
from datetime import datetime
from extractor import extract_outline, extract_text_by_page
from analyzer import rank_relevant_sections
from utils import load_persona_job, write_output

def main():
    input_dir = "sample/input"
    output_dir = "sample/output"

    os.makedirs(output_dir, exist_ok=True)

    # Load persona
    persona_file = os.path.join(input_dir, "persona.json")
    persona, job = load_persona_job(persona_file)

    # Process PDFs
    documents = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]
    outlines = []
    all_text_data = []

    for filename in documents:
        print(f"📄 Processing: {filename}")
        pdf_path = os.path.join(input_dir, filename)

        # Step 1A → Extract outline
        outline_result = extract_outline(pdf_path)
        outlines.append({filename: outline_result})
        outline_output = filename.replace(".pdf", "_outline.json")
        with open(os.path.join(output_dir, outline_output), "w", encoding="utf-8") as f:
            json.dump(outline_result, f, indent=2)

        # Step 1B → Extract full text
        text_pages = extract_text_by_page(pdf_path)
        all_text_data.append((filename, text_pages))

    # Step 1B → Relevance analysis
    ranked_sections, subsection_analysis = rank_relevant_sections(all_text_data, persona, job)

    analysis_output = {
        "metadata": {
            "documents": documents,
            "persona": persona,
            "job_to_be_done": job,
            "timestamp": datetime.now().isoformat()
        },
        "extracted_sections": ranked_sections,
        "subsection_analysis": subsection_analysis,
        "outlines": outlines
    }

    write_output(analysis_output, os.path.join(output_dir, "analysis.json"))
    print("✅ All tasks completed. Results in output folder.")

if __name__ == "__main__":
    main()
