# Import necessary modules
import os
import sys

from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Uncomment the below line if you want to load the OpenAI API key directly
# openai.api_key = os.getenv("OPENAI_API_KEY")

# Import Gradio for creating a user interface
import gradio as gr

# Import necessary modules and classes for indexing and prediction
from gpt_index import (
    GPTListIndex,
    GPTSimpleVectorIndex,
    LLMPredictor,
    PromptHelper,
    SimpleDirectoryReader,
)
from langchain.chat_models import ChatOpenAI

# Set the OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def construct_index(directory_path):
    # Define constants for the index construction
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600

    # Create a prompt helper with the defined constants
    prompt_helper = PromptHelper(
        max_input_size,
        num_outputs,
        max_chunk_overlap,
        chunk_size_limit=chunk_size_limit,
    )

    # Create a predictor using the ChatOpenAI model
    llm_predictor = LLMPredictor(
        llm=ChatOpenAI(
            temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs
        )
    )

    # Load documents from the specified directory
    documents = SimpleDirectoryReader(directory_path).load_data()

    # Create an index using the loaded documents, predictor, and prompt helper
    index = GPTSimpleVectorIndex(
        documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
    )

    # Save the constructed index to disk
    index.save_to_disk("index.json")

    return index


def chatbot(input_text):
    # Load the previously saved index from disk
    index = GPTSimpleVectorIndex.load_from_disk("index.json")

    # Query the index with the input text and get a response
    response = index.query(input_text, response_mode="compact")

    return response.response


# Create a Gradio interface for the chatbot
iface = gr.Interface(
    fn=chatbot,
    inputs=gr.components.Textbox(lines=7, label="Enter your text"),
    outputs="text",
    title="Custom-trained AI Chatbot",
)

# Construct the index using documents from the "docs" directory
index = construct_index("docs")

# Launch the Gradio interface
iface.launch(share=True)
