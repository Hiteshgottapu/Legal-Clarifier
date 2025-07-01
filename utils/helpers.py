import re

def clean_text(text):
    """
    Clean extracted legal text by removing excessive whitespace and formatting issues.
    """
    if not text:
        return ""
    
    # Remove multiple line breaks
    text = re.sub(r"\n{2,}", "\n\n", text)
    
    # Replace multiple spaces with one
    text = re.sub(r"[ \t]+", " ", text)
    
    # Strip leading/trailing whitespace
    return text.strip()


def is_valid_url(url):
    """
    Basic check to ensure URL is a proper CanLII link.
    """
    return isinstance(url, str) and url.startswith("https://www.canlii.org")


def fallback_summary(question):
    """
    Default response if no content or LLM fails.
    """
    return f"Sorry, I couldn't find a clear answer to your question: '{question}'. Please try rephrasing or narrowing it down."
