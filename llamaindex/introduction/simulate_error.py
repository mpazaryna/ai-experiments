from llama_index import SimpleDirectoryReader, VectorStoreIndex


def run_chatbot_demo():
    try:
        # Creating a SimpleDirectoryReader object and loading data from the "data" directory
        documents = SimpleDirectoryReader("data").load_data()

        # Creating a VectorStoreIndex object from the loaded documents
        # No specific service context is provided, so default settings will be used
        index = VectorStoreIndex.from_documents(documents)

        # Creating a chat engine from the index
        query_engine = index.as_chat_engine()

        # Querying the chat engine with a specific question and getting a response
        response = query_engine.chat("What did the author do growing up?")

        # Printing the response to the console
        print(response)

        # Simulate an exception by raising a custom exception
        raise ValueError("This is a custom exception to test the try-except block.")

        # Querying the chat engine again with a different question and getting a response
        response = query_engine.chat("Oh interesting, tell me more.")

        # Printing the response to the console
        print(response)

    except Exception as e:
        # Handle any potential exceptions gracefully
        print(f"An error occurred: {str(e)}")


# Run the function to execute the chatbot demo
run_chatbot_demo()
