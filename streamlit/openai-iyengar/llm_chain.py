import streamlit as st
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


def load_prompt_template(file_path):
    with open(file_path, "r") as file:
        return file.read()


def initialize_llm_chain():
    prompt_template_str = load_prompt_template("prompt_template.txt")
    prompt = PromptTemplate(
        input_variables=["chat_history", "question"],
        template=prompt_template_str,
    )

    llm = ChatOpenAI(
        openai_api_key=st.secrets["OPENAI_API_KEY"],
        model=st.secrets["OPENAI_MODEL"],
    )

    memory = ConversationBufferWindowMemory(memory_key="chat_history", k=4)
    llm_chain = LLMChain(llm=llm, memory=memory, prompt=prompt)
    return llm_chain
