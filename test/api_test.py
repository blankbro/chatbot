import openai
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

import server.env as env
from server.helper import LLMHelper


def test_openai():
    openai.api_type = env.OPENAI_API_TYPE
    openai.api_key = env.OPENAI_API_KEY
    openai.api_base = env.OPENAI_API_BASE
    openai.api_version = env.OPENAI_API_VERSION
    deployment_name = env.OPENAI_ENGINE_DEPLOYMENT_NAME

    prompt = "什么是OpenAI？"
    response = openai.Completion.create(
        engine=deployment_name,
        prompt=prompt,
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    print(f"1 ==> {response}")
    print(f'2 ==> {response["choices"][0]["text"]}')
    print(f'3 ==> {response["choices"][0]["text"].strip()}')


def test_azure_openai():
    LLMHelper(callbacks=[StreamingStdOutCallbackHandler()]).generate_response(question="What is OpenAI?")


if __name__ == "__main__":
    test_azure_openai()
