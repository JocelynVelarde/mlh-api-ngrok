import streamlit as st
import requests

st.title("Ultrasonic sensor readings")
st.image("sensor.png") 

st.divider()

st.write("Click on the button to fetch ultrasonic data")
if st.button("Fetch Data"):
    try:
        response = requests.get("https://3255-189-175-70-116.ngrok-free.app/sensors")
        if response.status_code == 200:
            data = response.json()
            st.write("Ultrasonic Sensor Data:")
            st.json(data)  
        else:
            st.error(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {e}")