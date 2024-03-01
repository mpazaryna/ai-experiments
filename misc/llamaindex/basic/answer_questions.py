from llama_index import StorageContext, load_index_from_storage

# Load knowledge base from disk outside the answer_question function to increase performance
index = load_index_from_storage(StorageContext.from_defaults(persist_dir="storage"))
query_engine = index.as_query_engine()


def answer_question(query):
    try:
        # Run a query on the query engine. This will find text chunks that are similar to the query
        # and use GPT-3 to return the answer.
        response = query_engine.query(query)
        return response
    except Exception as e:
        # Provide a meaningful error message to the user in case of any issues.
        return f"An error occurred: {e}"


def answer_questions():
    print("Ask a question or type 'quit' to exit.")
    while True:
        query = input("Your question: ")
        if query.strip().lower() == "quit":
            break
        response = answer_question(query)
        print(response)


if __name__ == "__main__":
    answer_questions()
