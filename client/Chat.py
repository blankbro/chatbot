import traceback

import streamlit as st
from streamlit_chat import message

from server.helper import LLMHelper


def clear_chat_data():
    st.session_state['input'] = ""
    st.session_state['chat_history'] = []


def send_msg():
    question = st.session_state['input']
    if question:
        response = llm_helper.generate_response(question, st.session_state['chat_history'])
        st.session_state['chat_history'].append((question, response))
        st.session_state['input'] = ""


try:
    st.set_page_config(layout="wide")

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    llm_helper = LLMHelper()

    col1, col2 = st.columns([9, 1])
    with col1:
        st.text_input("You: ", placeholder="type your question", key="input")
        clear_chat = st.button("Clear chat", key="clear_chat", on_click=clear_chat_data)
    with col2:
        st.text("")
        st.text("")
        st.button("Send", on_click=send_msg)

    if st.session_state['chat_history']:
        for i in range(len(st.session_state['chat_history']) - 1, -1, -1):
            message(st.session_state['chat_history'][i][1], key=str(i))
            message(st.session_state['chat_history'][i][0], is_user=True, key=str(i) + '_user')
except Exception as e:
    traceback.print_exc()
    st.error(traceback.format_exc())
