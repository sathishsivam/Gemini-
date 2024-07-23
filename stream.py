import streamlit as st
import pandas as pd



df = pd.DataFrame({"id": ["a", "b", "c"], "column": [4, 5, 6]}).set_index("id")
st.write(df)
x=st.text_input("id")
if x:
    st.write(df.loc[x, "column"])
    