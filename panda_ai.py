import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

# https://www.kaggle.com/datasets/unsdsn/world-happiness?resource=download
# link for a kaggle dataset of happiest contries

import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


llm = OpenAI(api_token=OPENAI_API_KEY)

pandas_ai = PandasAI(llm)

# configure streamlit app
st.set_page_config(
    page_title="Chat With Data",
    page_icon="🐼",
    layout="centered",
    initial_sidebar_state="auto",
)
st.title("📊Chat With Data")
st.subheader("This app is using PandasAI to chat with data")

# add file uploader to load csv file dataset
file = st.file_uploader("Upload Dataset", type=["csv"])

# read the data from the file if the file is uploaded
if file is not None:
    df = pd.read_csv(file)
    st.write(df)

# add text input for prompt
prompt = st.text_input("Enter Prompt", "which sex was most likely to have survived?")

# add button to run pandas_ai
if st.button("Run", key="run1"):
    # add info about the prompt
    st.info("Your prompt is: " + prompt)
    # add a loading indicator
    with st.spinner("Analyzing data..."):
        try:
            response = pandas_ai.run(df, prompt=prompt)
            st.success(response)
        except Exception as e:
            st.error(e)

# create some example prompts
st.subheader("Prompts to try out")
st.code("which sex was most likely to have survived? how much more likely?")
st.code("which class was most likely to have survived? how much more likely?")
st.code("which age was most likely to have survived? how much more likely?")
st.code("Is there any correlation between class and survival rate?")
st.code("calculate the survival rate for each sex")
st.code("calculate the survival rate for each class")
st.code("was older or younger people more likely to survive?")
st.code("Chart the survival rate for each class")
st.code("according to this data can we consider Morocco as a happy country?")
st.code(
    "i'm living in Morocco, and i won the usa lottery, what do you think i should decide?"
)

if file is not None:
    men = df[df["Sex"] == "male"]
    women = df[df["Sex"] == "female"]
    if st.button("Calculate the survival rate manually"):
        st.write("survival rate for men is : ", men["Survived"].sum() / len(men))
        st.write("survival rate for women is : ", women["Survived"].sum() / len(women))
