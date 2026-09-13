import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("random_forest_loan_default_model.pkl")

st.title("💳 Loan Default Prediction")
st.write("Predict whether a customer is likely to default on their next payment.")

st.subheader("Customer Information")

limit_bal = st.number_input("Credit Limit", min_value=0.0, value=50000.0)
sex = st.selectbox("Sex", [1, 2])
education = st.selectbox("Education", [1, 2, 3, 4])
marriage = st.selectbox("Marriage", [1, 2, 3])
age = st.number_input("Age", min_value=18, max_value=100, value=30)

st.subheader("Payment Status")

pay_0 = st.number_input("PAY_0", value=0)
pay_2 = st.number_input("PAY_2", value=0)
pay_3 = st.number_input("PAY_3", value=0)
pay_4 = st.number_input("PAY_4", value=0)
pay_5 = st.number_input("PAY_5", value=0)
pay_6 = st.number_input("PAY_6", value=0)

st.subheader("Bill Amounts")

bill_amt1 = st.number_input("Bill Amount 1", value=0.0)
bill_amt2 = st.number_input("Bill Amount 2", value=0.0)
bill_amt3 = st.number_input("Bill Amount 3", value=0.0)
bill_amt4 = st.number_input("Bill Amount 4", value=0.0)
bill_amt5 = st.number_input("Bill Amount 5", value=0.0)
bill_amt6 = st.number_input("Bill Amount 6", value=0.0)

st.subheader("Previous Payments")

pay_amt1 = st.number_input("Payment Amount 1", value=0.0)
pay_amt2 = st.number_input("Payment Amount 2", value=0.0)
pay_amt3 = st.number_input("Payment Amount 3", value=0.0)
pay_amt4 = st.number_input("Payment Amount 4", value=0.0)
pay_amt5 = st.number_input("Payment Amount 5", value=0.0)
pay_amt6 = st.number_input("Payment Amount 6", value=0.0)

if st.button("Predict Default Risk"):

    input_data = pd.DataFrame([[
        1, limit_bal, sex, education, marriage, age,
        pay_0, pay_2, pay_3, pay_4, pay_5, pay_6,
        bill_amt1, bill_amt2, bill_amt3, bill_amt4, bill_amt5, bill_amt6,
        pay_amt1, pay_amt2, pay_amt3, pay_amt4, pay_amt5, pay_amt6
    ]], columns=[
        "ID", "LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE",
        "PAY_0", "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6",
        "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4",
        "BILL_AMT5", "BILL_AMT6",
        "PAY_AMT1", "PAY_AMT2", "PAY_AMT3",
        "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"
    ])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠ High Risk: Customer is likely to default.")

        st.subheader("Business Recommendation")
        st.write("""
        - Perform additional credit-risk verification.
        - Reduce credit limit if necessary.
        - Monitor repayment behaviour closely.
        - Offer repayment assistance or reminders.
        """)

    else:
        st.success("✅ Low Risk: Customer is unlikely to default.")

        st.subheader("Business Recommendation")
        st.write("""
        - Customer is eligible for normal credit approval.
        - Continue standard repayment monitoring.
        - Consider loyalty or credit enhancement offers.
        """)
