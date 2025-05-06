import streamlit as st
import requests

st.title("Feedback Form")

name = st.text_input("Name")
email = st.text_input("Email")
feedback = st.text_area("Your Feedback")

if st.button("Submit"):
    if name and email and feedback:
        data = {
            "name": name,
            "email": email,
            "feedback": feedback
        }
        response = requests.post("http://localhost:5000/submit", json=data)
        if response.status_code == 200:
            st.success("Thank you! Feedback submitted.")
        else:
            st.error("Something went wrong.")
    else:
        st.warning("Please fill all fields.")
