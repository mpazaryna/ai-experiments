import os

from openai_thread_manager import OpenAIThreadManager

# Main execution
if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    assistant_id = "asst_7D0vjOW8K7PUmGFYcqblKAG1"
    manager = OpenAIThreadManager(api_key=api_key, assistant_id=assistant_id)

    thread = manager.create_thread()
    if thread:
        print(f"Thread created: {thread.id}")
        manager.send_message(thread.id, "Solve this problem: 3x + 11 = 14")
        run = manager.run_thread(thread.id)
        if run:
            print(f"Run initiated: {run.id}")
            completed_run = manager.wait_for_response(thread.id, run.id)
            if completed_run and completed_run.status == "completed":
                manager.retrieve_messages(thread.id)
            else:
                print("Run did not complete successfully.")
