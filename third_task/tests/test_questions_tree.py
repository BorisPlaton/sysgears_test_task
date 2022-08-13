import json
from pathlib import Path

import pytest

from third_task.questions_tree import get_question_tree, QuestionNode


@pytest.fixture
def path_to_source():
    return Path(__file__).resolve().parent / 'source'


@pytest.fixture
def questions(path_to_source):
    with open(path_to_source / 'questions.json') as f:
        return json.loads(f.read())


@pytest.fixture
def tree(questions) -> QuestionNode:
    return get_question_tree(questions)


def test_tree_building(questions):
    tree = get_question_tree(questions)
    assert isinstance(tree, QuestionNode)
    assert tree.question == "What is your marital status?"
    assert len(tree.answers) == 2


def test_tree_answers_is_question_tree(tree):
    answers = tree.answers
    for answer in answers:
        assert isinstance(answer, str)
        assert isinstance(answers[answer], QuestionNode)
        assert answer == 'Single' or answer == 'Married'
        assert (
                answers[answer].question == "Are you planning on getting married next year?"
                or answers[answer].question == "How long have you been married?"
        )
