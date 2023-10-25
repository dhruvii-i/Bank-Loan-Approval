import streamlit as st
from PIL import Image
import pickle

model = pickle.load(open('Model/knn_model.pkl', 'rb'))

def run():
    
    st.title("Bank Loan Prediction using Machine Learning")

    ## Account No
    account_no = st.text_input('Account number')

    ## For gender
    gen_display = ('Female', 'Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender", gen_options, format_func=lambda x: gen_display[x])

    ## For Marital Status
    mar_display = ('No', 'Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    ## No of dependents
    dep_display = ('No', 'One', 'Two', 'More than Two')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Dependents", dep_options, format_func=lambda x: dep_display[x])

    ## For education
    edu_display = ('Not Graduate', 'Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education", edu_options, format_func=lambda x: edu_display[x])

    ## For employment status
    emp_display = ('Yes', 'No')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Self Employed", emp_options, format_func=lambda x: emp_display[x])

    ## For Property status
    prop_display = ('Rural', 'Semi-Urban', 'Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Property Area", prop_options, format_func=lambda x: prop_display[x])

    ## For Credit Score
    cred_display = ('0', '1')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit Score", cred_options, format_func=lambda x: cred_display[x])

    ## Applicant Monthly Income
    mon_income = st.number_input("Applicant's Monthly Income($)", value=0)

    ## Co-Applicant Monthly Income
    co_mon_income = st.number_input("Co-Applicant's Monthly Income($)", value=0)

    ## Loan Amount
    loan_amt = st.number_input("Loan Amount", value=0)

    ## loan duration
    dur_display = ['2 Month','6 Month','8 Month','1 Year','16 Month']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration",dur_options, format_func=lambda x: dur_display[x])

    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480

if st.button("Submit"):
    # Extract feature values from widgets
    gen = int(gen)  # Assuming 'gen' is a number, change it to int or float if necessary
    mar = int(mar)  # Assuming 'mar' is a number
    dep = int(dep)  # Assuming 'dep' is a number
    edu = int(edu)  # Assuming 'edu' is a number
    emp = int(emp)  # Assuming 'emp' is a number
    duration = int(dur)  # Assuming 'dur' is a number

    # Format the features as a list of lists
    features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
    print(features)

    # Make sure to cast the features to float before predicting
    features = [[float(val) for val in feature] for feature in features]

    # Predict using the user's input
    prediction = model.predict(features)

    if prediction[0] == 0:
        st.error(
            "Account number: " + account_no + ' || ' +
            'According to our calculations, you will not get the loan from the bank'
        )
    else:
        st.success(
            "Account number: " + account_no + ' || ' +
            'Congratulations!! You will get the loan from the bank'
        )


run()
