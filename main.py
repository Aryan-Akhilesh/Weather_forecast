import streamlit as st
import plotly.express as px

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

x = ["2023-01-08", "2023-01-09", "2023-01-10"]
y = [25, 35, 45]
figure = px.line(x=x, y=y, labels={"x": "Date", "y": "Temperature(C)"})

st.plotly_chart(figure)



