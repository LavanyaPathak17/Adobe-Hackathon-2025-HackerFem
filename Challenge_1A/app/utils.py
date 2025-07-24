# utils.py

def clean_text(text):
    """
    Cleans and normalizes text extracted from PDF spans.
    Removes extra spaces, control characters, etc.
    """
    return " ".join(text.strip().split())


def get_heading_level(font_size):
    """
    Maps font sizes to heading levels (H1, H2, H3) heuristically.
    Adjust thresholds as needed for your PDFs.
    """
    if font_size >= 18:
        return "H1"
    elif font_size >= 14:
        return "H2"
    elif font_size >= 11:
        return "H3"
    else:
        return None
