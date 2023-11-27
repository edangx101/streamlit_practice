import streamlit as st

st.title("Hi there")
st.subheader("first subheader")
st.header("first HEADER")
st.text("Hi i am text function")
st.markdown("**Helloo** woorld")


st.header('st.button')
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')