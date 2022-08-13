from pathlib import Path

from io_utils import get_input_data, save_filtered_data
from modules_handler import DataFilter


def main(input_file: str | Path):
    """Запускает выполнение программы."""
    handler = DataFilter(get_input_data(input_file))
    save_filtered_data(handler.get_filtered_data())


if __name__ == '__main__':
    main('input.json')
