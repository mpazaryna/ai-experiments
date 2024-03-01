from qa import QuestionAnswering


class QuestionAnsweringSystem:
    def __init__(self):
        self.qa = QuestionAnswering()

    def answer_questions(self):
        self.qa.answer_questions()
