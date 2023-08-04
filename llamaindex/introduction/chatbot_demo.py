from llama_index import SimpleDirectoryReader, VectorStoreIndex


def run_chatbot_demo():
    # With the try-except block, the code will handle any exceptions that might arise during the
    # execution of the run_chatbot_demo() function. Instead of crashing the program, it
    # will print an error message containing the exception details. This allows
    # the program to continue execution if possible, even if
    # an error occurs during the chatbot demo.
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

        # Querying the chat engine again with a different question and getting a response
        response = query_engine.chat("Oh interesting, tell me more.")

        # Printing the response to the console
        print(response)

    except Exception as e:
        # Handle any potential exceptions gracefully
        print(f"An error occurred: {str(e)}")


# Run the function to execute the chatbot demo
# run_chatbot_demo()

# With the try-except block, the code will handle any exceptions that might arise during the
# execution of the run_chatbot_demo() function. Instead of crashing the program, it
# will print an error message containing the exception details. This allows
# the program to continue execution if possible, even if
# an error occurs during the chatbot demo.
