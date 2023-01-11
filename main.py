import streamlit as st
import plotly.express as px
import backend

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

if place:
    try:
        data = backend.get_data(place, days)
    except KeyError:
        st.write("This place doesn't exist.")
    else:
        if option == "Temperature":
            filtered_data = [dnr["main"]["temp"] for dnr in data]
            dates = [dnr["dt_txt"] for dnr in data]
            temp = filtered_data
            figure = px.line(x=dates, y=temp, labels={"x": "Date", "y": "Temperature(C)"})
            st.plotly_chart(figure)
        elif option == "Sky":
            images = {"Clear": "icons/clear.png", "Clouds": "icons/cloud.png",
                      "Rain": "icons/rain.png", "Snow": "icons/snow.png"}
            filtered_data = [dnr["weather"][0]["main"] for dnr in data]
            dates = [dnr["dt_txt"] for dnr in data]
            image_paths = [images[condition] for condition in filtered_data]
            st.image(image_paths, width=125, caption=dates)




