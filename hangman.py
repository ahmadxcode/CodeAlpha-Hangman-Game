import streamlit as st
import random

# -------------------------------
# 🎮 Game Setup
# -------------------------------
WORDS = ["python", "streamlit", "developer", "data", "machine", "learning", "codealpha", "internship"]

if "word" not in st.session_state:
    st.session_state.word = random.choice(WORDS)
    st.session_state.guessed = ["_"] * len(st.session_state.word)
    st.session_state.attempts = 6
    st.session_state.guessed_letters = []
    st.session_state.message = ""

# -------------------------------
# 🌈 Page Config & CSS Styling
# -------------------------------
st.set_page_config(page_title="Hangman Game | CodeAlpha", page_icon="🎮", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #141E30, #243B55);
        color: white;
    }

    h1 {
        text-align: center;
        color: #00FFF0;
        text-shadow: 0 0 15px #00FFF0;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .caption {
        text-align: center;
        color: #aaa;
        font-size: 14px;
        margin-bottom: 25px;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 25px 30px;
        box-shadow: 0 0 25px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }

    .word-display {
        font-size: 34px;
        letter-spacing: 6px;
        text-align: center;
        color: #00ffcc;
        text-shadow: 0 0 12px #00ffcc;
        font-weight: 600;
        margin-bottom: 15px;
    }

    .attempts {
        text-align: center;
        font-size: 18px;
        color: #FFD700;
        margin-bottom: 5px;
    }

    .letters {
        text-align: center;
        color: #ccc;
        font-size: 15px;
        margin-bottom: 20px;
    }

    .feedback {
        text-align: center;
        font-size: 18px;
        margin: 10px 0;
    }

    .correct { color: #00FF99; text-shadow: 0 0 10px #00FF99; }
    .wrong { color: #FF5C5C; text-shadow: 0 0 10px #FF5C5C; }
    .warning { color: #FFD700; text-shadow: 0 0 10px #FFD700; }

    .footer {
        text-align: center;
        color: #bbb;
        font-size: 13px;
        margin-top: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# 🎨 Layout
# -------------------------------
st.markdown("<h1>🎯 Hangman Game — Code alpha</h1>", unsafe_allow_html=True)
st.markdown('<p class="caption">Developed by <b>AhmadXCode</b> | CodeAlpha Internship Task 1</p>', unsafe_allow_html=True)

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

word_display = " ".join(st.session_state.guessed)
st.markdown(f'<div class="word-display">{word_display}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="attempts">💀 Attempts Left: {st.session_state.attempts}</div>', unsafe_allow_html=True)

if st.session_state.guessed_letters:
    st.markdown(f'<div class="letters">🔠 Guessed Letters: {", ".join(st.session_state.guessed_letters)}</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="letters">🔠 No letters guessed yet.</div>', unsafe_allow_html=True)

# -------------------------------
# ✏️ Input Form
# -------------------------------
with st.form("guess_form"):
    guess = st.text_input("Enter a letter:", max_chars=1, key="guess_input").lower()
    submitted = st.form_submit_button("Submit Guess")

# -------------------------------
# 🧠 Logic
# -------------------------------
if submitted:
    if not guess.isalpha():
        st.session_state.message = '<p class="feedback warning">⚠️ Please enter a valid letter.</p>'
    elif guess in st.session_state.guessed_letters:
        st.session_state.message = f'<p class="feedback warning">⚠️ You already guessed "{guess.upper()}"!</p>'
    else:
        st.session_state.guessed_letters.append(guess)
        if guess in st.session_state.word:
            for i, letter in enumerate(st.session_state.word):
                if letter == guess:
                    st.session_state.guessed[i] = guess
            st.session_state.message = f'<p class="feedback correct">✅ Correct guess: "{guess.upper()}"!</p>'
        else:
            st.session_state.attempts -= 1
            st.session_state.message = f'<p class="feedback wrong">❌ Wrong guess: "{guess.upper()}"!</p>'

# -------------------------------
# 🎉 Status + Restart Logic
# -------------------------------
if "_" not in st.session_state.guessed:
    st.success(f"🎉 You won! The word was: {st.session_state.word.upper()}")
elif st.session_state.attempts <= 0:
    st.error(f"💀 Game Over! The word was: {st.session_state.word.upper()}")

# Display feedback message
st.markdown(st.session_state.message, unsafe_allow_html=True)

if st.button("🔁 Restart Game"):
    st.session_state.word = random.choice(WORDS)
    st.session_state.guessed = ["_"] * len(st.session_state.word)
    st.session_state.attempts = 6
    st.session_state.guessed_letters = []
    st.session_state.message = ""
    st.rerun()

st.markdown('<p class="footer">© 2025 AhmadXCode | CodeAlpha Internship Project - Task 1</p>', unsafe_allow_html=True)
