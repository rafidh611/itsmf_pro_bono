import streamlit as st
from backend_logic import run_user_query


st.title(":blue[ITSMF Chat Bot]")


st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #222222;
    }

    [data-testid="stSidebar"] {
        background-color: black;
    }

    [data-testid="stHeader"] {
        background-color: black;
    }

    [data-testid="stBottomBlockContainer"] {
        background-color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")



if st.sidebar.button(':red[Reset Chat]'):
    pass

st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")

if st.sidebar.button(":blue[What is ITSMF?]"):
    response = run_user_query("What is ITSMF?")
    st.write(response)

st.sidebar.write(" ")

if st.sidebar.button(":blue[How do I join ITSMF?]"):
    response = run_user_query("How do I join ITSMF?")
    st.write(response)

st.sidebar.write(" ")

if st.sidebar.button(":blue[Is ITSMF hiring?]"):
    response = run_user_query("Is ITSMF hiring?")
    st.write(response)

st.sidebar.write(" ")

user_question = st.chat_input("Ask a question...")


if user_question:
    response = run_user_query(user_question)
    str1 = "Reponse: " + response[1]
    st.write(str1)
    