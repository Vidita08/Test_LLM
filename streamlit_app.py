import streamlit as st

# Title of the app
st.title("🎈 My New App")

# Description
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Adding a text input field
user_input = st.text_input("Enter some text:")

# Display the entered text
st.write("You entered:", user_input)

# Adding a slider
number = st.slider("Select a number", min_value=0, max_value=100, value=25)
st.write("Selected number:", number)

# Adding a checkbox
checkbox = st.checkbox("Check me out!")
if checkbox:
    st.write("Checkbox is checked!")

# Adding a select box
option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", option)

# Adding a button
if st.button("Click me!"):
    st.write("Button was clicked!")

# Adding an image (make sure to put an image named 'sample.jpg' in the same directory or provide a URL)
st.image("https://via.placeholder.com/150", caption="Sample Image")

# Adding a map
import pandas as pd
import numpy as np

# Create a DataFrame with random coordinates
df = pd.DataFrame(
    np.random.randn(10, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(df)
