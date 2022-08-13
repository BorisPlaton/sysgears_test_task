import json
from pathlib import Path


def save_data(data, save_to: Path):
    """Сохраняет данные и выводит их в консоль."""
    with open(save_to, 'w') as f:
        f.write(json.dumps(data, indent=2))
    print(data)


def get_input_data(file: str | Path):
    """Читает JSON-файл и возвращает словарь."""
    with open(file) as f:
        return json.loads(f.read())
