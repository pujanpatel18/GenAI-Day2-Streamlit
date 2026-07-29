import streamlit as st

st.title("🎓 Student Registration Form")

# Input Fields
name = st.text_input("Enter Your Name")

email = st.text_input("Enter Your Email")

mobile = st.text_input("Enter Your Mobile Number")

dob = st.date_input("Select Your Date of Birth")

address = st.text_area("Enter Your Address")

photo = st.file_uploader(
    "Upload Profile Photo",
    type=["jpg", "jpeg", "png"]
)

age = st.slider("Select Your Age", 18, 30)

branch = st.selectbox(
    "Choose Branch",
    [
        "Computer Engineering",
        "Information Technology",
        "AI & ML",
        "Cyber Security"
    ]
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

# Submit Button
if st.button("Submit"):
    if not agree:
        st.error("❌ Please accept Terms & Conditions.")
    else:
        st.success("🎉 Registration Successful!")
        st.balloons()

        st.write("## Student Details")
        st.write("👤 Name:", name)
        st.write("📧 Email:", email)
        st.write("📱 Mobile:", mobile)
        st.write("🎂 Date of Birth:", dob)
        st.write("🏠 Address:", address)
        st.write("🎓 Branch:", branch)
        st.write("👨 Gender:", gender)
        st.write("🎂 Age:", age)
        st.write("🎯 Hobbies:", ", ".join(hobby))

        if photo is not None:
            st.image(photo, caption="Profile Photo", width=200)