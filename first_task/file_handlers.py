import json
from pathlib import Path
from typing import TypedDict


class UnitInfo(TypedDict):
    unit: str
    value: int | float


class InputDistanceData(TypedDict):
    distance: UnitInfo
    convert_to: str


class AvailableUnits(TypedDict):
    base_unit: str
    available_units: list[UnitInfo]


class JsonFilesHandler:
    """
    Класс для работы с файлами json, где хранятся
    данные о величинах.
    """

    def get_input_data(self, input_file: str | Path = None) -> InputDistanceData:
        """Возвращает словарь с данными ввода."""
        input_file = input_file or self.input_file
        input_data = self.read_json_file(input_file)
        return InputDistanceData(**input_data)

    def get_units_data(self, units_file: str | Path = None) -> AvailableUnits:
        """
        Читает файл с данными о всех доступных величинах
        и возвращает его.
        """
        units_file = units_file or self.units_file
        units_data = self.read_json_file(units_file)
        return AvailableUnits(**units_data)

    @staticmethod
    def read_json_file(file: str | Path) -> dict:
        """
        Читает json-файл и возвращает его содержимое
        в виде словаря.
        """
        with open(file) as f:
            return json.loads(f.read())

    def __init__(self, input_file: str | Path = None, units_file: str | Path = None):
        """
        Устанавливает пути к файлам ввода и файла с данными.
        """
        self.input_file = input_file
        self.units_file = units_file
