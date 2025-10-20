import streamlit as st
import plotly.graph_objects as go

# 🏷️ Page Config
st.set_page_config(page_title="Grade Calculator", layout="centered")

# ⋮ More Options Menu
with st.expander("⋮ More Options", expanded=False):
    selected_option = st.radio("Choose an Option", [
        "About App",
        "Help",
        "Feedback",
    ])

    if selected_option == "About App":
        st.markdown("""
        🎓 **Result Calculator Dashboard**  
        **Version:** 1.6  
        **Released On:** 5 Aug 2025  
        **Developed by:** Ubaid-ur-Rehman  
        **Powered by:** Streamlit
        """)

    elif selected_option == "Help":
        st.markdown("""
        🆘 **Help Guide**  
        - Enter your obtained and total marks.  
        - Click **Calculate Result** to view your grade.  
        - Optionally, enter your name for a personalized report.  
        - Use **Download Report** to save your result.  
        - Access more options from the **⋮ Menu**.
        """)

    elif selected_option == "Feedback":
        st.markdown("""
        💬 **We Value Your Feedback!**  
        Found a bug or suggestion? Contact:  
        📧 **abdul.rehman6098@email.com**  
        🐱 GitHub: [github.com/Ubaidrajpoot12](https://github.com/Ubaidrajpoot12)
        """)

# 💠 CSS Styling
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

st.markdown("<div class='main-card'>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>📊 Result Calculator Dashboard</h2>", unsafe_allow_html=True)

# 🧑 Name Input
username = st.text_input("Enter Your Name (optional)")

# 🧮 Input Fields
marks = st.number_input("Enter Obtained Marks", min_value=0.0)
total = st.number_input("Enter Total Marks", min_value=1.0)

if st.button("Calculate Result"):
    percentage = (marks / total) * 100

    # 🎓 Grade System
    if percentage >= 90:
        grade = "A+"
        remark = "Outstanding! 🌟"
        color = "#2e7d32"
    elif percentage >= 80:
        grade = "A"
        remark = "Excellent! 🎉"
        color = "#43a047"
    elif percentage >= 70:
        grade = "B"
        remark = "Great job! 👍"
        color = "#fbc02d"
    elif percentage >= 60:
        grade = "C"
        remark = "Good effort! 😊"
        color = "#ffa000"
    elif percentage >= 50:
        grade = "D"
        remark = "Needs improvement. 📘"
        color = "#f57c00"
    else:
        grade = "Fail"
        remark = "Don't give up! Try again 🌱"
        color = "#d32f2f"

import plotly.graph_objects as go

# 🧾 Result Display
user_display = f"<b>{username}</b>, your " if username else "Your "

st.markdown(f"""
<div style='text-align: center; padding-top: 1rem;'>
    <h4>🎯 {user_display}percentage is: {percentage:.2f}%</h4>
    <h4>🏷️ Grade: <span style='color: {color};'><b>{grade}</b></span></h4>
    <h4>💬 Remarks: <i>{remark}</i></h4>
</div>
""", unsafe_allow_html=True)

# 🔵 Modern Circular Gauge
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=percentage,
    title={'text': "Your Percentage", 'font': {'size': 22}},
    number={'suffix': "%", 'font': {'size': 26, 'color': "#004aad"}},
    gauge={
        'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "gray"},
        'bar': {'color': "#00c9a7"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "#ddd",
        'steps': [
            {'range': [0, 50], 'color': '#ffe5e5'},
            {'range': [50, 70], 'color': '#fff7cc'},
            {'range': [70, 85], 'color': '#d4f8d4'},
            {'range': [85, 100], 'color': '#a1f0dc'},
        ],
        'threshold': {
            'line': {'color': "#004aad", 'width': 6},
            'thickness': 0.8,
            'value': percentage
        }
    }
))

fig.update_layout(
    height=350,
    margin=dict(l=30, r=30, t=50, b=0),
    paper_bgcolor="rgba(0,0,0,0)",
    font={'color': "#004aad", 'family': "Segoe UI"},
)

st.plotly_chart(fig, use_container_width=True)


    # 📄 Downloadable Report
    report = f"""
Name: {username if username else 'N/A'}
Marks Obtained: {marks}
Total Marks: {total}
Percentage: {percentage:.2f}%
Grade: {grade}
Remarks: {remark}
    """

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="grade_report.txt",
        mime="text/plain"
    )

st.markdown("</div>", unsafe_allow_html=True)

