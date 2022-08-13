from first_task.file_handlers import JsonFilesHandler
from first_task.converter import Converter
from first_task.output import save_converted_data


def main():
    """Запускает выполнение программы."""

    input_handler = JsonFilesHandler('input.json', 'units.json')
    input_data = input_handler.get_input_data()
    units_data = input_handler.get_units_data()

    converter = Converter(units_data)
    save_converted_data(converter.get_converted_unit(input_data))


if __name__ == '__main__':
    main()
