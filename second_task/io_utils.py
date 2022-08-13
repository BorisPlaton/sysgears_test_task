import json
from pathlib import Path


def save_filtered_data(filtered_data):
    """Сохраняет данные и выводит их в консоль."""
    with open('filtered.json', 'w') as f:
        f.write(json.dumps(filtered_data, indent=2))
    print(filtered_data)


def get_input_data(file: str | Path) -> dict:
    """Читает JSON-файл и возвращает словарь."""
    with open(file) as f:
        return json.loads(f.read())
