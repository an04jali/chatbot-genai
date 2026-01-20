import os, streamlit as st
st.write("API key loaded:", bool(os.getenv("GROQ_API_KEY")))

import streamlit as st
from chatbot import get_response

# Page config
st.set_page_config(
    page_title="DSA Instructor Bot",
    page_icon="🧠",
    layout="centered"
)

# Title and header
st.title("🧠 DSA Instructor Bot")
st.caption("Ask only Data Structures & Algorithms questions")

# Clear chat button
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("🗑️ Clear"):
        st.session_state.messages = []
        st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat-style input
user_input = st.chat_input("Ask a DSA question...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer = get_response(user_input)
                st.markdown(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )
            except Exception as e:
                error_msg = "❌ Something went wrong. Please try again."
                st.error(error_msg)
                st.code(str(e), language="text")
                st.session_state.messages.append(
                    {"role": "assistant", "content": error_msg}
                )