import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.markdown(
    """
This component supports **markdown formatting**, which is handy.

[Check out their documentation](https://docs.streamlit.io) for more information on how to get started.
"""
)
