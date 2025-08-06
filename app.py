import streamlit as st

st.set_page_config(page_title="Grade Calculator", layout="centered")

# ⋮ More Options Menu
with st.expander("⋮ More Options", expanded=False):
    selected_option = st.radio("Choose an Option", [
        "None"
        "About App"
    ])

    if selected_option == "Reset Form":
        st.experimental_rerun()
    elif selected_option == "About App":
        st.info("""
        🎓 **Result Calculator Dashboard**
        Version: 1.5  
        Developed by: [Ubaid-ur-Rehman]  
        Powered by Streamlit
        """)

st.markdown("""
    <style>
    .main-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        max-width: 100%;
        margin: auto;
        font-family: 'Segoe UI', sans-serif;
    }
    @media (max-width: 600px) {
        .main-card {
            padding: 15px;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""<div class='main-card'>""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>📊 Result Calculator Dashboard</h2>", unsafe_allow_html=True)

# 🧑 Optional Username Input
username = st.text_input("Enter Your Name (optional)")

# 📝 Input Section
marks = st.number_input("Enter Obtained Marks", min_value=0.0, format="%.2f")
total = st.number_input("Enter Total Marks", min_value=1.0, format="%.2f")

if st.button("Calculate Result"):
    percentage = (marks / total) * 100

    # 🎓 Grade & Remarks
    if percentage>=90
        grade= "A+"
        remark= "Out standing"
    if percentage >= 80:
        grade = "A+"
        remark = "Excellent! 🎉"
        color = "#2e7d32"  # green
    elif percentage >= 70:
        grade = "A"
        remark = "Great job! 👍"
        color = "#388e3c"
    elif percentage >= 60:
        grade = "B"
        remark = "Good effort! 😊"
        color = "#fbc02d"
    elif percentage >= 50:
        grade = "C"
        remark = "Needs improvement. 📘"
        color = "#ffa000"
    elif percentage >= 40:
        grade = "D"
        remark = "Try harder next time. 💪"
        color = "#f57c00"
    else:
        grade = "Fail"
        remark = "Don't give up! Good luck for next time 🌱"
        color = "#d32f2f"  # red

    # ✅ Output Section
    user_display = f"<b>{username}</b>, your " if username else "Your "

    st.markdown(f"""
    <div style='text-align: center; padding-top: 1rem;'>
        <h4>🎯 {user_display}percentage is: {percentage:.2f}%</h4>
        <h4>🏷️ Grade: <span style='color: {color};'><b>{grade}</b></span></h4>
        <h4>💬 Remarks: <i>{remark}</i></h4>
    </div>
    """, unsafe_allow_html=True)

    # 📄 Downloadable Report
    report = f"Name: {username if username else 'N/A'}\nMarks Obtained: {marks}\nTotal Marks: {total}\nPercentage: {percentage:.2f}%\nGrade: {grade}\nRemarks: {remark}"

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="grade_report.txt",
        mime="text/plain"
    )

st.markdown("""</div>""", unsafe_allow_html=True)




