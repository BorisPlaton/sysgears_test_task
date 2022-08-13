from pathlib import Path

from common.utils import get_input_data
from third_task.questions_tree import get_question_tree


def main():
    """Запускает выполнение программы."""
    current_dir = Path(__file__).resolve().parent
    input_data = get_input_data(current_dir / 'questions.json')
    questions = get_question_tree(input_data)


if __name__ == '__main__':
    main()
