# app/utils.py
import json

def load_persona_job(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    persona = data.get("persona", {}).get("role", "")
    job = data.get("job", "")
    return persona, job

def write_output(obj, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)

def keyword_score(text, keywords):
    count = 0
    text = text.lower()
    for word in keywords:
        if word.lower() in text:
            count += 1
    return count
