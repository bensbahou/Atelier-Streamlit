# guide for workshop about using streamlit to create web apps
# for data science

import streamlit as st

# Title
st.title("Streamlit Guide")

# First step is to install streamlit
st.subheader("1. Install VS Code")
st.write("You can install VS Code from here: https://code.visualstudio.com/")


# Second step is to install python
st.subheader("2. Install Python")
st.write("You can install Python from here: https://www.python.org/downloads/")
with st.expander("Check if Python is installed"):
    st.write(
        "To check if Python is installed or not, run the following command in your terminal:")
    st.code("python --version")
    st.write(
        "If you see the version of Python installed, then it is installed successfully.")
    st.write("If you see an error, then it is not installed. In that case, you can install it from the link above.")

# Third step is to install streamlit
st.subheader("3. Install Streamlit")
st.write("You can install Streamlit by running the following command in your terminal:")
st.code("pip install streamlit")
with st.expander("Check if Streamlit is installed"):
    st.write(
        "To check if Streamlit is installed or not, run the following command in your terminal:")
    st.code("streamlit --version")
    st.write(
        "If you see the version of Streamlit installed, then it is installed successfully.")
    st.write("If you see an error, then it is not installed. In that case, you can install it from the link above.")

# Fourth step is to create a streamlit app
st.subheader("4. Create a Streamlit app")
st.write("Create a simple python file with the some code")
with st.expander("See example of a simple hello world app"):

    st.code("""
	import streamlit as st

	st.title("Hello World")
	st.write("This is a simple hello world app")
	""")

st.write("Save the file as filename.py")

# Fifth step is to run the streamlit app
st.subheader("5. Run the Streamlit app")
st.write("Run the file using the following command:")
st.code("streamlit run filename.py")
st.write("You should see a new tab open in your browser with the title 'Hello World'")
st.write("Congratulations! You have successfully created your first Streamlit app.")

# Sixth step is to install Git
st.subheader("6. Install Git")
st.write("You can install Git from here: https://git-scm.com/downloads")
with st.expander("Check if Git is installed"):
    st.write(
        "To check if Git is installed or not, run the following command in your terminal:")
    st.code("git --version")
    st.write(
        "If you see the version of Git installed, then it is installed successfully.")
    st.write(
        "If you see an error, then it is not installed. In that case, you can install it from the link above.")

# Seventh step is to create a GitHub account
st.subheader("7. Create a GitHub account if you don't have one.")
st.write("""You can create a GitHub account from here: https://github.com/join""")

# Eighth step is to create a new repository
st.subheader("8. Create a new repository")
st.write("You can create a new repository from here: https://github.com/new")
with st.expander("See example of creating a new repository"):
    st.write("Enter the name of the repository")
    st.write("Select 'Public' option")
    st.write("Select 'Add a README file' option")
    st.write("Click on 'Create repository' button")

# Ninth step is to clone the repository
st.subheader("9. Clone the repository")
st.write("You can clone the repository by running the following command in your terminal:")
st.code("git clone <link> ")

# Tenth step is to add the streamlit app to the repository
st.subheader("10. Add the streamlit app to the repository")
st.write("Copy the streamlit app file to the repository folder")


# Eleventh step is to create a requirements.txt file
st.subheader("11. Create a requirements.txt file")
st.write("Create a requirements.txt file and add the required packages to it")

# Twelfth step is to create a commit and push the changes
st.subheader("12. Create a commit and push the changes")
st.write("Run the following commands in your terminal:")
st.code("git add .")
st.code("git commit -m 'Add streamlit app'")
st.code("git push")

# Thirteenth step is to deploy the app to Streamlit Share
st.subheader("13. Deploy the app to Streamlit Share")
st.write("Go to https://share.streamlit.io/")
st.write("Click on 'New app' button")
st.write("Select the repository")
st.write("Click on 'Deploy' button")
st.write("Wait for the app to deploy")
st.write("Click on the link to view the app")
st.write("Congratulations! You have successfully deployed your first Streamlit app.")
