import os

import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

# Start the conversation with a system message (this can be any message you want to set the behavior of the assistant)
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]

while True:
    # Get user input
    user_message = input("User: ")

    # Check if the user wants to quit
    if user_message.lower() == "quit":
        break

    # Append user message to conversation
    messages.append({"role": "user", "content": user_message})

    # Call OpenAI API
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    # Get the assistant's message from the response
    assistant_message = response["choices"][0]["message"]["content"]
    print(f"Assistant: {assistant_message}")

    # Append assistant message to conversation
    messages.append({"role": "assistant", "content": assistant_message})
