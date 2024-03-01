from llama_index import ServiceContext, SimpleDirectoryReader, VectorStoreIndex


def run_chunks_demo():
    try:
        # Load data from the "data" directory using SimpleDirectoryReader
        documents = SimpleDirectoryReader("data").load_data()

        # Create a ServiceContext object with a default chunk size of 1000
        service_context = ServiceContext.from_defaults(chunk_size=1000)

        # Create a VectorStoreIndex object from the loaded documents
        # and provide the service_context to handle indexing operations
        index = VectorStoreIndex.from_documents(
            documents, service_context=service_context
        )

        # Create a query engine from the index
        query_engine = index.as_query_engine()

        # Query the engine with a specific question and get a response
        query = "What did the author do growing up?"
        response = query_engine.query(query)

        # Print the response to the console
        print(f"Response to the query '{query}': {response}")

    except Exception as e:
        # Handle any potential exceptions gracefully
        print(f"An error occurred: {str(e)}")


# Run the function to execute the demo
# run_chunks_demo()
