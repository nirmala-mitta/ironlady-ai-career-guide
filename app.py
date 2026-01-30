import streamlit as st

st.title("Iron Lady AI Career Guide")
st.write("Helping women restart and grow their careers")

user_input = st.text_input("Ask your career question:")

if st.button("Send") and user_input:
    st.write(
        "AI: Based on your career gap, Iron Lady offers structured programs "
        "that help women restart their careers through mentorship, upskilling, "
        "and flexible learning paths. These programs are designed to rebuild "
        "confidence and support women in returning to the workforce."
    )
