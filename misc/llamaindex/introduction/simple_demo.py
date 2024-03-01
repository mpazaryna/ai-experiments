# Importing required modules from the llama_index library
from llama_index import SimpleDirectoryReader, VectorStoreIndex


# Function to run a simple demo of the VectorStoreIndex
def run_simple_demo():
    # Step 1: Load documents from the "data" directory using SimpleDirectoryReader
    documents = SimpleDirectoryReader("data").load_data()

    # Step 2: Create an index from the loaded documents using VectorStoreIndex
    index = VectorStoreIndex.from_documents(documents)

    # Step 3: Convert the index into a query engine
    query_engine = index.as_query_engine()

    # Step 4: Perform a query on the query engine
    response = query_engine.query("What did the author do growing up?")

    # Step 5: Print the response obtained from the query
    print(response)
