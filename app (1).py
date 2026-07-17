
import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('model.pkl', 'rb'))

st.title('🌱 Crop Recommendation System')

N = st.number_input('Nitrogen')
P = st.number_input('Phosphorus')
K = st.number_input('Potassium')
temperature = st.number_input('Temperature')
humidity = st.number_input('Humidity')
ph = st.number_input('pH')
rainfall = st.number_input('Rainfall')

if st.button('Predict Crop'):
    input_df = pd.DataFrame(
        [[N, P, K, temperature, humidity, ph, rainfall]],
        columns=[
            'N','P','K',
            'temperature',
            'humidity',
            'ph',
            'rainfall'
        ]
    )

    prediction = model.predict(input_df)

    st.success(f'Recommended Crop: {prediction[0]}')
