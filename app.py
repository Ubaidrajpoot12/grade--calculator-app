import streamlit as st

# 🎨 Custom background and styles
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1584697964403-a83aa8f5e7f3");
    background-size: cover;
    background-position: center;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("📊 Percentage & Grade Calculator")

# 📝 Form input
with st.form("grade_form"):
    marks = st.number_input("Enter Obtained Marks", min_value=0.0)
    total = st.number_input("Enter Total Marks", min_value=1.0)
    submitted = st.form_submit_button("Calculate")

if submitted:
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
        remark = "Don't give up! good luck for next time🌱"

    st.success(f"🎯 Percentage: {percentage:.2f}%\n📘 Grade: {grade}\n💬 Remark: {remark}")

    # 📄 Prepare report text
    report_text = f"""
Marks Obtained: {marks}
Total Marks: {total}
Percentage: {percentage:.2f}%
Grade: {grade}
Remarks: {remark}
"""

    # 📥 Download button
    st.download_button(
        label="📄 Download Report",
        data=report_text,
        file_name="grade_report.txt",
        mime="text/plain"
    )


