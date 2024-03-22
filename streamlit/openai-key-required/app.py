import streamlit as st
from langchain_openai import OpenAI

# Set the title of the Streamlit app
st.title("LangChain and OpenAI")
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def generate_response(input_text):
    """
    Generates a response for the given input text using OpenAI API.

    Parameters:
    - input_text (str): The text to generate a response for.

    Side Effects:
    - Displays the response inside the Streamlit app using st.info.
    """
    try:
        # Initialize the OpenAI API client with specified temperature and API key
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

        # Invoke the OpenAI API with the input text and display the result
        st.info(llm.invoke(input_text))
    except Exception as e:
        # Display an error message in case of API invocation failure
        st.error(f"Failed to generate response: {e}")


# Create a form for input submission
with st.form("my_form"):
    # Text area for user input with a default value
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )

    # Button to submit the form
    submitted = st.form_submit_button("Submit")

    # Check if the API key is provided and correctly formatted
    if not openai_api_key or not openai_api_key.startswith("sk-"):
        st.warning("Please enter a valid OpenAI API key!", icon="⚠️")
    elif submitted:
        # Generate and display the response if the API key is valid and the form is submitted
        generate_response(text)
