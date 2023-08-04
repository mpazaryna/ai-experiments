# conversation_call.py
from langchain import ConversationChain, PromptTemplate
from langchain.llms import OpenAI

# --------------------------------------------------------------
# Memory: Add State to Chains and Agents
# --------------------------------------------------------------


def run_conversation_demo():
    llm = OpenAI()
    conversation = ConversationChain(llm=llm, verbose=True)
    output1 = conversation.predict(input="Hi there!")
    output2 = conversation.predict(
        input="I'm doing well! Just having a conversation with an AI."
    )
    return output1, output2
