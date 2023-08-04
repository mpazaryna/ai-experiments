import os

# from dotenv import load_dotenv
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index.node_parser import SimpleNodeParser


class KnowledgeBaseConstructor:
    def __init__(self):
        # Load environment variables from .env file
        # load_dotenv()

        # Load your API key from an environment variable or secret management service
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

    def construct_base_from_directory(self, path):
        # Load all of the files inside the folder specified by the path
        # Store them in a variable called documents
        print("Loading your data for the knowledge base...")
        documents = SimpleDirectoryReader(path).load_data()

        # Build an index from the documents
        # Split the documents into chunks
        # NOTE: This step costs money
        print("Creating knowledge base.")
        index = GPTVectorStoreIndex.from_documents(documents)

        # Save the resulting index to disk so that we can use it later
        print("Knowledge base created. Saving to disk...")
        index.storage_context.persist()
