from answer_questions import answer_question, answer_questions


def get_answer(question):
    """
    Get the answer to a specific question using the 'answer_question' function.

    Parameters:
        question (str): The question to be answered.

    Returns:
        str: The response to the given question.
    """
    try:
        response = answer_question(question)
        return response
    except Exception as e:
        return f"Error: {e}"


def main():
    """
    Main function to answer specific questions and have a chat back and forth with the AI.

    Usage:
        1. To get answers for specific questions, call 'get_answer' with the question.
        2. To chat back and forth with the AI in the console, call 'answer_questions'.
    """
    question1 = "What is wu wei?"
    response1 = get_answer(question1)
    print(f"Question: {question1}\nResponse: {response1}\n")

    question2 = "Who is Dan Shipper?"
    response2 = get_answer(question2)
    print(f"Question: {question2}\nResponse: {response2}\n")

    # Uncomment the line below if you want to chat back and forth with the AI in the console
    answer_questions()


if __name__ == "__main__":
    main()
