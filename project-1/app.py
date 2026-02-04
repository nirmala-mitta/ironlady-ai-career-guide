import streamlit as st

# Page title
st.title("Iron Lady AI Career Guide")
st.write("Helping women restart and grow their careers")

# User input
user_input = st.text_input("Ask your career question:")

# Button click
if st.button("Send") and user_input:

    question = user_input.lower()

    # Simple AI-like logic based on question
    if "career gap" in question:
        answer = (
            "Iron Lady offers career restart programs specially designed for women with career gaps. "
            "These programs include mentorship, confidence-building sessions, and structured upskilling "
            "to help women re-enter the workforce successfully."
        )

    elif "technology" in question or "it" in question:
        answer = (
            "Iron Lady provides technology-focused upskilling programs in areas like IT, digital skills, "
            "and emerging technologies. These programs help women transition or grow into tech roles."
        )

    elif "confidence" in question or "interview" in question:
        answer = (
            "Iron Lady supports women through confidence-building workshops, mock interviews, and career "
            "guidance sessions to prepare them for job interviews and professional growth."
        )

    elif "program" in question or "courses" in question:
        answer = (
            "Iron Lady offers structured career programs that include mentorship, flexible learning paths, "
            "hands-on training, and continuous support tailored to women professionals."
        )

    else:
        answer = (
            "Iron Lady helps women restart and grow their careers through personalized guidance, "
            "skill development, and supportive mentoring programs. You can ask about career gaps, "
            "upskilling, or confidence-building support."
        )

    # Display answer
    st.write("AI:", answer)
