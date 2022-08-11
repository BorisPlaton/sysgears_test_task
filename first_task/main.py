from file_handlers import JsonFilesHandler
from converter import Converter


def main():
    """Запускает выполнение программы."""

    input_handler = JsonFilesHandler('input.json', 'units.json')
    input_data = input_handler.get_input_data()
    units_data = input_handler.get_units_data()

    converter = Converter(units_data)
    print(converter.get_converted_unit(input_data))


if __name__ == '__main__':
    main()
