import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI


OPENAI_API_KEY = "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"
llm = OpenAI(api_token=OPENAI_API_KEY)

pandas_ai = PandasAI(llm)


st.title("PandasAI Demo")
st.subheader("This is a simple app to demonstrate PandasAI")

# add file uploader to load csv file dataset
file = st.file_uploader("Upload Dataset", type=["csv"])

# read the data from the file if the file is uploaded
if file is not None:
    df = pd.read_csv(file)
    st.write(df.head())

# add text input for prompt
prompt = st.text_input("Enter Prompt", "which sex was most likely to have survived?")

# add button to run pandas_ai
if st.button("Run", key="run1"):
    # add a loading indicator
    with st.spinner("Running..."):
        try:
            response = pandas_ai.run(df, prompt=prompt)
            st.write(response)
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

men = df[df["Sex"] == "male"]
women = df[df["Sex"] == "female"]
if st.button("Calculate the survival rate manually"):
    st.write("survival rate for men is : ", men["Survived"].sum() / len(men))
    st.write("survival rate for women is : ", women["Survived"].sum() / len(women))
