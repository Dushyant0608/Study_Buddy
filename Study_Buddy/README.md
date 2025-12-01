AI Study Buddy 🤖
This is an AI-powered web application designed to help students understand complex topics, summarize study notes, and generate quizzes on demand. It uses Google's Gemini family of models via their API to provide instant, helpful responses.

✨ Features
Explain a Topic: Enter any topic or question to get a simple, easy-to-understand explanation.

Summarize Notes: Paste in your study notes to receive a concise summary of the key points.

Generate a Quiz: Create a multiple-choice quiz on any subject to test your knowledge.

🚀 How to Run Locally
Clone the repository:

git clone [https://github.com/YOUR_USERNAME/ai-study-buddy.git](https://github.com/YOUR_USERNAME/ai-study-buddy.git)
cd ai-study-buddy

Install the required libraries:

pip install streamlit google-generativeai python-dotenv

Create a .env file in the root directory and add your Google API key:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"

Run the Streamlit app:

streamlit run app.py
