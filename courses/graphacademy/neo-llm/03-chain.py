import os

import dotenv
from langchain_openai import OpenAI

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Get the path and load the .env file
dotenv_path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_path)

llm = OpenAI()

template = PromptTemplate.from_template(
    """
You are a cockney fruit and vegetable seller.
Your role is to assist your customer with their fruit and vegetable needs.
Respond using cockney rhyming slang.

Tell me about the following fruit: {fruit}
"""
)

llm_chain = LLMChain(llm=llm, prompt=template)

response = llm_chain.invoke({"fruit": "apple"})

print(response)
