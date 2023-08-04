# main.py
from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI

# Load environment variables
load_dotenv(find_dotenv())

from agent_call import run_agent_demo
from chain_call import run_chain_demo
from conversation_call import run_conversation_demo

# Import the functions from the separate files
from llm_call import run_llm_demo
from prompt_template_call import run_prompt_template_demo

if __name__ == "__main__":
    # Call each function
    print("LLMs Demo:")
    print(run_llm_demo())
    print("Prompt Template Demo:")
    print(run_prompt_template_demo())
    print("Chain Demo:")
    print(run_chain_demo())
    print("Agent Demo:")
    print(run_agent_demo())
    print("Conversation Demo:")
    output1, output2 = run_conversation_demo()
    print(output1)
    print(output2)
