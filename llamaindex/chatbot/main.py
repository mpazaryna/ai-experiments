from qa_system import QuestionAnsweringSystem


class MyChatbot:
    def __init__(self):
        # Constructor code here
        self.qa = QuestionAnsweringSystem()

    def run(self):
        # Method code here
        self.qa.answer_questions()


# Create an instance of MyClass and call the desired method
my_bot = MyChatbot()
my_bot.run()
