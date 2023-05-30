import time

from flask import Flask, stream_with_context

from custom_callback_handler import WebStreamingCallbackHandler
from helper import LLMHelper

app = Flask(__name__)


@app.route('/test')
def test():
    def generate():
        for i in range(5):
            time.sleep(1)
            yield f'Response {i}\n'

    return app.response_class(stream_with_context(generate()))


@app.route('/chat')
def chat():
    # query_string = request.query_string
    # query_params = urllib.parse.parse_qs(query_string)
    # question = query_params['question'][0]
    question = "What is OpenAI?"
    # chat_history = query_params['chat_history']
    chat_history = None

    def generate():
        handler = WebStreamingCallbackHandler()
        llmHelper = LLMHelper(callbacks=[handler])
        llmHelper.generate_response(question="", chat_history=None)

        for token in handler.tokens:
            yield token
            time.sleep(0.2)

    return app.response_class(stream_with_context(generate()))


if __name__ == '__main__':
    app.run()
