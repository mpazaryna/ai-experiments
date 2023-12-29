import streamlit as st

# Title of the app
st.title("Question Submission App")

# User input
user_question = st.text_input("Ask a question:", "")

# Button to submit the question
if st.button("Submit"):
    if user_question:
        st.write("Your question: ", user_question)
    else:
        st.write("Please enter a question.")
