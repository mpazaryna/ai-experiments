# Importing necessary modules
from langchain.chains.summarize import (
    load_summarize_chain,  # Load the summarization chain
)
from langchain.chat_models import (
    ChatOpenAI,  # Chat model from langchain based on OpenAI's GPT
)
from langchain.document_loaders import (
    WebBaseLoader,  # Loader to fetch documents from the web
)


def run_call_summarize(url):
    """
    Given a URL, this function fetches its content, summarizes it using a chain based on the GPT model,
    and returns the summarized version.

    Args:
        url (str): The URL of the web page/document to be summarized.

    Returns:
        str: Summarized content of the provided URL.
    """

    # Create an instance of the WebBaseLoader with the provided URL.
    # This will be used to fetch the content from the URL.
    loader = WebBaseLoader(url)

    # Load the document/content from the provided URL.
    docs = loader.load()

    # Instantiate the ChatOpenAI model.
    # Using the GPT "gpt-3.5-turbo-16k" variant with a temperature of 0 for deterministic outputs.
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")

    # Load the summarization chain.
    # The 'llm' instance is provided as an argument to use for summarization.
    # The type of chain being used is specified as "stuff" (exact functionality would depend on library specifics).
    chain = load_summarize_chain(llm, chain_type="stuff")

    # Run the summarization chain on the loaded documents and return the summarized result.
    return chain.run(docs)
