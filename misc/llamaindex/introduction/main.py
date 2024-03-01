# Importing the required functions from the respective modules.
from chatbot_demo import run_chatbot_demo
from chunks_demo import run_chunks_demo
from simple_demo import run_simple_demo

# Ensuring the code below only runs when this script is executed directly.
if __name__ == "__main__":
    try:
        # Printing the heading for the Simple Demo.
        print("Llama Index Demo:")
        # Running the Simple Demo and printing its output.
        print(run_simple_demo())

        # Printing the heading for the Chunks Demo.
        print("Llama Index Demo with Chunks:")
        # Running the Chunks Demo and printing its output.
        print(run_chunks_demo())

        # Printing the heading for the Chatbot Demo.
        print("Llama Index Demo with Chatbot:")
        # Running the Chatbot Demo and printing its output.
        print(run_chatbot_demo())

    except Exception as e:
        # In case any errors occur, we catch and print the exception.
        print(f"An error occurred: {e}")
