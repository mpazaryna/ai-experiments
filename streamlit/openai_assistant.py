import time

import openai

import streamlit as st

assistant_id = "asst_uLudSyZicfQUK1KisyEDaXEm"

client = openai

if "file_id_list" not in st.session_state:
    st.session_state.file_id_list = []

if "start_chat" not in st.session_state:
    st.session_state.start_chat = False

if "thread_id" not in st.session_state:
    st.session_state.thread_id = None

st.set_page_config(page_title="OpenAI Assistant", page_icon=":robot_face:")

st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter your api key", type="password")
if api_key:
    openai.api_key = api_key

# Display all file ids
if st.session_state.file_id_list:
    st.sidebar.subheader("File Ids")
    st.sidebar.write(st.session_state.file_id_list)

if st.sidebar.button("Start Chat"):
    # if st.session_state.file_id_list:
    st.session_state.start_chat = True
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id
    st.write("thread id: ", thread.id)
    # else:
    # st.sidebar.warning("Please upload a file first")


def process_message_with_citations(message):
    message_content = message.content[0].text
    annotations = (
        message_content.annotations if hasattr(message_content, "annotations") else []
    )
    citations = []

    # Iterate over the annotations and add footnotes
    for index, annotation in enumerate(annotations):
        message_content.value = message_content.value.replace(
            annotation.text, f"[{index +1}]"
        )

        if file_citation := getattr(annotation, "file_citation", None):
            cited_file = {"filename": "cited_document.pdf"}
            citations.append(
                f'[{index +1}] {file_citation.quote} from {cited_file["filename"]}'
            )
        elif file_path := getattr(annotation, "file_path", None):
            cited_file = {"filename": "downloaded_document.pdf"}
            citations.append(
                f'[{index +1}] Click [here](#) to download {cited_file["filename"]}'
            )

    full_response = message_content.value + "\n\n" + "\n".join(citations)
    return full_response


st.title("OpenAI Assistants API Chat")
st.write(
    "This is a demo of the OpenAI Assistants API. You can use this to chat with an AI assistant."
)

# only show chat interface if the chat has been started
if st.session_state.start_chat:
    # initialize the model and messages list if not already in session state
    if "openai_model" not in st.session_state:
        st.session_state.openai_model = "gpt-4-1106-preview"
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # display existing messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # chat input for the user
    if prompt := st.chat_input("What is up?"):
        # add user message to the state and display it
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # add the users message to the existing thread
        client.beta.threads.message.create(
            thread_id=st.session_state.thread_id,
            role="user",
            content="prompt",
        )

        # create run with additional instructions
        run = client.beta.threads.run.create(
            thread_id=st.session_state.thread_id,
            assistant_id=assistant_id,
            instructions="Please answer the queries using the knowledge provided in the documents.",
        )

        # poll for the run to complete and retrived the assistant's message
        while run.status != "completed":
            time.sleep(1)
            run = client.beta.threads.run.retrieve(
                thread_id=st.session_state.thread_id, run_id=run.id
            )

        # retrieve the messages added by the assistant
        messages = client.beta.threads.message.list(
            thread_id=st.session_state.thread_id
        )

        # process and display assistant messages
        assistant_messages_for_run = [
            message
            for message in messages
            if message.run_id == run.id and message.role == "assistant"
        ]
        for message in assistant_messages_for_run:
            full_response = process_message_with_citations(message)
            st.session_state.messages.append(
                {"role": "assistant", "content": full_response}
            )
            with st.chat_message("assistant"):
                st.markdown(full_response, unsafe_allow_html=True)
    else:
        # prompt to star the chat
        st.write("please upload a file to start the chat.")
