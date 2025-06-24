import os
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from a PDF
def extract_text_from_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "
    return text.strip()

# Load job description
with open("job_description.txt", "r", encoding="utf-8") as f:
    job_description = f.read().strip()

# Load resumes
resume_texts = []
resume_names = []

for file in os.listdir("resumes"):
    path = os.path.join("resumes", file)
    if file.endswith(".pdf"):
        text = extract_text_from_pdf(path)
    elif file.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            text = f.read().strip()
    else:
        continue

    if text:
        resume_texts.append(text)
        resume_names.append(file)

# Validate
if not resume_texts:
    print(" No resumes found.")
    exit()

# TF-IDF vectorization
documents = [job_description] + resume_texts
vectorizer = TfidfVectorizer(stop_words='english', token_pattern=r'\b[a-zA-Z]{2,}\b')
tfidf_matrix = vectorizer.fit_transform(documents)

if tfidf_matrix.shape[0] < 2 or tfidf_matrix.shape[1] == 0:
    print(" Not enough meaningful data to compare.")
    exit()

# Cosine similarity
scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
ranked = sorted(zip(resume_names, scores), key=lambda x: x[1], reverse=True)

# Output results 
print("\n Ranked Resumes:")
for i, (name, score) in enumerate(ranked, 1):
    print(f"{i}. {name} — Score: {score:.2f}")
import csv

# Export results to CSV
with open("ranking_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Rank", "Resume Name", "Score"])

    for i, (name, score) in enumerate(ranked, 1):
        writer.writerow([i, name, f"{score:.2f}"])

print("\nResults saved to ranking_results.csv")

