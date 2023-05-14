# list of the necessary tools for the project
import streamlit as st


st.title("Tools and accounts for the workshop")
st.info(
    "It's always better to install the tools before the workshop day. but if you can't, it's still okay. we'll take the time to insure that everyone has the tools installed."
)
st.header("Tools")
st.subheader("1. VS Code")
st.write("You can install VS Code from here: https://code.visualstudio.com/")
st.subheader("2. Python")
st.write("You can install Python from here: https://www.python.org/downloads/")

with st.expander("Check if Python is installed"):
    st.write(
        "To check if Python is installed or not, run the following command in your terminal:"
    )
    st.code("python --version")
    st.write(
        "If you see the version of Python installed, then it is installed successfully."
    )
    st.write(
        "If you see an error, then it is not installed. In that case, you can install it from the link above."
    )

st.subheader("3. Streamlit")
st.write("You can install Streamlit by running the following command in your terminal:")
st.code("pip install streamlit")
with st.expander("Check if Streamlit is installed"):
    st.write(
        "To check if Streamlit is installed or not, run the following command in your terminal:"
    )
    st.code("streamlit --version")
    st.write(
        "If you see the version of Streamlit installed, then it is installed successfully."
    )
    st.write(
        "If you see an error, then it is not installed. In that case, you can install it from the link above."
    )

st.subheader("4. Git")
st.write("You can install Git from here: https://git-scm.com/downloads")
with st.expander("Check if Git is installed"):
    st.write(
        "To check if Git is installed or not, run the following command in your terminal:"
    )
    st.code("git --version")
    st.write(
        "If you see the version of Git installed, then it is installed successfully."
    )
    st.write(
        "If you see an error, then it is not installed. In that case, you can install it from the link above."
    )


st.header("Accounts")
st.subheader("1. OpenAi")
st.write("You can create an account from here: https://platform.openai.com")
st.subheader("2. Github")
st.write("You can create an account from here: https://github.com/join ")
st.subheader("3. Github Copilot (Optional)")
st.write("You can create an account from here: https://copilot.github.com")
st.success(
    "Note: Github Copilot is not necessary for the workshop, but it is very recommended."
)

st.success(
    "It will make the workshop more fun and much easier (More than you can imagine)."
)
st.write(
    "You'll need to subscribe to the free 30 days trial - credit card or paypal required -."
)


st.info(
    "Many poeple don't feel comfortable using their credit cards online, but this worth giving it a try."
)
st.write("You can cancel anytime later!")
st.header("For Linux and Mac users only")
st.write(
    "I believe the above tools are available for Linux and Mac users. but there may be some differences in the installation process."
)
st.write("Please refer to the official documentation of each tool for more details.")
