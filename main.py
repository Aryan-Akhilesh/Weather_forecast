import streamlit as st

st.title("Weather forcast")

st.write("This minimalistic web application finds the weather forcast "
         "for the next few days")

place = st.text_input(label="Place:",
                      placeholder="Enter any place...")


days = st.slider(label="Forcast Days", min_value=1, max_value=5,
                 help="Select the number of days for which you"
                      " wish to see the forcast")

option = st.selectbox(label="Select type of data to view",
                      options=["Temperature", "Sky"])

st.subheader(f"{option} for the next {days} days in {place}")



