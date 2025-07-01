import streamlit as st
from utils.summarizer import summarize_text
import time

st.set_page_config(
    page_title="Legal Clarifier (Canada)", 
    page_icon="⚖️", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Enhanced Custom CSS with better spacing, animations, and visual polish
st.markdown("""
<style>
:root {
    --primary: #2874A6;
    --secondary: #1abc9c;
    --dark: #1a2636;
    --light: #f8fafc;
    --accent: #3498db;
    --border: #e3eaf2;
    --card-shadow: 0 4px 24px 0 rgba(214, 234, 248, 0.6);
}

body {
    background: linear-gradient(135deg, #f8fafc 0%, #f0f7fc 100%);
    font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
}

.block-container {
    max-width: 750px !important;
    margin: 2em auto;
    background: #fff;
    border-radius: 16px;
    box-shadow: var(--card-shadow);
    padding: 2.5em 2.5em 1.5em 2.5em;
    border: 1px solid var(--border);
    animation: fadeIn 0.5s ease-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

h1, h2, h3, h4 {
    color: var(--dark);
    font-weight: 600;
}

.stTextInput > div > div > input {
    background: #f8fafc;
    border-radius: 10px;
    border: 1.5px solid #d6e3ec;
    font-size: 1.1em;
    padding: 0.75em 1em;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
}

.stTextInput > div > div > input:focus {
    border: 1.5px solid var(--primary);
    background: #fff;
    box-shadow: 0 0 0 3px rgba(40, 116, 166, 0.1);
}

.stSelectbox > div > div {
    background: #f8fafc;
    border-radius: 10px;
    border: 1.5px solid #d6e3ec;
    font-size: 1.1em;
    padding: 0.5em 1em;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.stSelectbox > div > div:focus-within {
    border: 1.5px solid var(--primary);
    box-shadow: 0 0 0 3px rgba(40, 116, 166, 0.1);
}

/* Dropdown menu styling for selectbox */
.stSelectbox > div > div > div {
    background: #fff !important;
    border: 1px solid #d6e3ec !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
    z-index: 1000 !important;
}
.stSelectbox > div > div > div > div {
    padding: 0.5em 1em !important;
    color: #2d3748 !important;
}
.stSelectbox > div > div > div > div:hover {
    background: #f0f7ff !important;
}

.stButton > button {
    background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%);
    color: #fff;
    border-radius: 10px;
    font-weight: 600;
    font-size: 1.1em;
    padding: 0.75em 2em;
    margin: 1.5em 0 0.5em 0;
    border: none;
    box-shadow: 0 4px 12px rgba(26, 188, 156, 0.15);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    width: 100%;
}

.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 16px rgba(26, 188, 156, 0.2);
    background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 120%);
}

.stButton > button:active {
    transform: translateY(0);
}

.stSpinner > div > div {
    border-color: var(--primary) transparent transparent transparent !important;
}

.stMarkdown > div {
    font-size: 1.12em;
    line-height: 1.8;
    color: #2d3748;
}

/* Custom card styles */
.card {
    border-radius: 12px;
    padding: 1.5em;
    margin: 1.5em 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    border: 1px solid rgba(0,0,0,0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
}

.user-card {
    background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
    border-left: 4px solid var(--primary);
}

.answer-card {
    background: linear-gradient(135deg, #f0fff4 0%, #e6ffed 100%);
    border-left: 4px solid var(--secondary);
}

.detail-card {
    background: linear-gradient(135deg, #fffaf0 0%, #fff5e6 100%);
    border-left: 4px solid #f39c12;
}

.source-card {
    background: linear-gradient(135deg, #f8f0ff 0%, #f0e6ff 100%);
    border-left: 4px solid #9b59b6;
}

/* Tooltip style */
.tooltip {
    position: relative;
    display: inline-block;
    border-bottom: 1px dotted #666;
    cursor: help;
}

.tooltip .tooltiptext {
    visibility: hidden;
    width: 200px;
    background-color: #555;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    padding: 8px;
    position: absolute;
    z-index: 1;
    bottom: 125%;
    left: 50%;
    margin-left: -100px;
    opacity: 0;
    transition: opacity 0.3s;
    font-size: 0.9em;
    line-height: 1.4;
}

.tooltip:hover .tooltiptext {
    visibility: visible;
    opacity: 1;
}

/* Custom CSS for checkboxes (add this to your CSS block if not already present) */
.stCheckbox > label {
    font-size: 1.1em;
    padding: 0.5em 1em;
    border-radius: 8px;
    transition: all 0.2s;
    margin-bottom: 0.5em;
    display: block;
}
/* Hover effect */
.stCheckbox > label:hover {
    background-color: #f0f7ff;
}
/* Selected checkbox style */
.stCheckbox > label[data-baseweb="checkbox"]:has(input:checked) {
    background-color: #e6f2ff;
    font-weight: 500;
}
/* Hide the original checkbox */
.stCheckbox > label > div:first-child {
    opacity: 0;
    width: 0;
    margin-right: 0;
}
/* Custom checkbox appearance */
.stCheckbox > label:before {
    content: "";
    display: inline-block;
    width: 18px;
    height: 18px;
    border: 2px solid #2874A6;
    border-radius: 4px;
    margin-right: 10px;
    vertical-align: middle;
    position: relative;
    top: -1px;
}
/* Checked state */
.stCheckbox > label:has(input:checked):before {
    background-color: #2874A6;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white'%3E%3Cpath d='M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: center;
    background-size: 14px;
}
/* Section styling */
.section {
    margin-bottom: 2em;
    padding: 1.5em;
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .block-container {
        padding: 1.5em;
        border-radius: 0;
    }
}
</style>
""", unsafe_allow_html=True)

# Header with improved layout
col1, col2 = st.columns([0.85, 0.15])
with col1:
    st.markdown("""
    <h1 style='margin-bottom: 0.2em;'>Legal Clarifier <span style="font-size: 0.7em; color: #666;">Canada</span></h1>
    <p style='color: #666; margin-top: 0;'>Get clear, concise answers to your Canadian legal questions</p>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("<div style='text-align: right; font-size: 3em;'>⚖️</div>", unsafe_allow_html=True)

# Information box with tooltips
st.markdown("""
<div class='card' style='background-color: #f8fafc;'>
    <div style='display: flex; align-items: center; margin-bottom: 0.5em;'>
        <span style='font-size: 1.2em; margin-right: 0.5em;'>💡</span>
        <b>How to use this tool</b>
    </div>
    <p style='margin-bottom: 0.5em;'>Ask any question about Canadian law and get an AI-powered summary with references to relevant statutes, case law, and legal principles.</p>
    <div style='font-size: 0.9em; color: #666;'>
        <span class='tooltip'>Example questions
            <span class='tooltiptext'>"What are the requirements for a valid will in Ontario?"<br>"Explain tenant rights in BC for rent increases"<br>"What constitutes wrongful dismissal in Canada?"</span>
        </span> | 
        <span class='tooltip'>Limitations
            <span class='tooltiptext'>Not a substitute for legal advice. Accuracy not guaranteed. Focused on Canadian law only.</span>
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# Form section with better visual hierarchy
with st.form("legal_query_form"):
    st.markdown("<h3 style='margin-bottom: 0.5em;'>Your Legal Question</h3>", unsafe_allow_html=True)
    query = st.text_area(
        "Enter your question about Canadian law", 
        placeholder="e.g. What are the grounds for contesting a will in Alberta?",
        height=120,
        key="query_input"
    )

    # Jurisdiction multi-select checkboxes
    st.markdown("""
**Jurisdiction**
""", unsafe_allow_html=True)
    jurisdictions = [
        "Federal", "Alberta", "British Columbia", "Manitoba", "New Brunswick", 
        "Newfoundland and Labrador", "Nova Scotia", "Ontario", 
        "Prince Edward Island", "Quebec", "Saskatchewan", 
        "Northwest Territories", "Nunavut", "Yukon"
    ]
    selected_jurisdictions = []
    cols = st.columns(3)
    for i, jurisdiction in enumerate(jurisdictions):
        with cols[i % 3]:
            if st.checkbox(jurisdiction, key=f"jur_{jurisdiction}"):
                selected_jurisdictions.append(jurisdiction)

    # Law Type multi-select checkboxes
    st.markdown("""
**Law Type**
""", unsafe_allow_html=True)
    law_types = [
        "Statutes/Acts", "Regulations", "Case Law", 
        "Charter Rights", "Contract Law", "Property Law",
        "Family Law", "Criminal Law", "Other"
    ]
    selected_law_types = []
    cols2 = st.columns(3)
    for i, law_type in enumerate(law_types):
        with cols2[i % 3]:
            if st.checkbox(law_type, key=f"law_{law_type}"):
                selected_law_types.append(law_type)

    submitted = st.form_submit_button("Get Legal Answer", type="primary")

if submitted and query:
    if not selected_jurisdictions or not selected_law_types:
        st.warning("Please select at least one jurisdiction and one law type")
    else:
        # Use the first selected value for single-jurisdiction logic, or join for multi
        selected_jurisdiction = ", ".join(selected_jurisdictions)
        selected_law_type = ", ".join(selected_law_types)

        # Prepare context for Gemini
        context = (
            f"Provide a comprehensive answer about Canadian law only. "
            f"Jurisdiction: {selected_jurisdiction}. "
            f"Law type: {selected_law_type}. "
            f"Reference relevant Canadian statutes, regulations, or case law when possible. "
            f"Use clear, plain language but maintain legal accuracy. "
            f"Structure the answer with headings if helpful. "
        )
        
        # User's question card
        with st.container():
            st.markdown(f"""
            <div class='card user-card'>
                <div style='display: flex; align-items: center; margin-bottom: 0.8em;'>
                    <span style='font-size: 1.5em; margin-right: 0.5em;'>👤</span>
                    <h3 style='margin: 0;'>Your Question</h3>
                </div>
                <div style='font-size: 1.15em; line-height: 1.7;'>
                    {query}
                </div>
                <div style='margin-top: 1em; font-size: 0.9em; color: #666;'>
                    <span>Jurisdiction: {selected_jurisdiction}</span> • 
                    <span>Law Type: {selected_law_type}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Answer section with loading animation
        with st.spinner("Researching Canadian law sources..."):
            time.sleep(1)  # Simulate research time
            
            # Main answer card
            with st.container():
                st.markdown("""
                <div class='card answer-card'>
                    <div style='display: flex; align-items: center; margin-bottom: 0.8em;'>
                        <span style='font-size: 1.5em; margin-right: 0.5em;'>⚖️</span>
                        <h3 style='margin: 0;'>Legal Summary</h3>
                    </div>
                """, unsafe_allow_html=True)
                
                # Stream the answer
                placeholder = st.empty()
                summary = summarize_text(context, query)
                words = summary.split()
                displayed = ""
                for word in words:
                    displayed += word + " "
                    placeholder.markdown(f"""
                    <div style='font-size: 1.12em; line-height: 1.8;'>
                        {displayed}
                    </div>
                    """, unsafe_allow_html=True)
                    time.sleep(0.03)
                
                st.markdown("</div>", unsafe_allow_html=True)
            
            # Detailed explanation card
            with st.container():
                st.markdown("""
                <div class='card detail-card'>
                    <div style='display: flex; align-items: center; margin-bottom: 0.8em;'>
                        <span style='font-size: 1.5em; margin-right: 0.5em;'>📚</span>
                        <h3 style='margin: 0;'>Detailed Explanation</h3>
                    </div>
                """, unsafe_allow_html=True)
                
                detail_context = context + " Provide a detailed, step-by-step legal explanation with references to specific statutes, cases, or legal principles where applicable."
                detail = summarize_text(detail_context, query)
                st.markdown(detail)
                
                st.markdown("</div>", unsafe_allow_html=True)
            
            # Legal sources card (simulated - would be real in production)
            with st.container():
                st.markdown("""
                <div class='card source-card'>
                    <div style='display: flex; align-items: center; margin-bottom: 0.8em;'>
                        <span style='font-size: 1.5em; margin-right: 0.5em;'>🔍</span>
                        <h3 style='margin: 0;'>Potential Legal Sources</h3>
                    </div>
                    <ul style='margin-top: 0; padding-left: 1.2em;'>
                        <li><i>Canadian Charter of Rights and Freedoms</i> (if applicable)</li>
                        <li><i>{selected_jurisdiction} Statutes</i> relevant to the question</li>
                        <li>Recent case law from {selected_jurisdiction} courts</li>
                        <li>Canadian legal textbooks and commentaries</li>
                    </ul>
                    <div style='margin-top: 1em; font-size: 0.9em; color: #666;'>
                        Note: These are potential sources - consult a lawyer for authoritative references.
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Disclaimer
        st.markdown("""
        <div style='margin-top: 2em; padding: 1em; background-color: #fff8f8; border-radius: 8px; border-left: 4px solid #e74c3c;'>
            <div style='display: flex; align-items: center; margin-bottom: 0.5em;'>
                <span style='font-size: 1.2em; margin-right: 0.5em;'>⚠️</span>
                <b>Important Disclaimer</b>
            </div>
            <p style='margin: 0; font-size: 0.95em;'>
                This tool provides general legal information only, not professional advice. Laws change frequently and vary by jurisdiction. For legal decisions, always consult a qualified lawyer licensed in your province or territory.
            </p>
        </div>
        """, unsafe_allow_html=True)