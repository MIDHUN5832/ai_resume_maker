🧠 AI Resume Ranker
A Python-based tool that analyzes and ranks resumes based on how well they match a given job description using Natural Language Processing (NLP).

🚀 Features
📝 Input a job description (as text file)

📂 Analyze multiple resumes (PDF or text files)

📊 Automatically ranks resumes by relevance

⚙️ Uses TF-IDF vectorization + cosine similarity for scoring

📂 Project Structure
ai_resume_ranker/
├── resume_ranker.py       # Python script with ranking logic
├── resumes/               # Folder containing sample resumes
├── job_description.txt    # Job description file
├── results.csv            # Output file with ranked results
├── requirements.txt       # Python dependencies
└── README.md              # This file
⚙️ Tech Stack
🐍 Python 3.8+

🧠 NLP: scikit-learn, nltk

📄 File handling: PyPDF2, os

🧪 How to Run

git clone https://github.com/MIDHUN5832/ai_resume_ranker.git
cd ai_resume_ranker
pip install -r requirements.txt
python resume_ranker.py
💡 How It Works
Loads the job description from job_description.txt

Reads all .pdf or .txt files from the resumes/ folder

Extracts text and cleans it

Uses TF-IDF + cosine similarity to score each resume

Saves a ranked list in results.csv

📜 License
This project is licensed under the MIT License.

🙌 Developed By
Midhun Kunjumon
Built with ❤️ using Python and NLP