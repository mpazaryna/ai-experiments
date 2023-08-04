from dotenv import find_dotenv, load_dotenv

# Load environment variables
load_dotenv(find_dotenv())

from call_summarize import run_call_summarize

if __name__ == "__main__":
    print("Summarize Data")
    url_to_summarize = "https://austinkleon.com/2010/01/31/logbook/"
    result = run_call_summarize(url_to_summarize)
    print(result)
