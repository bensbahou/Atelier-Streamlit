# simple hello world streamlit app

import streamlit as st
from time import sleep

st.title("Hello World")
# st.help(st.title)
# add a subheader
st.subheader("This is a simple hello world app")

st.write("This is the content of the hello world app")
'Yes, this it is working fine and I am able to see the changes in the app'

# add a button
if st.button("Click Me"):
    st.write("You have clicked the button")

# add a name text box
name = st.text_input("Enter your name")
st.write("Hello", name)

# add a number input box with step size of 1
number_a = st.number_input("Enter a number", step=1)
number_b = st.number_input("Enter another number", step=1)
# show the sum of the two numbers
st.write("The sum of the two numbers is", number_a + number_b)

# add a slider
slider = st.slider("Select a value", min_value=0, max_value=100)
st.write("The value of the slider is", slider)

# add a select box
select = st.selectbox("Select a number", [1, 2, 3, 4, 5])
st.write("The value of the select box is", select)

# add a multi select box
multi_select = st.multiselect("Select a number", [1, 2, 3, 4, 5])
st.write("The value of the multi select box is", multi_select)

# add a checkbox
checkbox = st.checkbox("Check the box")
st.write("The value of the checkbox is", checkbox)

# add a radio button
radio = st.radio("Select a number", [1, 2, 3, 4, 5])
st.write("The value of the radio button is", radio)

# add a file uploader
file = st.file_uploader("Upload a file")
st.write("The file name is : ", file.name if file else "No file uploaded")


# add a color picker
color = st.color_picker("Pick a color")
st.write("The color you have selected is", color)

# add a date picker
date = st.date_input("Select a date")
st.write("The date you have selected is", date)

# add a time picker
time = st.time_input("Select a time")
st.write("The time you have selected is", time)

# add a text area
text_area = st.text_area("Enter some text")
st.write("The text you have entered is", text_area)

# add a code editor
code = st.code("print('Hello World')")


# add a button to show the code
if st.button("Show Code"):
    st.code("""
    with st.spinner("Wait for it..."):
    sleep(5)


    st.success("Done!")
    """)
# add a progress bar and make balloon animation when the progress bar is full

progress_bar = st.progress(50)
for i in range(50, 100):
    progress_bar.progress(i + 1)
    if (i + 1) == 100:
        st.balloons()
    else:

        sleep(0.1)

# add a spinner
with st.spinner("Wait for it..."):
    sleep(5)


st.success("Done!")

# add a success message
st.success("This is a success message")

# add an info message
st.info("This is an info message")

# add a warning message
st.warning("This is a warning message")

# add an error message
st.error("This is an error message")

# add an exception
st.exception("NameError('name three not defined')")

# add a help message
st.help(range)
