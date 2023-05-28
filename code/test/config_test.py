import openai
from langchain.llms import AzureOpenAI

import utils.env as env

if __name__ == "__main__":
    openai.api_type = env.OPENAI_API_TYPE
    openai.api_key = env.OPENAI_API_KEY
    openai.api_base = env.OPENAI_API_BASE
    openai.api_version = env.OPENAI_API_VERSION
    completion_model = env.OPENAI_COMPLETION_MODEL

    prompt = "什么是OpenAI？"
    response = openai.Completion.create(
        engine=completion_model,
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

    llm = AzureOpenAI(
        deployment_name=completion_model,
    )
    llm("What is OpenAI?")

