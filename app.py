# streamlit
# openAI
# pypdf2

import streamlit as st 
from openai import OpenAI
from PyPDF2 import PdfReader

st.title("AI RESUME ANALYZER")

resume_file=st.file_uploader( #None
    "upload yr resume here (pdf)",
    type=["pdf"]
)

job_desc=st.text_area(
    "enter job description here ",
    height=300
)

def extract_data_from_resume(file): # file param
    text=""
    extract_data=PdfReader(file)
    for i in extract_data.pages:
        text += i.extract_text()

    return text;    

if st.button("anlyze the resume"):
    
    if not resume_file:
        st.write("try to upload resume")
        st.stop()

    if not job_desc:
        st.write("fill jd in jd text area")
        st.stop()

    returnedPdfData=extract_data_from_resume(resume_file) # fun invokation :-- passing an arg resume_file    
    # st.write(returnedPdfData)


    with st.spinner("im thinking and anlyzing teh resume wait a sec"):
        # pass 
        system_prompt = f"""
    Your name is Resume Buddy.

    You are an expert recruiter and ATS analyzer.

    Analysis Type: {analysis_type}

    Rules:
    1. Compare resume with job description.
    2. Give clear score if possible.
    3. Mention missing skills.
    4. Suggest improvements.
    5. Use simple English.
    6. Use bullet points.
    """

        userPrompt=f"""
        
        this is my resume :-- 

        {returnedPdfData}

        this is job descrpition :-- 

        {job_desc}

        now anlyze the resume and job desc and give me improvements to match my skills with job description 
        
        """

