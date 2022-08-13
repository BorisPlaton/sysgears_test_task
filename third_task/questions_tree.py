from typing import TypedDict


class Answer(TypedDict):
    next_question: str
    answer: str


class Question(TypedDict):
    question: str
    answers: list[Answer]


class QuestionAndAnswer(TypedDict):
    question: str


class QuestionPaths(TypedDict):
    number: int
    list: list[QuestionAndAnswer]


class QuestionNode:
    """Класс вопроса."""

    _questions_list: list[Question] = []

    def build(self, answers: list[Answer]):
        """
        Возвращает словарь где ключом есть ответ, а значением
        следующий вопрос класса `QuestionNode`.
        """
        answers_map: dict[str, QuestionNode | None] = {}
        for answer in answers:
            if not (question := answer['next_question']):
                question_node = None
            else:
                question_node = QuestionNode(
                    question,
                    self.get_question_answers(question)
                )
            answers_map[answer['answer']] = question_node
        self.answers = answers_map

    def get_question_answers(self, question_text: str):
        """Возвращает список ответов на вопрос."""
        for question in self._questions_list:
            if question['question'] == question_text:
                return question['answers']

    @classmethod
    def set_questions_list(cls, questions_list: list[Question]):
        cls._questions_list = questions_list

    def __init__(self, question: str, answers: list[Answer]):
        """
        Сохраняет вопрос и словарь, где ключом есть
        ответ на вопрос, а значение - следующий вопрос
        после ответа.
        """
        self.question = question
        self.answers: dict[str, QuestionNode | None] = {}
        self.build(answers)


def get_question_tree(questions: list[Question]):
    QuestionNode.set_questions_list(questions)
    question, answers = questions[0]['question'], questions[0]['answers']
    return QuestionNode(question, answers)
