import streamlit as st
from chatbot import get_response

st.title("FAQ Chatbot")

user_input = st.text_input("You: ", "")

if user_input:
    response = get_response(user_input)
    st.text_area("Bot:", value=response, height=100)
