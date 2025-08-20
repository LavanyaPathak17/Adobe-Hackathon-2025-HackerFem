from utils import keyword_score

def rank_relevant_sections(all_docs, persona, job):
    focus_keywords = persona.lower().split() + job.lower().split()

    extracted = []
    refined = []
    rank = 1

    for docname, pages in all_docs:
        for i, page_text in enumerate(pages):
            score = keyword_score(page_text, focus_keywords)
            if score > 2:
                lines = page_text.split('\n')
                title = lines[0][:80] if lines else f"Page {i+1}"
                extracted.append({
                    "document": docname,
                    "page": i+1,
                    "section_title": title.strip(),
                    "importance_rank": rank
                })
                refined.append({
                    "document": docname,
                    "page": i+1,
                    "refined_text": page_text[:500],
                    "importance_rank": rank
                })
                rank += 1

    return extracted, refined
