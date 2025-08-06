import streamlit as st

# 🌓 Dark Mode Toggle
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# Apply Dark or Light Mode Styles
# Check for theme toggle before anything else
if st.session_state.get("theme_toggle", False):
    st.session_state.dark_mode = not st.session_state.dark_mode
    st.session_state.theme_toggle = False
    st.experimental_rerun()

# ⋮ More Options Menu
with st.expander("⋮ More Options", expanded=False):
    selected_option = st.radio("Choose an Option", [
        "None",
        "Toggle Dark Mode",
        "Reset Form",
        "About App"
    ])

    if selected_option == "Toggle Dark Mode":
        st.session_state.theme_toggle = True

    elif selected_option == "Reset Form":
        st.experimental_rerun()

    elif selected_option == "About App":
        st.info("""
        🎓 **Grade Calculator Dashboard**
        Version: 1.0  
        Developed by: [Your Name or Link]  
        Powered by Streamlit
        """)

    """
else:
    page_bg = """
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #e0f7fa, #fff);
        padding: 2rem;
    }
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }
    .main-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        max-width: 500px;
        margin: auto;
        font-family: 'Segoe UI', sans-serif;
    }
    </style>
    """

st.markdown(page_bg, unsafe_allow_html=True)

# ⋮ More Options Menu
with st.expander("⋮ More Options", expanded=False):
    selected_option = st.radio("Choose an Option", [
        "None",
        "Toggle Dark Mode",
        "Reset Form",
        "About App"
    ])

    if selected_option == "Toggle Dark Mode":
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.experimental_rerun()
    elif selected_option == "Reset Form":
        st.experimental_rerun()
    elif selected_option == "About App":
        st.info("""
        🎓 **Grade Calculator Dashboard**
        Version: 1.0  
        Developed by: [Your Name or Link]  
        Powered by Streamlit
        """)

st.markdown("""<div class='main-card'>""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>📊 Grade Calculator Dashboard</h2>", unsafe_allow_html=True)

# 🧑 Optional Username Input
username = st.text_input("Enter Your Name (optional)")

# 📝 Input Section
marks = st.number_input("Enter Obtained Marks", min_value=0.0, format="%.2f")
total = st.number_input("Enter Total Marks", min_value=1.0, format="%.2f")

if st.button("Calculate Grade"):
    percentage = (marks / total) * 100

    # 🎓 Grade & Remarks
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

