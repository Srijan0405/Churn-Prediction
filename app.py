import streamlit as st
import joblib
import numpy as np

model = joblib.load('logistic_model.pkl')

st.title("Customer Churn Prediction App")

def user_input():
    gender = st.selectbox("Gender", ['Male', 'Female'])
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Has Partner", ['Yes', 'No'])
    Dependents = st.selectbox("Has Dependents", ['Yes', 'No'])
    tenure = st.slider("Tenure (months)", 0, 72)
    PhoneService = st.selectbox("Phone Service", ['Yes', 'No'])
    InternetService = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
    MonthlyCharges = st.number_input("Monthly Charges")
    TotalCharges = st.number_input("Total Charges")
    Contract = st.selectbox("Contract Type", ['Month-to-month', 'One year', 'Two year'])
    PaperlessBilling = st.selectbox("Paperless Billing", ['Yes', 'No'])
    PaymentMethod = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'])

    # Convert inputs to model format
    input_data = {
        'SeniorCitizen': SeniorCitizen,
        'tenure': tenure,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges,
        # Add one-hot encoding manually
        'gender_Male': 1 if gender == 'Male' else 0,
        'Partner_Yes': 1 if Partner == 'Yes' else 0,
        'Dependents_Yes': 1 if Dependents == 'Yes' else 0,
        'PhoneService_Yes': 1 if PhoneService == 'Yes' else 0,
        'InternetService_Fiber optic': 1 if InternetService == 'Fiber optic' else 0,
        'InternetService_No': 1 if InternetService == 'No' else 0,
        'Contract_One year': 1 if Contract == 'One year' else 0,
        'Contract_Two year': 1 if Contract == 'Two year' else 0,
        'PaperlessBilling_Yes': 1 if PaperlessBilling == 'Yes' else 0,
        'PaymentMethod_Electronic check': 1 if PaymentMethod == 'Electronic check' else 0,
        'PaymentMethod_Mailed check': 1 if PaymentMethod == 'Mailed check' else 0,
        'PaymentMethod_Bank transfer': 1 if PaymentMethod == 'Bank transfer' else 0
    }

    return np.array([list(input_data.values())])

input_df = user_input()

if st.button("Predict"):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.error("⚠️ This customer is likely to churn.")
    else:
        st.success("✅ This customer is likely to stay.")
