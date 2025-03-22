import streamlit as st
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pickle

st.title("Insurance Charges Prediction")

df = pd.read_csv('insurance.csv')
#st.dataframe(df)

age = st.slider('Age', min_value=18, max_value=100, value=30)
sex = st.selectbox('Sex', ['male', 'female'])
bmi = st.slider('BMI', min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input('Children', min_value=0, max_value=5, value=0)
smoker = st.selectbox('Smoker', ['yes', 'no'])
region = st.selectbox('Region', ['southwest', 'southeast', 'northwest', 'northeast'])

# Create DataFrame with scalar values (not lists)
input_data = pd.DataFrame({
    'age': age,
    'sex': sex,
    'bmi': bmi,
    'children': children,
    'smoker': smoker,
    'region': region
}, index=[0])  # Add index to make it a DataFrame

st.subheader("Input Data")
st.dataframe(input_data)

columns_to_encode = ['sex', 'smoker', 'region']
numerical_cols = ['age', 'bmi']

ohe = OneHotEncoder(sparse_output=False, drop='first')
ohe.fit(df[columns_to_encode])

encoded_data = ohe.transform(input_data[columns_to_encode])
encoded_columns = ohe.get_feature_names_out(columns_to_encode)
encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns, index=input_data.index)

#st.subheader("One-Hot Encoded dataframe")
#st.dataframe(encoded_df)

input_data = pd.concat([input_data.drop(columns=columns_to_encode), encoded_df], axis=1)
#st.subheader("Dataframe with One-hot encoded columns")
#st.dataframe(input_data)

scaler = StandardScaler()
scaler.fit(df[numerical_cols])
input_data[numerical_cols] = scaler.transform(input_data[numerical_cols])

#st.subheader("standardized numerical data")
#st.dataframe(input_data[numerical_cols])

st.subheader("Preprocessed Data")
st.dataframe(input_data)

# Load the model
try:
    with open('random_forest_model.pkl', 'rb') as file:
        model = pickle.load(file)

    if st.button("Predict Insurance Charges"):
        prediction = model.predict(input_data)
        st.write(f"Predicted Insurance Charges: ${prediction[0]:.2f}")

except FileNotFoundError:
    st.error("Model file 'insurance_model.pkl' not found. Please train and save your model.")
except Exception as e:
    st.error(f"An error occurred: {e}")