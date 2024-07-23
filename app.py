from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# for i in genai.list_models():
#     print(i.name)

def get_gemini_response(quest):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(quest)
    return response.text


import streamlit as st

st.set_page_config(page_title="Gemini QA")
st.header("Gemini Model with QA")
input=st.text_input("Input:","input")
submit=st.button("Ask to gemini")

if submit:
     res=get_gemini_response(input)
     st.subheader("Response from Gemini is.. ")
     st.write(res)
    









