import streamlit as st

st.title("📊 Percentage & Grade Calculator")

marks = st.number_input("Enter Obtained Marks")
total = st.number_input("Enter Total Marks")

if st.button("Calculate"):
    if total > 0:
        percentage = (marks / total) * 100

        # 🎓 Grade system
        if percentage >= 80:
            grade = "A+"
            remark = "Excellent! 🎉"
        elif percentage >= 70:
            grade = "A"
            remark = "Great job! 👍"
        elif percentage >= 60:
            grade = "B"
            remark = "Good effort! 😊"
        elif percentage >= 50:
            grade = "C"
            remark = "Needs improvement. 📘"
        elif percentage >= 40:
            grade = "D"
            remark = "Try harder next time. 💪"
        else:
            grade = "Fail"
            remark = "Don't give up! Good luck for next time 🌱"

        # ✅ Show result with bold formatting
        st.markdown(f"""
        ✅ **Percentage:** `{percentage:.2f}%`  
        🏷️ **Grade:** **{grade}**  
        💬 **Remarks:** *{remark}*
        """)
    else:
        st.error("Total marks must be greater than 0.")



