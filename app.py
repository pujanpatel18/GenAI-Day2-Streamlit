import streamlit as st

st.title("Student Registration Form")

name = st.text_input("Enter Your Name")

age = st.slider("Select Your Age", 18, 30)

branch = st.selectbox(
    "Choose Branch",
    ["Computer Engineering", "Information Technology", "AI & ML", "Cyber Security"]
)

gender = st.radio(
    "Gender",
    ["Male", "Female", "Other"]
)

hobby = st.multiselect(
    "Select Your Hobbies",
    ["Coding", "Gaming", "Reading", "Cricket", "Music"]
)

agree = st.checkbox("I Accept Terms & Conditions")

if st.button("Submit"):
    st.success("Registration Successful ✅")

    st.write("### Student Details")
    st.write("Name :", name)
    st.write("Age :", age)
    st.write("Branch :", branch)
    st.write("Gender :", gender)
    st.write("Hobbies :", hobby)