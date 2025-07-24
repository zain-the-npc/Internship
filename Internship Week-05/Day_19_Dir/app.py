import streamlit as st
from encryptor import encrypt_message, decrypt_message
import pyperclip

st.set_page_config(page_title="VaultCode", page_icon="🔐", layout="centered")
st.title(" VaultCode – Web Encryption Tool")

st.markdown("""<style>
textarea, input[type='text'], input[type='password'] {
    border-radius: 0.5rem;
    font-size: 16px;
}
.stButton>button {
    width: 100%;
    margin-top: 10px;
    background-color: #1f6feb;
    color: white;
    font-weight: 500;
}
</style>""", unsafe_allow_html=True)

st.subheader("Message:")
message = st.text_area("", height=100, key="message_box")

st.subheader("Password:")
password = st.text_input("", type="password", key="password_box")

st.subheader("Mode:")
mode = st.radio("Choose an action:", ["Encrypt", "Decrypt"], horizontal=True)

result = ""
if st.button("Submit"):
    if not message.strip() or not password.strip():
        st.warning("Please enter both the message/code and password.")
    else:
        if mode == "Encrypt":
            result = encrypt_message(message, password)
        else:
            result = decrypt_message(message, password)

        st.success("Output:")
        st.code(result, language="")

        if st.button(" Copy to clipboard"):
            try:
                pyperclip.copy(result)
                st.toast("Copied to clipboard ")
            except Exception:
                st.info("Copy failed. Clipboard support may be limited on web.")

st.markdown("""---
🔒 VaultCode | Powered by Streamlit & Cryptography
""")
