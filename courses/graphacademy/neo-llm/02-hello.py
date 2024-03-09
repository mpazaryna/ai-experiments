# Import necessary libraries
import os  # For interacting with the operating system

import dotenv  # For loading environment variables from .env files
from langchain_openai import OpenAI  # For accessing OpenAI's API

from langchain.prompts import PromptTemplate  # For creating prompt templates

# Load environment variables from the .env file
# First, find the .env file in the project directory
dotenv_path = dotenv.find_dotenv()
# Then, load the found .env file's variables into the environment
dotenv.load_dotenv(dotenv_path)

# Create a prompt template for the language model
# This template instructs the model to respond as a cockney fruit and vegetable seller
# using cockney rhyming slang, focused on a specific fruit provided by the user.
template = PromptTemplate(
    template="""
You are a cockney fruit and vegetable seller.
Your role is to assist your customer with their fruit and vegetable needs.
Respond using cockney rhyming slang.

Tell me about the following fruit: {fruit}
""",
    input_variables=["fruit"],  # Specify the variables used in the template
)

# Initialize the language model with specific parameters
# In this case, we're using the GPT-3.5 model with a "turbo" instruct variant at a fixed temperature
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)

# Use the language model to generate a response
# Here, we're formatting the template with a specific fruit ("apple") and invoking the model
response = llm.invoke(template.format(fruit="apple"))

# Print the generated response
print(response)
