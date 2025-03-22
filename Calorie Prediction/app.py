import pandas as pd
import numpy as np
import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler

st.title("Calorie Prediction")

df = pd.read_csv("exercise.csv")
op = pd.read_csv("calories.csv")
df['Calorie'] = op['Calories']
df.drop(['User_ID'], axis='columns', inplace=True)


gender = st.selectbox('Sex', ['male', 'female'])
age = st.slider('Age', min_value=18, max_value=100, value=30)
height = st.slider('Height', min_value=120, max_value=225)
weight = st.slider('Weight', min_value=30, max_value=135)
duration = st.slider('Duration', min_value=1, max_value=60)
heart_rate = st.slider('Heart_Rate', min_value=60, max_value=140)
body_temp = st.slider('Body_Temp', min_value=36, max_value=42)

input_data = pd.DataFrame({
    'Gender' : gender,
    'Age' : age,
    'Height' : height,
    'Weight' : weight,
    'Duration' : duration,
    'Heart_Rate' : heart_rate,
    'Body_Temp' : body_temp
}, index=[0])

st.subheader('Input_data')
st.dataframe(input_data)

# Preprocessing
df.replace({'Gender' : {'male':0, 'female':1}}, inplace=True)
input_data.replace({'Gender' : {'male':0, 'female':1}}, inplace=True)

X = df.drop(['Calorie'], axis='columns')

scaler = StandardScaler()
scaler.fit(X)
input_data = pd.DataFrame(scaler.transform(input_data), columns=X.columns)

st.subheader('Preprocessed Data')
st.dataframe(input_data)

with open('Calorie_model.pkl', 'rb') as file:
    model = pickle.load(file)

if st.button('Predict Calorie'):
    prediction = model.predict(input_data)
    prediction_value = prediction[0]
    prediction_rounded = int(round(prediction_value * 100))
    st.write("Predicted calorie : ", + prediction_rounded)