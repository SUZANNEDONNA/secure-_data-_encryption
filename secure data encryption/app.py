import streamlit as st
from cryptography.fernet import Fernet

st.set_page_config(page_title="Secure Data Encryption", page_icon="🔐")

st.title("🔐 Secure Data Encryption System")

# Function to generate a new key
def generate_key():
    return Fernet.generate_key()

# UI: Text input
data = st.text_area("Enter text to encrypt/decrypt")

# Key input
key_input = st.text_input("Enter your encryption key (leave blank to auto-generate)", type="password")

# Generate or use user-provided key
if key_input:
    try:
        key = key_input.encode()
        fernet = Fernet(key)
    except Exception as e:
        st.error("Invalid key! Make sure it's a valid Fernet key.")
        st.stop()
else:
    key = generate_key()
    fernet = Fernet(key)
    st.info(f"Generated key: `{key.decode()}` — save it to decrypt later!")

# Encrypt button
if st.button("Encrypt"):
    if data:
        encrypted = fernet.encrypt(data.encode())
        st.success("🔒 Encrypted Data:")
        st.code(encrypted.decode(), language="text")
    else:
        st.warning("Please enter some text to encrypt.")

# Decrypt button
if st.button("Decrypt"):
    if data:
        try:
            decrypted = fernet.decrypt(data.encode()).decode()
            st.success("🔓 Decrypted Data:")
            st.code(decrypted, language="text")
        except Exception:
            st.error("Failed to decrypt! Check if the key and encrypted data are correct.")
    else:
        st.warning("Please enter some encrypted text to decrypt.")

