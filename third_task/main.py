from pathlib import Path

from common.utils import get_input_data, save_data
from third_task.questions_tree import get_question_tree


def main():
    """Запускает выполнение программы."""
    current_dir = Path(__file__).resolve().parent
    input_data = get_input_data(current_dir / 'questions.json')
    questions_path = get_question_tree(input_data).get_all_questions_path_data()
    save_data(questions_path, current_dir / 'questions_path.json')


if __name__ == '__main__':
    main()
