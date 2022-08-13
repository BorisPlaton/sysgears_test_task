from filters import (
    AbstractFilter,
    SortingFilter,
    IncludeFilter,
    ExcludeFilter,
)


class DataFilter:
    conditions_mapping = {
        'sort_by': SortingFilter,
        'include': IncludeFilter,
        'exclude': ExcludeFilter,
    }

    def get_filtered_data(self) -> list[dict]:
        """Возвращает отфильтрованные данные."""
        self._initialize_modules()
        return self._filter_data()

    @property
    def condition(self) -> dict:
        """Возвращает список условий для фильтрации."""
        return self.input_data.get('condition')

    @property
    def data(self) -> list[dict]:
        """Возвращает список данных."""
        return self.input_data.get('data')

    def _initialize_modules(self):
        """
        Инициализирует модули, которые были выбраны
        во входных данных.
        """
        for condition_name, statements in self.condition.items():
            if module := self.conditions_mapping.get(condition_name):
                self.active_filters.append(module(statements))

    def _filter_data(self) -> list[dict]:
        """Фильтрует данные и возвращает список с ними."""
        filtered_data = []
        for filter_ in self.active_filters:
            filtered_data = filter_.filter(
                self.data if not filtered_data else filtered_data
            )
        return filtered_data

    def __init__(self, input_data: dict):
        self.input_data = input_data
        self.active_filters: list[AbstractFilter] = []
