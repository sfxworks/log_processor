## main.py
from log_processor import LogProcessor
from openai_client import OpenAIClient

def main(logs: str, api_key: str, endpoint: str = "https://api.openai.com/v1/engines/davinci-codex/completions") -> str:
    """Main function to process logs and send them to OpenAI"""
    log_processor = LogProcessor()
    openai_client = OpenAIClient(api_key, endpoint, log_processor)
    response = openai_client.send_logs(logs)
    return response

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python main.py <logs> <api_key>")
        sys.exit(1)
    logs = sys.argv[1]
    api_key = sys.argv[2]
    response = main(logs, api_key)
    print(response)
