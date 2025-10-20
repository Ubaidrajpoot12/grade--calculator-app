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

    # 🧾 Result Display
    user_display = f"<b>{username}</b>, your " if username else "Your "

    st.markdown(f"""
    <div style='text-align: center; padding-top: 1rem;'>
        <h4>🎯 {user_display}percentage is: {percentage:.2f}%</h4>
        <h4>🏷️ Grade: <span style='color: {color};'><b>{grade}</b></span></h4>
        <h4>💬 Remarks: <i>{remark}</i></h4>
    </div>
    """, unsafe_allow_html=True)

    # 🟢 Circular Percentage Meter
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=percentage,
        number={'suffix': "%", 'font': {'size': 36}},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': color},
            'bgcolor': "#e0e0e0",
            'borderwidth': 2,
            'bordercolor': "#888",
            'steps': [
                {'range': [0, 40], 'color': '#ffcdd2'},
                {'range': [40, 60], 'color': '#fff59d'},
                {'range': [60, 80], 'color': '#c8e6c9'},
                {'range': [80, 100], 'color': '#a5d6a7'}
            ],
        },
        title={'text': "Performance", 'font': {'size': 20}}
    ))

    fig.update_layout(height=300, margin=dict(t=30, b=0, l=0, r=0))
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
