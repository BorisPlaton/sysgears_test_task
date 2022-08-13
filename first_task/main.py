from pathlib import Path

from common.utils import save_data
from first_task.file_handlers import JsonFilesHandler
from first_task.converter import Converter


def main():
    """Запускает выполнение программы."""
    current_dir = Path(__file__).resolve().parent
    input_handler = JsonFilesHandler(
        current_dir / 'input.json',
        current_dir / 'units.json'
    )
    input_data = input_handler.get_input_data()
    units_data = input_handler.get_units_data()

    converter = Converter(units_data)
    save_data(
        converter.get_converted_unit(input_data),
        current_dir / 'converted.json',
    )


if __name__ == '__main__':
    main()
