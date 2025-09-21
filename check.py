import requests
import os

# API endpoint
url = "http://127.0.0.1:8000/api/candidates/"

# Candidate data
data = {
    "name": "John Doe",
    "address": "123 Example Street",
    "skills": "Django, Python, REST API",
    "github_link": "https://github.com/johndoe",
    "age": 25,
    "email": "john@example.com",
    "phone_number": "+12345678901",
    "college_name": "ABC University",
    "passing_year": 2021
}

# Path to resume file
resume_path = "download.pdf"   # <-- change to your test file

# Check if file exists before sending
if not os.path.isfile(resume_path):
    raise FileNotFoundError(f"Resume file not found: {resume_path}")

# Open file for upload
with open(resume_path, "rb") as resume_file:
    files = {"resume": (os.path.basename(resume_path), resume_file, "application/pdf")}
    
    # Send POST request
    response = requests.post(url, data=data, files=files)

# Print results
print("Status Code:", response.status_code)
try:
    print("Response JSON:", response.json())
except Exception:
    print("Response Text:", response.text)
