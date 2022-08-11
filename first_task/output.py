import json

from file_handlers import UnitInfo


def save_converted_data(converted_data: UnitInfo):
    """Сохраняет данные и выводит их в консоль."""
    with open('converted.json', 'w') as f:
        f.write(json.dumps(converted_data, indent=2))
    print(converted_data)
