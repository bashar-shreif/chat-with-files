import streamlit as st
from chat_page import chat_page

st.title("Chat With Your Files")


if not st.user.is_logged_in:
    if st.button("Sign In With Google"):
        st.login()
else:
    chat_page()
