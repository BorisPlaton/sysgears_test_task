from typing import TypedDict


class Answer(TypedDict):
    next_question: str
    answer: str


class Question(TypedDict):
    question: str
    answers: list[Answer]


class QuestionsPathDetailedInfo(TypedDict):
    number: int
    list: list[list[dict]]


class QuestionsPath(TypedDict):
    paths: QuestionsPathDetailedInfo


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

    def get_question_path(self) -> list[list[dict]]:
        """
        Возвращает данные о всех возможных путей опросов, начиная
        с текущего вопроса.
        """
        end_answers = []
        questions_path = []
        for answer, question_node in self.answers.items():
            if question_node is None:
                end_answers.append(answer)
                continue
            for path in question_node.get_question_path():
                questions_path.append([{self.question: answer}, *path])
        if end_answers:
            questions_path.append([{self.question: '/'.join(end_answers)}])
        return questions_path

    def get_all_questions_path_data(self) -> QuestionsPath:
        """
        Возвращает словарь с данными о всех возможных опросах
        и их количество.
        """
        questions_path_list = self.get_question_path()
        number = len(questions_path_list)
        return {'paths': {'number': number, 'list': questions_path_list}}

    @classmethod
    def set_questions_list(cls, questions_list: list[Question]):
        """Устанавливает список вопросов."""
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


def get_question_tree(questions: list[Question]) -> QuestionNode:
    QuestionNode.set_questions_list(questions)
    question, answers = questions[0]['question'], questions[0]['answers']
    return QuestionNode(question, answers)
