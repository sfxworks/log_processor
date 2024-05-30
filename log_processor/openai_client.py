## openai_client.py
import openai
import ssl
from log_processor import LogProcessor

class OpenAIClient:
    def __init__(self, api_key: str, endpoint: str = "https://api.openai.com/v1/engines/davinci-codex/completions", log_processor: LogProcessor = None):
        self.api_key = api_key
        self.endpoint = endpoint
        self.log_processor = log_processor if log_processor else LogProcessor()
        openai.api_key = self.api_key

    def send_logs(self, logs: str) -> str:
        """Send chunked logs to an OpenAI compatible endpoint"""
        chunked_logs = self.log_processor.process_logs(logs)
        responses = []
        for chunk in chunked_logs:
            response = openai.Completion.create(
                engine="davinci-codex",
                prompt=chunk,
                max_tokens=60,
                n=1,
                stop=None,
                temperature=0.5,
                request_timeout=60,
                ssl_context=ssl.create_default_context()
            )
            responses.append(response.choices[0].text.strip())
        return "\n".join(responses)
