import streamlit as st
import datetime

st.set_page_config(page_title="Student Registration Form", page_icon="🎓")

st.title("🎓 Student Registration Form")

# Today's Date
today = datetime.date.today()

# Input Fields
name = st.text_input("👤 Enter Your Name")

email = st.text_input("📧 Enter Your Email")

mobile = st.text_input("📱 Enter Your Mobile Number")

dob = st.date_input(
    "🎂 Select Your Date of Birth",
    value=today.replace(year=today.year - 18),
    min_value=today.replace(year=today.year - 60),
    max_value=today
)

address = st.text_area("🏠 Enter Your Address")

photo = st.file_uploader(
    "📷 Upload Profile Photo",
    type=["jpg", "jpeg", "png"]
)

age = st.slider("🎂 Select Your Age", 1, 60)

branch = st.selectbox(
    "🎓 Choose Branch",
    [
        "Computer Engineering",
        "Information Technology",
        "AI & ML",
        "Cyber Security"
    ]
)

gender = st.radio(
    "👨 Gender",
    ["Male", "Female", "Other"]
)

hobby = st.multiselect(
    "🎯 Select Your Hobbies",
    [
        "Coding",
        "Gaming",
        "Reading",
        "Cricket",
        "Music"
    ]
)

agree = st.checkbox("✅ I Accept Terms & Conditions")

# Submit Button
if st.button("Submit"):

    if not agree:
        st.error("❌ Please accept Terms & Conditions.")

    elif name == "":
        st.warning("Please enter your name.")

    elif email == "":
        st.warning("Please enter your email.")

    elif mobile == "":
        st.warning("Please enter your mobile number.")

    else:
        st.success("🎉 Registration Successful!")
        st.balloons()

        st.subheader("📋 Student Details")

        st.write("👤 Name:", name)
        st.write("📧 Email:", email)
        st.write("📱 Mobile:", mobile)
        st.write("🎂 Date of Birth:", dob)
        st.write("🎂 Age:", age)
        st.write("🏠 Address:", address)
        st.write("🎓 Branch:", branch)
        st.write("👨 Gender:", gender)
        st.write("🎯 Hobbies:", ", ".join(hobby))

        if photo is not None:
            st.image(photo, caption="Profile Photo", width=200)