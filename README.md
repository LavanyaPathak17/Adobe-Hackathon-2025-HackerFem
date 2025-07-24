# Adobe-Hackathon-2025-HackerFem

# Round 1A - Document Outline Extractor

This project is a solution for Round 1A of the Adobe India Hackathon, "Connecting the Dots." It's designed to parse a PDF file and automatically extract a structured outline, including the document's title and hierarchical headings (H1, H2, H3).

---

## Our Approach

The solution processes PDFs by analyzing their structural properties, primarily focusing on **font characteristics**.

1.  **Text Extraction:** The `PyMuPDF` library is used to extract all text blocks from each page while preserving crucial metadata like font size.
2.  **Noise Reduction:** A series of cleaning steps are applied to remove irrelevant text fragments and whitespace, ensuring that only meaningful content is analyzed.
3.  **Heading Identification:** The core of the logic assumes that **headings use larger font sizes** than body text. The program identifies all unique font sizes in the document and maps the three largest sizes to H1, H2, and H3 respectively.
4.  **Bonus: Language Detection:** To handle the multilingual requirement, the `langdetect` library is used to determine the primary language of the document, which is included in the final output.

---

## Libraries Used

This solution is lightweight and relies on two key Python libraries:

* **PyMuPDF**: Used for robust PDF parsing and text extraction.
* **langdetect**: Used for the multilingual heading detection bonus criterion.

---

## How to Build and Run

The solution is containerized using Docker and is designed to run offline on a CPU.

**1. Build the Docker Image**
• From the root directory of the project, run the following command to build the image:

docker build --platform linux/amd64 -t mysolutionname:somerandomidentifier .

**2. Prepare Input**
•	Place your PDFs inside a folder named 'input' in the root directory.

**3. Run the Container**
•	The container will process all .pdf files in the input folder and produce corresponding .json files in the output folder:

docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none mysolutionname:somerandomidentifier

---

**Example Output**
• For a sample PDF sample.pdf, the output JSON in output/sample.json looks like:

{
  "title": "Sample Document",
  "language": "en",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1, "language": "en" },
    { "level": "H2", "text": "Overview", "page": 2, "language": "en" }
  ]
}

**Notes**
•	Runs in <10 seconds for a 50-page PDF.
•	No internet access required.



