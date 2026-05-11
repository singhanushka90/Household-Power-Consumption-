import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('random_forest_power_model.pkl')
scaler = joblib.load('scaler.save')

st.title("Household Global Active Power Prediction")
st.sidebar.header("Input Parameters")

def user_input_features():
    Global_reactive_power = st.sidebar.number_input('Global Reactive Power', 0.0, 5.0, step=0.01)
    Voltage = st.sidebar.number_input('Voltage', 220.0, 250.0, step=0.1)
    Sub_metering_1 = st.sidebar.number_input('Sub Metering 1', 0.0, 50.0, step=1.0)
    Sub_metering_2 = st.sidebar.number_input('Sub Metering 2', 0.0, 50.0, step=1.0)
    Sub_metering_3 = st.sidebar.number_input('Sub Metering 3', 0.0, 50.0, step=1.0)
    hour = st.sidebar.slider('Hour', 0, 23, 12)
    day = st.sidebar.slider('Day', 1, 31, 15)
    month = st.sidebar.slider('Month', 1, 12, 6)
    weekday = st.sidebar.slider('Weekday (0=Mon, 6=Sun)', 0, 6, 2)
    data = np.array([[Global_reactive_power, Voltage, Sub_metering_1, Sub_metering_2,
                      Sub_metering_3, hour, day, month, weekday]])
    return data

input_features = user_input_features()

if st.button('Predict'):
    # SCALE the input before predict!
    scaled_input = scaler.transform(input_features)
    prediction = model.predict(scaled_input)
    st.success(f'Predicted Global Active Power: {prediction[0]:.3f}')