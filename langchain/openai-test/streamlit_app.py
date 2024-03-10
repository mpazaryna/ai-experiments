import streamlit as st
from dotenv_setup import load_dotenv
from langchain_openai import OpenAI

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load environment variables at the start of the app
load_dotenv()


# Function to load prompt template from file
def load_prompt_template(file_path):
    with open(file_path, "r") as file:
        return file.read()


# Initialize components based on the refactored code
template_str = load_prompt_template("prompt_template.txt")
prompt = PromptTemplate.from_template(template_str)
llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
llm_chain = LLMChain(prompt=prompt, llm=llm)


def get_answer(question):
    """Given a question, return the AI's answer."""
    response = llm_chain.invoke(question)
    # Extract the answer text from the response
    answer_text = response.get("text", "Sorry, I couldn't process that question.")
    return answer_text


# Streamlit interface
st.title("AI Question Answering System")

# User input
user_question = st.text_input("Enter your question:", "")

if st.button("Get Answer"):
    if user_question:
        # Get the answer from the LLMChain
        answer = get_answer(user_question)
        st.write("Answer:", answer)
    else:
        st.error("Please enter a question.")
