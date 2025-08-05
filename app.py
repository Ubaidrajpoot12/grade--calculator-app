import streamlit as st

st.title("📊 Percentage & Grade Calculator")

marks = st.number_input("Enter Obtained Marks")
total = st.number_input("Enter Total Marks")

if st.button("Calculate"):
    if total > 0:
        percentage = (marks / total) * 100

        # 🎓 Grade & Color system
        if percentage >= 80:
            grade = "A+"
            remark = "Excellent! 🎉"
            color = "green"
        elif percentage >= 70:
            grade = "A"
            remark = "Great job! 👍"
            color = "limegreen"
        elif percentage >= 60:
            grade = "B"
            remark = "Good effort! 😊"
            color = "orange"
        elif percentage >= 50:
            grade = "C"
            remark = "Needs improvement. 📘"
            color = "darkorange"
        elif percentage >= 40:
            grade = "D"
            remark = "Try harder next time. 💪"
            color = "orangered"
        else:
            grade = "Fail"
            remark = "Don't give up! Good luck for next time 🌱"
            color = "red"

        # ✅ Display results with colored grade
        st.markdown(f"""
        <div style='font-size: 18px;'>
            ✅ <b>Percentage:</b> {percentage:.2f}%<br>
            🏷️ <b>Grade:</b> <span style='color:{color}; font-weight: bold;'>{grade}</span><br>
            💬 <b>Remarks:</b> <i>{remark}</i>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Total marks must be greater than 0.")



