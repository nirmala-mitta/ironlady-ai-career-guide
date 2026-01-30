import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyDvhzS9Zq0In765jqJTc2t1sEbC-LMBG7Q")

st.title("Iron Lady AI Career Guide")
st.write("Helping women restart and grow their careers")

model = genai.GenerativeModel(
    model_name="gemini-pro",
    system_instruction="""
You are an empathetic AI Career Guide for Iron Lady.
Iron Lady helps women restart careers, upskill, and gain confidence.
Explain programs simply and motivate women learners.
"""
)

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

user_input = st.text_input("Ask your career question:")

if st.button("Send") and user_input:
    response = st.session_state.chat.send_message(user_input)
    st.write("AI:", response.text)
