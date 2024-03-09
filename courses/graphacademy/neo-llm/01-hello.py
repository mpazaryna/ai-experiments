import os

import dotenv

# Get the path and load the .env file
dotenv_path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_path)

from langchain_openai import OpenAI

llm = OpenAI()
response = llm.invoke("What is Neo4j?")
print(response)
