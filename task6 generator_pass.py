import streamlit as st
import random
import string
import time

def generate_password(length, use_upper, use_lower, use_numbers, use_symbols):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return "Select at least one character type!"
    
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    strength = "🔴 Weak"
    if len(password) >= 12 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password):
        strength = "🟢 Strong"
    elif len(password) >= 10:
        strength = "🟡 Moderate"
    return strength

# Streamlit UI
st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")

# Custom Background and Styling
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stTextInput, .stNumberInput, .stCheckbox, .stButton {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: #FFA500;'>✨ Secure Password Generator 🔐</h1>", unsafe_allow_html=True)

# User input
password_length = st.number_input("🔢 Enter password length:", min_value=8, max_value=100, value=12)
use_upper = st.checkbox("🔠 Include Uppercase Letters", value=True)
use_lower = st.checkbox("🔡 Include Lowercase Letters", value=True)
use_numbers = st.checkbox("🔢 Include Numbers", value=True)
use_symbols = st.checkbox("💲 Include Symbols", value=True)
num_passwords = st.number_input("🔄 How many passwords to generate?", min_value=1, max_value=10, value=1)

# Human verification
human_check = st.text_input("🤖 Are you a human? Type 'yes' to continue:", "")

if st.button("🚀 Generate Passwords"):
    if human_check.lower() == "yes":
        with st.spinner("🔄 Generating passwords..."):
            time.sleep(2)
        passwords = [generate_password(password_length, use_upper, use_lower, use_numbers, use_symbols) for _ in range(num_passwords)]
        
        st.markdown("### 🔑 Your Secure Passwords:")
        for pwd in passwords:
            strength = check_strength(pwd)
            color = "#28a745" if "Strong" in strength else "#ffc107" if "Moderate" in strength else "#dc3545"
            st.markdown(f"<p style='background-color:{color}; padding:10px; border-radius:5px; color:white;'><b>{pwd}</b> - {strength}</p>", unsafe_allow_html=True)
    else:
        st.error("❌ Please confirm you are a human by typing 'yes'!")
