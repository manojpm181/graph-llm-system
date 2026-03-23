import streamlit as st

def chat_box():
    col1, col2 = st.columns([4, 1])

    with col1:
        user_input = st.text_input("Ask about orders, customers, products...", label_visibility="collapsed")

    with col2:
        ask_clicked = st.button("🚀")

    if ask_clicked and user_input:
        return user_input

    return None


def stream_text(text):
    import time
    placeholder = st.empty()
    output = ""

    for char in text:
        output += char
        placeholder.markdown(output)
        time.sleep(0.01)