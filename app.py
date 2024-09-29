import streamlit as st
import pandas as pd
import pickle


model_path = 'best_gradient_boosting_model.pkl'  
with open(model_path, 'rb') as f:
    model = pickle.load(f)


st.title("Wind Power Prediction")


temperature_2m = st.number_input("Temperature (2m) [°C]", value=0.0)
relativehumidity_2m = st.number_input("Relative Humidity (2m) [%]", value=0.0)
dewpoint_2m = st.number_input("Dewpoint (2m) [°C]", value=0.0)
windspeed_10m = st.number_input("Windspeed (10m) [m/s]", value=0.0)
windspeed_100m = st.number_input("Windspeed (100m) [m/s]", value=0.0)
winddirection_10m = st.number_input("Wind Direction (10m) [degrees]", value=0.0)
winddirection_100m = st.number_input("Wind Direction (100m) [degrees]", value=0.0)
windgusts_10m = st.number_input("Wind Gusts (10m) [m/s]", value=0.0)


input_data = pd.DataFrame({
    'temperature_2m': [temperature_2m],
    'relativehumidity_2m': [relativehumidity_2m],
    'dewpoint_2m': [dewpoint_2m],
    'windspeed_10m': [windspeed_10m],
    'windspeed_100m': [windspeed_100m],
    'winddirection_10m': [winddirection_10m],
    'winddirection_100m': [winddirection_100m],
    'windgusts_10m': [windgusts_10m]
})


if st.button("Predict Power"):
    prediction = model.predict(input_data)
    st.write(f"Predicted Wind Power: {prediction[0]:.2f} MW")


st.sidebar.header("Model Information")
st.sidebar.write("This model predicts wind power generation based on meteorological inputs.")
