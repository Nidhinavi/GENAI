import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
import re  # To clean unwanted characters

# Load environment variables
load_dotenv()

# Configure the Google Generative AI client
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini AI response
def get_gemini_response(input_prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(input_prompt)
    return response.text

# Function to extract text from uploaded PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text

# Function to generate the input prompt dynamically
def generate_input_prompt(resume_text, job_description):
    return f"""
    Hey Act Like a skilled or very experienced ATS(Application Tracking System)
    with a deep understanding of tech field, software engineering, data science, data analysis, 
    and big data engineering. Your task is to evaluate the resume based on the given job description.
    You must consider the job market is very competitive and you should provide 
    the best assistance for improving the resumes. Assign the percentage Matching based 
    on the JD and the missing keywords with high accuracy.
    Resume: {resume_text}
    Description: {job_description}
    
    I want the response in one single string having the structure:
    {{
        "JD Match": "Percentage Match",
        "MissingKeywords": ["list of missing keywords"],
        "Profile Summary": "Summary of the profile"
    }}
    """

# Function to preprocess the raw response
def preprocess_response(raw_response):
    # Remove backticks and extra annotations
    cleaned_response = re.sub(r"```.*?json|```", "", raw_response, flags=re.DOTALL).strip()
    return cleaned_response

# Streamlit app setup
st.title("Resume Expert - ATS")
st.text("Boost your job prospects: Upload your resume PDF and job description to optimize your ATS score")
jd = st.text_area("Paste your job description here")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload a PDF file")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None and jd.strip():
        # Extract resume text
        resume_text = input_pdf_text(uploaded_file)
        # Generate the input prompt
        input_prompt = generate_input_prompt(resume_text, jd)
        try:
            # Get response from Gemini
            raw_response = get_gemini_response(input_prompt)
            # Preprocess the response to remove unwanted characters
            cleaned_response = preprocess_response(raw_response)
            try:
                # Parse the cleaned response as JSON
                parsed_response = json.loads(cleaned_response)
                st.subheader("Analysis Result")
                st.json(parsed_response)  # Display the response as structured JSON
            except json.JSONDecodeError:
                st.error("Failed to parse the cleaned response as JSON. The response might still have issues.")
                st.text("Cleaned Raw Response:")
                st.code(cleaned_response)
        except Exception as e:
            st.error(f"An error occurred while processing: {e}")
    else:
        st.error("Please provide both a job description and upload a resume.")
