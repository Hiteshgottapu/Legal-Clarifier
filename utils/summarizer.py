
import os
from dotenv import load_dotenv
import google.generativeai as genai
from utils.helpers import clean_text


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a valid Gemini model name (update as needed)
model = genai.GenerativeModel("gemini-2.0-flash")

def summarize_text(text, question):
    """Uses Gemini to summarize legal content for the given question."""
    cleaned_text = clean_text(text)
    prompt = f"""
You are a Canadian legal assistant. Based on the text below, provide a short and clear answer to this question:

Q: {question}

Text:
{cleaned_text}

Reply in 2–3 sentences, and if possible, relate to Canadian legal context.
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error summarizing: {e}"
