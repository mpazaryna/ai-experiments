import os

import dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

# Get the path to the .env file
dotenv_path = dotenv.find_dotenv()

# Load the .env file
dotenv.load_dotenv(dotenv_path)

template = """Question: {question}
Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)

llm = OpenAI()
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "What NFL team won the Super Bowl in the year Shakira was born?"

r = llm_chain.invoke(question)
print(r)
