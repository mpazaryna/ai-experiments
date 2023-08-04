from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index.node_parser import SimpleNodeParser


def construct_base_from_directory(path):
    try:
        # load all of the files inside of the folder named "data" and store them in a variable called documents
        print("Loading your data for the knowledge base...")
        documents = SimpleDirectoryReader(path).load_data()

        # split the documents into chunks, and turn them into a format that will make them easy to query
        # NOTE: this step COSTS MONEY so we only want to do this once for each document we're using. it costs $0.0004 / 1k tokens, so it's fairly cheap—but be aware of what you're doing
        print("Creating knowledge base.")
        index = GPTVectorStoreIndex.from_documents(documents)

        # save the resulting index to disk so that we can use it later
        print("Knowledge base created. Saving to disk...")
        index.storage_context.persist()

    except Exception as e:
        print("An error occurred:", e)


# Example usage:
construct_base_from_directory("./data")
