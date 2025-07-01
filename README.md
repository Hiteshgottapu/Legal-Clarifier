# Legal Clarifier

Legal Clarifier is a modern Streamlit app that answers Canadian legal questions using Gemini AI, with a clean, card-based UI and real-time answer streaming.

## Features
- ⚖️ Ask any question about Canadian law and get an AI-powered summary and detailed explanation
- � Select jurisdiction and law type from dropdowns (all provinces/territories and major law categories)
- 💡 Real-time, word-by-word streaming of Gemini's answer for a conversational feel
- �️ Modern, responsive UI with custom CSS, cards, tooltips, and visual hierarchy
- 🔗 References to relevant statutes, case law, and legal principles (where possible)
- 🚫 Disclaimer and clear limitations (not legal advice)

## Setup
1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Add your Gemini API key to a `.env` file:
   - `GEMINI_API_KEY` for Gemini LLM summarization
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Project Structure
```
legal_clarifier/
├── app.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml
├── utils/
│   ├── __init__.py
│   ├── canlii_scraper.py
│   ├── summarizer.py
│   └── helpers.py
├── assets/
    └── logo.png
```

## Environment Variables
Create a `.env` file in the root with:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

## Usage
1. Enter your legal question in the text area.
2. Select the jurisdiction and law type from the dropdowns.
3. Click "Get Legal Answer" to receive a summary and detailed explanation, streamed in real time.

## Disclaimer
This tool provides general legal information only, not professional advice. Laws change frequently and vary by jurisdiction. For legal decisions, always consult a qualified lawyer licensed in your province or territory.
