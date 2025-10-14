import streamlit as st
import google.generativeai as genai
import os

# --- Configuration ---
try:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
except ImportError:
    # This will run when deployed on Streamlit Community Cloud
    api_key = st.secrets["GOOGLE_API_KEY"]


if not api_key:
    st.error("Google API Key not found. Please set it in your environment or Streamlit secrets.")
else:
    genai.configure(api_key=api_key)


# --- Helper Function to Call Gemini API ---
def get_gemini_response(prompt):
    """Sends a prompt to the Gemini API and returns the response."""
    try:
        # --- Using a confirmed available model from your list ---
        model = genai.GenerativeModel('gemini-2.5-flash') 
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"An API error occurred. This might be due to safety settings or regional restrictions.")
        st.error(f"Details: {e}")
        return None

# --- Streamlit App Interface ---
st.set_page_config(page_title="AI Study Buddy", page_icon="🤖", layout="centered")
st.title("AI Study Buddy 🤖")
st.write("Your personal AI tutor for explanations, summaries, and quizzes.")
st.markdown("---")

# --- Sidebar ---
with st.sidebar:
    st.header("Choose a Tool")
    app_mode = st.radio(
        "Select a tool:",
        ("Explain a Topic", "Summarize My Notes", "Generate a Quiz")
    )
    st.markdown("---")
    st.info("This app is powered by Google Gemini.")


# --- Main App Logic ---
if app_mode == "Explain a Topic":
    st.header("📚 Explain a Topic")
    topic_input = st.text_input("Enter the topic or question:", placeholder="e.g., What is photosynthesis?")
    if st.button("Explain Topic"):
        if topic_input:
            prompt = f"Explain '{topic_input}' simply for a high school student."
            with st.spinner("Generating explanation..."):
                response = get_gemini_response(prompt)
                if response:
                    st.subheader("Explanation:")
                    st.markdown(response)
        else:
            st.warning("Please enter a topic.")

elif app_mode == "Summarize My Notes":
    st.header("📝 Summarize My Notes")
    notes_input = st.text_area("Paste your notes here:", height=200, placeholder="Paste study notes...")
    if st.button("Summarize Notes"):
        if notes_input:
            prompt = f"Summarize these notes into key bullet points:\n\n{notes_input}"
            with st.spinner("Summarizing..."):
                response = get_gemini_response(prompt)
                if response:
                    st.subheader("Summary:")
                    st.markdown(response)
        else:
            st.warning("Please paste your notes.")

elif app_mode == "Generate a Quiz":
    st.header("❓ Generate a Quiz")
    quiz_topic = st.text_input("Enter the quiz topic:", placeholder="e.g., The Solar System")
    if st.button("Generate Quiz"):
        if quiz_topic:
            prompt = f"Create a 3-question multiple-choice quiz on '{quiz_topic}'. Provide an answer key at the end."
            with st.spinner("Generating quiz..."):
                response = get_gemini_response(prompt)
                if response:
                    st.subheader("Quiz Time!")
                    st.markdown(response)
        else:
            st.warning("Please enter a topic.")

