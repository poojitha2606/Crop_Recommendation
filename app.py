import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="centered"
)

model = pickle.load(open("model.pkl", "rb"))

st.title("🌱 Crop Recommendation System")

st.write(
    "Enter soil nutrient values and weather conditions to get the best crop recommendation."
)

col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", min_value=0.0)
    P = st.number_input("Phosphorus (P)", min_value=0.0)
    K = st.number_input("Potassium (K)", min_value=0.0)

with col2:
    temperature = st.number_input("Temperature (°C)")
    humidity = st.number_input("Humidity (%)")
    ph = st.number_input("pH Value")

rainfall = st.number_input("Rainfall (mm)", min_value=0.0)

if st.button("🌾 Predict Crop"):
    input_df = pd.DataFrame(
        [[N, P, K, temperature, humidity, ph, rainfall]],
        columns=[
            "N",
            "P",
            "K",
            "temperature",
            "humidity",
            "ph",
            "rainfall"
        ]
    )

    prediction = model.predict(input_df)

    st.success(f"✅ Recommended Crop: {prediction[0]}")
