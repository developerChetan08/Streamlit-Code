import streamlit as st

# Title
st.title("Project Title")

# Header / Subheader
st.header("This is a header")
st.subheader("This is a Subheader")

# text
st.text("Hello Streamlit")

# markdown
st.markdown(" # This is our first markdown")
st.markdown(" #### This is our first markdown")

# Message / Colorful text
st.success("Scuessful Done")
st.info("Information")
st.warning("This is a warning")
st.error("This is an error")
st.exception("NameError('name pd is not defiened')")

import pandas
st.help(pandas)

# Writing text super function
st.write("Text with write")

##Image
from PIL import Image
img = Image.open("img_5terre.jpg")
st.image(img)
st.image(img, width = 300, caption = "Simple Image")

# Video adding
# vid_file = open("job.mov", "rb")
# vid_bytes = vid_file.read()
# st.video(vid_bytes)

# Audio
sudio_file = open("ring.mp3", "rb").read()
st.audio(sudio_file)

#Checkbox
# ML ( Gender , M / F)
if st.checkbox("Show / Hide"):
    st.text("Showing or Hiding widget")

# Radio Buttons
status = st.radio("What is your Status", ("Active", "Inactive"))

# Link with some function
if status == "Active":
    st.success("You are Active")

# Else function
if status == "Active":
    st.success("You are Active")
else:
    st.warning("Inactive, Activate it")

# SelectBox
occupation = st.selectbox("Your Occupation", ["Programmer", "Data Scientist", "Docter", "Businessman"])
st.write("You Selected this option", occupation)

# Multiselect
location = st.multiselect("Where do you work", ("Karnatka", "Mumbai", 
"Pune", "Delhi"))
# TO get all selected count
st.write("You Selected", len(location), "locations")

# Slider
lelvel = st.slider("What is your level", 1,5)


# Buttons
st.button("Simple Button")
if st.button("About"):
    st.text("Streamlit is cool")
if st.button("Submit"):
    st.text("Sucessful Submited")

# text Input
first_name = st.text_input("Enter your first name", "Type here..")
if st.button("Submit", key="1"):
    result = first_name.title()
    st.success(result)

# Text Area
message = st.text_area("Enter your message", "Type here..")
if st.button("Submit", key = "2"):
    result = message.title()
    st.success(result)


# Date Input
import datetime
today = st.date_input("Today is", datetime.datetime.now())

# Time
the_time = st.time_input("The time is", datetime.time())

#Display Json Output
st.text("Display json Data")
st.json({"Name":"Shivan",
        "Gender":"Male"})

# IMport numpy as np
st.text("Display Row Code")
st.code("import numpy as np")

# Display row code with dataframe
with st.echo():
    import pandas as pd
    df = pd.DataFrame()

# Progress bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress( p + 10)

#spinner
with st.spinner("Watinig .."):
    time.sleep(5)
st.success("Finished!")


st.title("Happy Birday!")

# ballon
st.balloons()

# Sidebar
st.sidebar.header("About")
st.sidebar.text("This is our demo project")

# Select Box
algoritmhs = st.sidebar.selectbox("Your Algorithm", ["Liner Regression", "Logistic Regression", "Decision tree",
"Random Forest"])


##https://github.com/Shivan118?tab=repositories