import os
import time

from openai import OpenAI

# Constants
ASSISTANT_ID = "asst_7D0vjOW8K7PUmGFYcqblKAG1"
MAX_WAIT_TIME = 30  # Maximum time to wait for a response, in seconds

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def create_thread(client):
    """Create a new thread and return the thread object."""
    try:
        return client.beta.threads.create()
    except Exception as e:
        print(f"Error creating thread: {e}")
        return None


def send_message(client, thread_id, content):
    """Send a message to a specific thread."""
    try:
        return client.beta.threads.messages.create(
            thread_id=thread_id, role="user", content=content
        )
    except Exception as e:
        print(f"Error sending message: {e}")
        return None


def run_thread(client, thread_id):
    """Run a specific thread and return the run object."""
    try:
        return client.beta.threads.runs.create(
            thread_id=thread_id, assistant_id=ASSISTANT_ID
        )
    except Exception as e:
        print(f"Error running thread: {e}")
        return None


def retrieve_messages(client, thread_id):
    """Retrieve and print all messages from a specific thread."""
    try:
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        for message in reversed(messages.data):
            print(f"{message.role}: {message.content[0].text.value}")
    except Exception as e:
        print(f"Error retrieving messages: {e}")


def wait_for_response(client, thread_id, run_id):
    """Wait for the run to complete and return the result."""
    elapsed_time = 0
    while elapsed_time < MAX_WAIT_TIME:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread_id, run_id=run_id
        )
        if run_status.status in ["completed", "failed"]:
            return run_status
        time.sleep(5)  # Check every 5 seconds
        elapsed_time += 5
    print("Timeout waiting for response.")
    return None


# Main execution
if __name__ == "__main__":
    thread = create_thread(client)
    if thread:
        print(f"Thread created: {thread.id}")
        send_message(client, thread.id, "Solve this problem: 3x + 11 = 14")
        run = run_thread(client, thread.id)
        if run:
            print(f"Run initiated: {run.id}")
            completed_run = wait_for_response(client, thread.id, run.id)
            if completed_run and completed_run.status == "completed":
                retrieve_messages(client, thread.id)
            else:
                print("Run did not complete successfully.")
