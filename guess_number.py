import streamlit as st
import random

# Initialize session state for storing the random number
if 'target_number' not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
if 'tries' not in st.session_state:
    st.session_state.tries = 0

# Set Page Configuration
st.set_page_config(page_title="Number Guessing Challenge", page_icon="🎲", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(120deg, #6a11cb, #2575fc);
            color: #fff;
        }
        .stApp {
            background: linear-gradient(120deg, #f5af19, #f12711);
            padding: 30px;
            border-radius: 20px;
        }
        .stTextInput, .stNumberInput {
            background: #f4f4f4 !important;
            border-radius: 12px;
            border: 2px solid #ddd;
        }
        .stButton>button {
            background: linear-gradient(120deg, #00c6ff, #0072ff);
            color: white;
            font-weight: bold;
            padding: 12px;
            border-radius: 12px;
            border: none;
        }
        .stButton>button:hover {
            background: linear-gradient(120deg, #00b4d8, #0096c7);
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Game Header
st.markdown("<h1 style='text-align: center; color: #fff;'>🎯 Number Guessing Challenge 🎲</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #3498db;'>I've picked a number between 1 and 100. Can you figure it out?</h4>", unsafe_allow_html=True)

# User input
user_input = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Check button
if st.button("Check Guess"):
    st.session_state.tries += 1
    if user_input < st.session_state.target_number:
        st.warning("❌ Too low! Try again. 🔽")
    elif user_input > st.session_state.target_number:
        st.warning("❌ Too high! Try again. 🔼")
    else:
        st.success(f"🎉 Well done! You guessed it in {st.session_state.tries} tries! 🎯")

# Reset button to restart the game
if st.button("🔄 Restart Challenge"):
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.tries = 0
    st.rerun()  # ✅ Updated from st.experimental_rerun()
