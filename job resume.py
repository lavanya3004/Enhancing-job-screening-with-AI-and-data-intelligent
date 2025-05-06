from flask import Flask, render_template_string, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import fitz  # PyMuPDF

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>AI Job Match</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background: #f4f7fa;
      margin: 0;
      padding: 0;
    }
    .container {
      max-width: 600px;
      margin: 40px auto;
      background: white;
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    h1 {
      text-align: center;
      color: #2c3e50;
    }
    form {
      display: flex;
      flex-direction: column;
      gap: 15px;
      margin-top: 20px;
    }
    input[type="file"],
    textarea {
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 6px;
    }
    button {
      background-color: #0077ff;
      color: white;
      padding: 12px;
      border: none;
      border-radius: 6px;
      font-size: 16px;
      cursor: pointer;
    }
    button:hover {
      background-color: #005fcc;
    }
    #result {
      margin-top: 30px;
      padding: 20px;
      background: #ecf9ec;
      border: 1px solid #b2d8b2;
      border-radius: 8px;
      text-align: center;
    }
    .hidden {
      display: none;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🔍 AI Job Screening Assistant</h1>
    <form id="uploadForm" enctype="multipart/form-data">
      <label>Upload Resume (PDF):</label>
      <input type="file" name="resume" required />

      <label>Paste Job Description:</label>
      <textarea name="jobDesc" rows="6" required></textarea>

      <button type="submit">Get Match Score</button>
    </form>

    <div id="result" class="hidden">
      <h2>✅ Match Score: <span id="scoreDisplay"></span>%</h2>
    </div>
  </div>

  <script>
    document.getElementById('uploadForm').addEventListener('submit', async function(e) {
      e.preventDefault();
      const formData = new FormData(this);
      const response = await fetch('/match', {
        method: 'POST',
        body: formData
      });
      const data = await response.json();
      document.getElementById('scoreDisplay').textContent = data.score;
      document.getElementById('result').classList.remove('hidden');
    });
  </script>
</body>
</html>
"""

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

def calculate_similarity(resume_text, job_desc):
    texts = [resume_text, job_desc]
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(texts)
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(float(similarity[0][0]) * 100, 2)

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/match', methods=['POST'])
def match():
    resume = request.files['resume']
    job_desc = request.form['jobDesc']
    resume_text = extract_text_from_pdf(resume)
    if not resume_text:
        return jsonify({'score': 0})
    score = calculate_similarity(resume_text, job_desc)
    return jsonify({'score': score})

if __name__ == '__main__':
    app.run(debug=True)
