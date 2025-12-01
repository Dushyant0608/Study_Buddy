📚 StudyBuddy — AI-Powered Study Assistant

Live Demo: https://studybuddy-4hruqvazf96whpxcrx69ne.streamlit.app/

StudyBuddy is a lightweight Streamlit application that helps students summarize notes, generate quizzes, and interact with their study material using AI.

🔍 Features

Text & PDF Summarization

Ask Questions About Your Notes

Auto-generated Quizzes (MCQ / Short Answer)

Flashcard Generator

Simple & responsive UI

🛠️ Installation
1. Clone the repository
git clone https://github.com/your-username/StudyBuddy.git
cd StudyBuddy

2. Install dependencies
pip install -r requirements.txt

3. Add your API key

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here

4. Run the app
streamlit run app.py

🧠 How It Works

User uploads text or PDF

The app processes and chunks the content

An AI model generates summaries, answers, or quiz questions

Results are displayed inside the Streamlit UI

📦 Tech Stack

Python / Streamlit

OpenAI (or any LLM provider)

PyPDF / pdfplumber for PDF reading

dotenv for environment variables

📈 Roadmap

Add user accounts

Save quizzes & summaries

Export flashcards (Anki format)

Dark mode

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.
