from pathlib import Path

from common.utils import save_data, get_input_data
from modules_handler import DataFilter


def main(input_file: str | Path):
    """Запускает выполнение программы."""
    current_dir = Path(__file__).resolve().parent
    handler = DataFilter(get_input_data(input_file))
    save_data(
        handler.get_filtered_data(),
        current_dir / 'filtered.json'
    )


if __name__ == '__main__':
    main('input.json')
