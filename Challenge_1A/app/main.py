# main.py
import os
import json
from extractor import extract_outline

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"

    print("📁 Scanning input folder...")
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            print(f"📄 Processing: {filename}")
            pdf_path = os.path.join(input_dir, filename)
            result = extract_outline(pdf_path)

            output_filename = filename.replace(".pdf", ".json")
            output_path = os.path.join(output_dir, output_filename)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)
            print(f"✅ Output saved: {output_filename}")
    print("✅ All files processed.")

if __name__ == "__main__":
    main()
