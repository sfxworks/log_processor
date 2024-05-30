## log_processor.py
import logging
import tiktoken

class LogProcessor:
    def __init__(self, encoding_name: str = "cl100k_base"):
        self.encoding = tiktoken.get_encoding(encoding_name)

    def process_logs(self, logs: str) -> list:
        """Process logs and chunk them into 32k token sizes"""
        chunked_logs = self.chunk_logs(logs)
        return chunked_logs

    def chunk_logs(self, logs: str) -> list:
        """Chunk logs into 32k token sizes"""
        tokenized_logs = self.encoding.encode(logs)
        chunked_logs = [tokenized_logs[i:i + 32000] for i in range(0, len(tokenized_logs), 32000)]
        return chunked_logs
