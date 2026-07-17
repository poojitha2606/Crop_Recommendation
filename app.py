
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





   from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        input_data = pd.DataFrame(
            [[N, P, K, temperature, humidity, ph, rainfall]],
            columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
        )

        prediction = model.predict(input_data)

        return render_template(
            'index.html',
            prediction_text=f"Recommended Crop: {prediction[0]}"
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text=f"Error: {str(e)}"
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True) 
