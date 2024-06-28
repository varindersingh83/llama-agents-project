from typing import Any, Dict

class CustomOpenAILLM:
    def __init__(self, model: str, api_key: str):
        self.model = model
        self.api_key = api_key
        self.context_window = 2048  # Set a default context window size

    def achat(self, messages: Any, **kwargs: Any) -> Any:
        # Implement async chat method
        pass

    def acomplete(self, prompt: str, **kwargs: Any) -> Any:
        # Implement async complete method
        pass

    def astream_chat(self, messages: Any, **kwargs: Any) -> Any:
        # Implement async stream chat method
        pass

    def astream_complete(self, prompt: str, **kwargs: Any) -> Any:
        # Implement async stream complete method
        pass

    def chat(self, messages: Any, **kwargs: Any) -> Any:
        # Implement chat method
        pass

    def complete(self, prompt: str, **kwargs: Any) -> Any:
        # Implement complete method
        pass

    def metadata(self) -> Dict[str, Any]:
        # Implement metadata method
        return {
            "model": self.model,
            "api_key": self.api_key,
            "context_window": self.context_window,
        }

    def stream_chat(self, messages: Any, **kwargs: Any) -> Any:
        # Implement stream chat method
        pass

    def stream_complete(self, prompt: str, **kwargs: Any) -> Any:
        # Implement stream complete method
        pass
