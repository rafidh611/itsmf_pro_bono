import streamlit as st



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



if st.sidebar.button(':red[Reset Chat]'):
    pass

st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")

if st.sidebar.button(":blue[What is ITSMF?]"):
    pass

st.sidebar.write(" ")

if st.sidebar.button(":blue[How do I join ITSMF?]"):
    pass

st.sidebar.write(" ")

if st.sidebar.button(":blue[Is ITSMF hiring?]"):
    pass

st.sidebar.write(" ")

user_question = st.chat_input("Ask a question....")


if user_question:
    pass