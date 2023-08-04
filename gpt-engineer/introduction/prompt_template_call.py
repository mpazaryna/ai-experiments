# prompt_template_call.py
from langchain import PromptTemplate

# --------------------------------------------------------------
# Prompt Templates: Manage prompts for LLMs
# --------------------------------------------------------------


def run_prompt_template_demo():
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )
    return prompt.format(product="Smart Apps using Large Language Models (LLMs)")
