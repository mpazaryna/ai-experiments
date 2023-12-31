import os

import dotenv
import openai

import streamlit as st

# Get the path to the .env file
dotenv_path = dotenv.find_dotenv()

# Load the .env file
dotenv.load_dotenv(dotenv_path)

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

system_prompt = "You are an excellent assistant AI. Please answer any questions."

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": system_prompt}]


# OpenAI API
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""


st.title("Assistant AI Bot")
st.write("🤖 Hello! Feel free to ask me anything.")
st.sidebar.markdown("## AUTOMATION ARCHITECH AGENCY")
st.sidebar.markdown(
    "We are Experienced Architech-nicians When it comes to helping take your project to the next level with automation and data, we’re here to help! We have 10+ years of collective experience in automating and integrating technology across a range of industries."
)

user_input = st.text_input(
    "Please write your message.", key="user_input", on_change=communicate
)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        speaker = "🙂"
        if message["role"] == "assistant":
            speaker = "🤖"

        st.write(speaker + ": " + message["content"])
