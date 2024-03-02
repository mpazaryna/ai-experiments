from openai import OpenAI

client = OpenAI(api_key="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")
import streamlit as st

# Set your OpenAI API key here


st.title("AI Chat")

# Session state to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("You: ", "")

if st.button("Send") and user_input:
    # Append user input to chat history
    st.session_state.chat_history.append(f"You: {user_input}")

    # Generate the response using OpenAI's API
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",  # Choose an appropriate model
        prompt="\n".join(st.session_state.chat_history),
        temperature=0.7,
        max_tokens=150,
        stop=None,
        n=1,
    )

    # Extract text response
    text_response = response.choices[0].text.strip()
    st.session_state.chat_history.append(f"AI: {text_response}")

    # Display chat history
    st.text_area(
        "Chat",
        value="\n".join(st.session_state.chat_history),
        height=300,
        disabled=True,
    )

    # Clear input box after sending
    st.session_state["user_input"] = ""
