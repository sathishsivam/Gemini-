import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import pandas as pd

from contextlib import redirect_stdout
from io import StringIO

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro")

def get_gemini_response(ques):
    response=model.generate_content(ques)
    return response.text

st.set_page_config(page_title="Data Analysis")
st.title("Gemini Data Analyst")
uploadedfile=st.file_uploader("Upload csv or excel file",type=["csv","xlsx"])

if uploadedfile is not None:
    # Check if the file exists
    if not os.path.isfile(uploadedfile.name):
        st.error(f"Error: File '{uploadedfile.name}' does not exist.")
        st.stop()

    # Read uploaded file into a DataFrame
    data = pd.read_csv(uploadedfile)

    # Display top 10 rows of the DataFrame
    st.subheader("Top 10 Rows of the DataFrame:")
    st.write(data.head(10))

    input=st.text_input("Prompt:","input")
    ques=f"use the dataframe data with {data.columns} and compute the output"+input

    res=get_gemini_response(ques)
    

    st.subheader("Gemini Response is....")

    st.write(res)