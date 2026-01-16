import streamlit as st
from chatbot import get_response

st.set_page_config(
    page_title="DSA Instructor Bot",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 DSA Instructor Bot")
st.caption("Ask only Data Structures & Algorithms questions")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Ask a DSA question...")

if user_input:
    # User message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    with st.spinner("Thinking... 🤔"):
        reply = get_response(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
    with st.chat_message("assistant"):
        st.markdown(reply)

# Sidebar
with st.sidebar:
    st.header("⚙️ Controls")
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
