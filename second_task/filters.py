from typing import Any


class AbstractFilter:
    """Абстрактный модуль для фильтрации данных."""

    def filter(self, data_list: list[dict]):
        """
        Фильтрует список `objects_list` по какому-то
        критерию и возвращает измененный список с этими
        записями.
        """
        raise NotImplementedError


class IncludeFilter(AbstractFilter):
    """Модуль для включения по списку значений."""

    def filter(self, data_list: list[dict]) -> list[dict | None]:
        """
        Сохраняет только те данные, что имеют те же
        значения, что и в списке `self.condition_statements`,
        иначе удаляет из `data_list`.
        """
        filtered_data_list = []
        for data in data_list:
            for key, value in self._conditions():
                if data.get(key) != value:
                    break
            else:
                filtered_data_list.append(data)
        return filtered_data_list

    def _conditions(self) -> tuple[Any, Any]:
        """
        Возвращает ключ и значение для фильтрации данных.
        """
        for item in self.condition_statements:
            for key, value in item.items():
                yield key, value

    def __init__(self, statements: list[dict]):
        self.condition_statements = statements


class ExcludeFilter(IncludeFilter):
    """Модуль для исключения данных по значению."""

    def filter(self, data_list: list[dict]) -> list[dict | None]:
        """
        Сохраняет только те данные, у которых нет
        значений, что и в списке `self.condition_statements`,
        иначе удаляет из `data_list`.
        """
        filtered_data_list = []
        for data in data_list:
            for key, value in self._conditions():
                if data.get(key) == value:
                    break
            else:
                filtered_data_list.append(data)
        return filtered_data_list


class SortingFilter(AbstractFilter):
    """Модуль для сортировки по значению."""

    def filter(self, data_list: list[dict]):
        """
        Возвращает список `data_list` в порядке, который
        задан в `self.condition_statements`.
        """
        sorted_data_list = sorted(
            data_list,
            key=lambda x: self._get_item_values(x)
        )
        return sorted_data_list

    def _get_item_values(self, item: dict) -> tuple:
        """
        Возвращает значения предмета по ключам из
        `self.condition_statements`.
        """
        item_values = [
            item.get(condition) for condition in self.condition_statements
        ]
        return tuple(item_values)

    def __init__(self, statements: list[str]):
        self.condition_statements = statements
