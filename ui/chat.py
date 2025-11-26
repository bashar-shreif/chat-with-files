import os

import streamlit as st

SAVE_DIR = "files"
os.makedirs(SAVE_DIR, exist_ok=True)

st.markdown(
    "<h1 style='text-align: center;'>Chat With Your Documents!</h1>",
    unsafe_allow_html=True,
)

uploaded_files = st.file_uploader(
    "Upload your documents",
    type=["pdf", "txt", "docx", "csv", "xlsx"],
    accept_multiple_files=True,
)

saved_paths = []
if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = os.path.join(SAVE_DIR, uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        saved_paths.append(file_path)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type prompt")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append(
        {"role": "assistant", "content": f"You said: {prompt}"}
    )
    st.rerun()

