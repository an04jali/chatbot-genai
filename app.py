import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="DSA Instructor Bot", page_icon="🧠")

st.title("🧠 DSA Instructor Bot")
st.caption("Ask only Data Structures & Algorithms questions")

# Input box
user_input = st.text_input("Ask a DSA question:")

# Button click
if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                answer = get_response(user_input)
                st.success("Answer:")
                st.write(answer)
            except Exception as e:
                st.error("Something went wrong.")
                st.code(str(e))
