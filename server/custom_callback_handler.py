from typing import Any

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


class WebStreamingCallbackHandler(StreamingStdOutCallbackHandler):
    tokens = []

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        self.tokens.append(token)
