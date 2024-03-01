import streamlit as st

st.write("Hello world!")
st.header("st.button")

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
