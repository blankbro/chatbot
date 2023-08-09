import openai
import streamlit as st

with st.sidebar:
    model_array = []
    for model in st.secrets.OPENAI_GPT_MODEL:
        model_array.append(model["model_name"])
    st.selectbox("Model", model_array, key="Model")


def get_model():
    for m in st.secrets.OPENAI_GPT_MODEL:
        if st.session_state.Model == m["model_name"]:
            st.session_state.deployment_name = m["deployment_name"]
            st.session_state.model_name = m["model_name"]
            break


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
