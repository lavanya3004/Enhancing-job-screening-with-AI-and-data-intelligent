An intelligent, AI-powered job screening assistant that streamlines the recruitment process by automatically extracting resume content, matching it against job descriptions, and calculating a similarity score.

Features:

Upload resumes in PDF format
Paste job descriptions directly
AI calculates match score using TF-IDF & cosine similarity
Instant result display on the browser
Built with Flask, HTML/CSS/JavaScript, and Python NLP

How It Works:

User uploads a resume (PDF)
Enters or pastes a job description
Backend extracts resume text using PyMuPDF
Compares both using TfidfVectorizer and cosine_similarity
Outputs a match score (%)

Tech Stack:

Component	Technology
Frontend	HTML, CSS, JavaScript
Backend	Python, Flask
NLP Matching	Scikit-learn (TF-IDF + cosine similarity)
Resume Parser	PyMuPDF (fitz)

Installation:
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/ai-job-screening.git
cd ai-job-screening
Install dependencies:

bash
Copy
Edit
pip install flask scikit-learn pymupdf
Run the app:

bash
Copy
Edit
python app.py
Open in browser:

cpp
Copy
Edit
http://127.0.0.1:5000
Project Structure:
bash
Copy
Edit
ai-job-screening/

 app.py             # Flask app with backend + embedded frontend
 README.md          # Project documentation

Future Enhancements:

GPT-based JD summarizer
Skill gap analyzer
Resume scoring with LLM (OpenAI/Gemini)
Dashboard for HR analytics
Database integration for storing matches

Built For:

Hack the Future: A Gen AI Sprint powered by Data
Revolutionizing hiring with automation, intelligence, and speed.

