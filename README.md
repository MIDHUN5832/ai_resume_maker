# 🧠 AI Resume Ranker

An AI-powered resume ranking tool that compares resumes to a job description using TF-IDF and cosine similarity.

---

## 📂 Project Structure

ai_resume_ranker/
│
├── resumes/ # Folder containing sample resumes (PDF)
│ ├── resume1.pdf
│ └── resume2.pdf
│
├── job_description.txt # Sample job description text
├── resume_ranker.py # Main Python script
├── ranking_results.csv # Output file with ranked results
├── requirements.txt # Dependencies
├── LICENSE # MIT License
└── README.md # This file

yaml
Copy
Edit

---

## 🚀 How It Works

1. Reads a job description from `job_description.txt`
2. Loads all PDF resumes from the `resumes/` folder
3. Applies TF-IDF vectorization using `scikit-learn`
4. Calculates cosine similarity between the job description and each resume
5. Ranks resumes by relevance and exports the results to `ranking_results.csv`

---

## 🧪 How to Run

```bash
git clone https://github.com/MIDHUN5832/ai_resume_ranker.git
cd ai_resume_ranker
pip install -r requirements.txt
python resume_ranker.py
📦 Requirements
Install dependencies using:

bash
Copy
Edit
pip install -r requirements.txt
Required Libraries:

scikit-learn

PyPDF2

📄 Sample Data
This repo includes example data for quick testing:

✅ A sample job description (job_description.txt)

✅ Two sample resumes in PDF format (resumes/ folder)

✅ Output CSV file (ranking_results.csv) showing similarity scores

📊 Output
After running the script:

Console displays ranked resume results

A CSV file (ranking_results.csv) is generated like this:

Resume	Similarity Score
resume1.pdf	0.66
resume2.pdf	0.04

🛡 License
This project is licensed under the MIT License.
© 2025 Midhun Kunjumon