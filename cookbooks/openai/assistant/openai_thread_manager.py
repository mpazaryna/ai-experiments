import time

from openai import OpenAI


class OpenAIThreadManager:
    def __init__(self, api_key, assistant_id):
        self.client = OpenAI(api_key=api_key)
        self.assistant_id = assistant_id
        self.max_wait_time = 30

    def create_thread(self):
        try:
            return self.client.beta.threads.create()
        except Exception as e:
            print(f"Error creating thread: {e}")
            return None

    def send_message(self, thread_id, content):
        try:
            return self.client.beta.threads.messages.create(
                thread_id=thread_id, role="user", content=content
            )
        except Exception as e:
            print(f"Error sending message: {e}")
            return None

    def run_thread(self, thread_id):
        try:
            return self.client.beta.threads.runs.create(
                thread_id=thread_id, assistant_id=self.assistant_id
            )
        except Exception as e:
            print(f"Error running thread: {e}")
            return None

    def retrieve_messages(self, thread_id):
        try:
            messages = self.client.beta.threads.messages.list(thread_id=thread_id)
            for message in reversed(messages.data):
                print(f"{message.role}: {message.content[0].text.value}")
        except Exception as e:
            print(f"Error retrieving messages: {e}")

    def wait_for_response(self, thread_id, run_id):
        elapsed_time = 0
        while elapsed_time < self.max_wait_time:
            run_status = self.client.beta.threads.runs.retrieve(
                thread_id=thread_id, run_id=run_id
            )
            if run_status.status in ["completed", "failed"]:
                return run_status
            time.sleep(5)
            elapsed_time += 5
        print("Timeout waiting for response.")
        return None
