import os
import sys

import streamlit as st

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from rag_logic.rag import process_rag

def chat_page():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "file_paths" not in st.session_state:
        st.session_state.file_paths = []

    messages = st.container()

    for message in st.session_state.messages:
        if message["role"] == "user":
            messages.chat_message("user").write(message["content"])
        elif message["role"] == "assistant":
            messages.chat_message("assistant").write(message["content"])

    st.sidebar.image(st.user["picture"], width=200)
    st.sidebar.write(st.user["name"])
    st.sidebar.markdown("<br>" * 20, unsafe_allow_html=True)

    if st.sidebar.button("Sign Out"):
        st.logout()

    chat_in = st.container()
    st.sidebar.markdown("<br>" * 20, unsafe_allow_html=True)

    if files := chat_in.file_uploader(
        "Upload files to chat with",
        type=["txt", "pdf", "docx", "json", "csv", "xlsx"],
        accept_multiple_files=True,
    ):
        dir_path = f"files/{st.user['name']}"
        for file in files:
            os.makedirs(dir_path, exist_ok=True)
            file_path = os.path.join(dir_path, file.name)
            with open(file_path, "wb") as f:
                f.write(file.getbuffer())
            st.session_state.file_paths.append(file_path)

    if prompt := chat_in.chat_input("Enter Prompt"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        response = process_rag(f"files/{st.user.name}", prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
