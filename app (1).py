import streamlit as st
import random

st.set_page_config(page_title="Random Quote Generator", page_icon="💡")

st.title("💡 Random Quote Generator")

quotes = [
    "The best way to predict the future is to create it. – Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
    "Do what you can with all you have, wherever you are. – Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. – William James",
    "Happiness is not something ready made. It comes from your own actions. – Dalai Lama",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs",
    "The harder you work for something, the greater you’ll feel when you achieve it."
]

if st.button("✨ Get Random Quote"):
    quote = random.choice(quotes)
    st.success(quote)
else:
    st.info("Click the button to generate a random quote!")
