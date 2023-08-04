import os

# from dotenv import load_dotenv
from llama_index import StorageContext, load_index_from_storage


class QuestionAnswering:
    def __init__(self):
        # Load environment variables from .env file
        # load_dotenv()

        # Load your API key from an environment variable or secret management service
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

        # Load knowledge base from disk. You may want to move this outside of the class to increase performance
        self.index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir="storage")
        )

        # Make the knowledge base into a query engine—an object that queries can be run on
        self.query_engine = self.index.as_query_engine()

    def answer_question(self, query):
        # Run a query on the query engine. This will:
        # - Find text chunks that are similar to the query we gave it
        # - Give the query + the text chunks to GPT-3, and then return the answer
        response = self.query_engine.query(query)
        return response

    def answer_questions(self):
        while True:
            query = input("Ask a question: ")
            if query == "quit":
                break
            response = self.answer_question(query)
            print(response)
