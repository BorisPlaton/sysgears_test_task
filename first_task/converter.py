from file_handlers import UnitInfo, AvailableUnits, InputDistanceData


class Converter:
    """
    Класс, который преобразует одну величину
    в другую.
    """

    def get_converted_unit(self, convert_data: InputDistanceData) -> UnitInfo:
        """
        Конвертирует одну величину в другую и возвращает
        результат.
        """
        converted_value = convert_data['distance']['value']
        convert_unit = convert_data['distance']['unit']
        convert_to = convert_data['convert_to']

        if convert_unit != self.base_unit:
            converted_value = self.from_unit_to_base(convert_unit, converted_value)
        if convert_to != self.base_unit:
            converted_value = self.from_base_to_unit(convert_to, converted_value)
        return UnitInfo(unit=convert_to, value=converted_value)

    def from_base_to_unit(self, unit_to_convert: str, base_value: int | float) -> int | float:
        """
        Преобразует значение из стандартной величины
        в ту, которую запросил пользователь.
        """
        for unit_info in self.available_units:
            if unit_to_convert == unit_info['unit']:
                return self.get_rounded(base_value * unit_info['value'])
        raise ValueError(f"Неизвестная величина `{unit_to_convert}`.")

    def from_unit_to_base(self, unit_to_convert: str, unit_value: int | float) -> int | float:
        """
        Преобразует значение из нестандартной величины
        в стандартную.
        """
        for unit_info in self.available_units:
            if unit_to_convert == unit_info['unit']:
                return self.get_rounded(unit_value / unit_info['value'])
        raise ValueError(f"Неизвестная величина `{unit_to_convert}`.")

    @staticmethod
    def get_rounded(expression: int | float) -> float:
        """Округляет до сотых выражение."""
        return float("{:.2f}".format(expression))

    @property
    def base_unit(self) -> str:
        """
        Возвращает величины, относительно которой
        задаются другие величины.
        """
        return self.units['base_unit']

    @property
    def available_units(self) -> list[UnitInfo]:
        """
        Возвращает список доступных для конвертации
        величин.
        """
        return self.units['available_units']

    def __init__(self, units: AvailableUnits):
        """Сохраняет данные о конвертации."""
        self.units = units
