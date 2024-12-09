import streamlit as st
import pandas as pd
import numpy as np

# Page Title
st.set_page_config(page_title="Interactive Map with Streamlit", layout="wide")
st.title("Interactive Map Example with Streamlit")
st.write("This app demonstrates how to use maps with dynamic data in Streamlit.")

# Sidebar Configuration
st.sidebar.title("Map Configuration")
st.sidebar.write("Customize your map settings here:")

# Generate random data (for demo purposes)
# Use your own latitude and longitude data here
default_lat = 6.9271  # Default latitude (Colombo)
default_lon = 79.8612  # Default longitude (Colombo)
n_points = st.sidebar.slider("Number of Points", min_value=10, max_value=500, value=100)
radius = st.sidebar.slider("Radius (km)", min_value=1, max_value=50, value=10)

# Generate random lat/long points around a default center
random_data = pd.DataFrame({
    'latitude': default_lat + np.random.uniform(-radius / 100, radius / 100, n_points),
    'longitude': default_lon + np.random.uniform(-radius / 100, radius / 100, n_points)
})

# Display the map
st.subheader("Generated Map")
st.write("The map below shows randomly generated points based on your input.")
st.map(random_data)

# Upload custom dataset
st.subheader("Upload Your Own Data")
uploaded_file = st.file_uploader("Choose a CSV file with latitude and longitude columns", type="csv")

if uploaded_file is not None:
    custom_data = pd.read_csv(uploaded_file)

    # Ensure the necessary columns exist
    if {'latitude', 'longitude'}.issubset(custom_data.columns):
        st.map(custom_data)
        st.success("Map updated with uploaded data!")
    else:
        st.error("The uploaded file must contain 'latitude' and 'longitude' columns.")

# Add interactivity (select box for viewing options)
st.subheader("View Data")
view_option = st.selectbox("Select data to view:", ["Random Data", "Uploaded Data (if available)"])

if view_option == "Random Data":
    st.write("Displaying generated data:")
    st.dataframe(random_data)
elif uploaded_file is not None and view_option == "Uploaded Data (if available)":
    st.write("Displaying uploaded data:")
    st.dataframe(custom_data)

# Footer
st.write("### Notes:")
st.markdown(
    """
    - The random data points are generated around the default center (Colombo) using the configured radius.
    - If you upload your own dataset, make sure it has `latitude` and `longitude` columns for proper mapping.
    """
)

st.sidebar.info("Explore more features of Streamlit at [streamlit.io](https://streamlit.io)")
