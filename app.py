import streamlit as st

st.title("📊 Percentage & Grade Calculator")

marks = st.number_input("Enter Obtained Marks")
total = st.number_input("Enter Total Marks")

if st.button("Calculate"):
    if total > 0:
        percentage = (marks / total) * 100

        if percentage >= 80:
            grade = "A+"
        elif percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "'Fail'best of luck for next time"

        st.success(f"🎯 Percentage: {percentage:.2f}%\n📘 Grade: {grade}")
    else:
        st.error("❌ Total marks must be greater than 0.")
