ATS Resume Expert
ATS Resume Expert is a powerful Streamlit-based web application designed to help job seekers enhance their resumes by analyzing them against job descriptions using Google Generative AI (Gemini 1.5). The app provides actionable insights such as match percentage, missing keywords, and an AI-generated profile summary—boosting your resume’s chances of passing through Applicant Tracking Systems (ATS).

Features
✅ Resume vs. Job Description Match Analysis
Upload your resume (PDF) and compare it with a job description to evaluate compatibility.

✅ Match Percentage Calculation
Get an estimated match score (in percentage) between your resume and the job description.

✅ Missing Keywords Identification
Automatically detect important keywords missing from your resume.

✅ Profile Summary Generation
AI-generated summary based on your resume to improve professional branding.

✅ Structured Output
Results are presented in structured JSON format for clarity and reusability.



Technologies Used
Streamlit – For the interactive user interface

Google Generative AI (Gemini 1.5) – To analyze resumes and generate insights

PyPDF2 – To extract text from uploaded PDF resumes

dotenv – To securely load the Google API key

re (regex) – For cleaning and formatting AI responses

json – To parse and display structured analysis results
