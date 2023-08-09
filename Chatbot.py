import openai
import streamlit as st

with st.sidebar:
    st.selectbox("Model", ("GPT-3.5", "GPT-4"), key="Model")


def get_model():
    if st.session_state.Model == "GPT-3.5":
        st.session_state.deployment_name = st.secrets.GPT3_5["OPENAI_ENGINE_DEPLOYMENT_NAME"]
        st.session_state.model_name = st.secrets.GPT3_5["OPENAI_ENGINE_MODEL_NAME"]
    elif st.session_state.Model == "GPT-4":
        st.session_state.deployment_name = st.secrets.GPT4["OPENAI_ENGINE_DEPLOYMENT_NAME"]
        st.session_state.model_name = st.secrets.GPT4["OPENAI_ENGINE_MODEL_NAME"]


def clear_chat():
    st.session_state.messages = []


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        get_model()
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
                api_key=st.secrets["OPENAI_API_KEY"],
                api_base=st.secrets["OPENAI_API_BASE"],
                api_version=st.secrets["OPENAI_API_VERSION"],
                api_type=st.secrets["OPENAI_API_TYPE"],
                engine=st.session_state.deployment_name,
                model=st.session_state.model_name,
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        st.button("Clear chat", key="clear_chat", on_click=clear_chat)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
