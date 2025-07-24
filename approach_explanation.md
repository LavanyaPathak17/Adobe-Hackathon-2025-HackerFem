
# Approach Explanation – Round 1B

## Introduction
This solution is designed for Round 1B of the Adobe India Hackathon, *"Connecting the Dots."* The challenge focuses on building a **persona-driven document intelligence system** that can analyze a collection of PDFs and extract the most relevant sections based on a given **persona** and their **job-to-be-done**. The system outputs a structured JSON containing metadata, ranked sections, and refined sub-section analysis.

---

## Methodology

### 1. Persona and Input Handling
The solution accepts:
- **A persona definition (sample_persona.json)** which describes the user's role and job-to-be-done.
- **A collection of PDFs (3-10 documents)** located in the `input/` folder.

The persona’s `job_to_be_done` acts as the query against which all document sections are scored.

### 2. Text Extraction and Chunking
- **PyMuPDF (fitz)** is used to extract text from each page of all input PDFs.
- Extracted text is split into **chunks** of 5 consecutive lines to capture coherent context, while filtering out very short or noisy lines.

### 3. Semantic Scoring with Sentence Transformers
- The **`all-MiniLM-L6-v2`** model (size <100MB) from `sentence-transformers` is used to create embeddings for each chunk and the persona’s `job_to_be_done` query.
- Each chunk is scored using **cosine similarity** (via `pytorch_cos_sim`), and the top 2 chunks per page are selected as **relevant sections**.

### 4. Ranking and Sub-section Analysis
- Extracted sections are ranked based on their similarity scores.
- For each top-ranked chunk, a refined text snippet (up to 60 characters) is stored as the **section title**.
- Sub-sections include the full chunk text and the page number for detailed context.

### 5. Output JSON
The final JSON file (`insights.json`) contains:
- **Metadata**: list of input documents, persona, job-to-be-done, and processing timestamp.
- **Extracted Sections**: document name, page number, section title, and importance rank.
- **Sub-section Analysis**: document name, refined text, and page number.

---

## Performance and Constraints
- Runs fully **offline** with no external API calls.
- **CPU-only execution** with a lightweight model (<100MB).
- Processes 3-5 documents in **<60 seconds** on an AMD64 CPU environment.
- Uses efficient chunking and cosine similarity to ensure quick response times.

---

## Docker Build and Run Instructions

### Build
```bash
docker build --platform linux/amd64 -t persona-doc-intelligence:round1b .
```

### Run
```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none persona-doc-intelligence:round1b
```

The output `insights.json` will be generated inside the `output/` folder.

---

## Example
For a given persona:
```json
{
  "persona": "PhD Researcher in Computational Biology",
  "job_to_be_done": "Prepare a literature review focusing on methodologies, datasets, and performance benchmarks"
}
```

The system extracts and ranks sections from all research papers in `input/` to produce a structured output tailored to this persona's needs.

