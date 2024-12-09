import streamlit as st
import pandas as pd

# Title
st.title("Map Example with Streamlit")

# Create sample data with latitude and longitude
data = pd.DataFrame({
    'latitude': [6.9271, 7.8731, 8.3114],  # Example latitudes
    'longitude': [79.8612, 80.7718, 80.4037]  # Example longitudes
})

# Display map with the data
st.map(data)

# Additional info
st.write("This map displays locations from the provided latitude and longitude data.")
