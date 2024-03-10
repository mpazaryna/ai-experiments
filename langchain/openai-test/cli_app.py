from dotenv_setup import load_dotenv
from langchain_openai import OpenAI

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


# Function to load prompt template from file
def load_prompt_template(file_path):
    with open(file_path, "r") as file:
        return file.read()


def main():
    # Load environment variables
    load_dotenv()

    # Load the prompt template from a file
    template_str = load_prompt_template("prompt_template.txt")
    prompt = PromptTemplate.from_template(template_str)

    # Initialize the LLM and LLMChain
    llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    # Sample question
    question = "What NFL team won the Super Bowl in the year Shakira was born?"
    # Invoke the LLMChain with the question
    response = llm_chain.invoke(question)
    print(response)


if __name__ == "__main__":
    main()
