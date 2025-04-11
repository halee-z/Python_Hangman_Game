import streamlit as st
import random

# Word list
words = ["python", "streamlit", "hangman", "developer", "challenge"]

# Initialize session state
if 'word' not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.guessed = []
    st.session_state.tries = 6

# Title
st.title("🎯 Hangman Game")

# Display word with blanks
display_word = " ".join([letter if letter in st.session_state.guessed else "_" for letter in st.session_state.word])
st.write(f"## Word: {display_word}")

# User input
guess = st.text_input("Enter a letter:", max_chars=1)

# Guess handling
if guess:
    guess = guess.lower()
    if guess in st.session_state.word and guess not in st.session_state.guessed:
        st.session_state.guessed.append(guess)
        st.success(f"Correct! '{guess}' is in the word.")
    elif guess not in st.session_state.word and guess not in st.session_state.guessed:
        st.session_state.guessed.append(guess)
        st.session_state.tries -= 1
        st.error(f"Wrong guess! '{guess}' is not in the word. Tries left: {st.session_state.tries}")
    else:
        st.info("You already guessed that letter.")

# Game status
if all(letter in st.session_state.guessed for letter in st.session_state.word):
    st.balloons()
    st.success("Congratulations! You've guessed the word!")
    if st.button("Play Again"):
        st.session_state.clear()
elif st.session_state.tries == 0:
    st.error(f"Game Over! The word was '{st.session_state.word}'.")
    if st.button("Try Again"):
        st.session_state.clear()
