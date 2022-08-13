import pytest

from second_task.filters import IncludeFilter, SortingFilter, ExcludeFilter


@pytest.fixture
def data_list():
    return [
        {'number': 1, 'word': 'one'},
        {'number': 2, 'word': 'two'},
        {'number': 1, 'word': 'one_2'},
        {'number': 4, 'word': 'four'},
        {'number': 3, 'word': 'three'},
    ]


def test_include_module(data_list):
    include_module = IncludeFilter([{'number': 1}])
    new_data_list = include_module.filter(data_list)
    assert len(new_data_list) == 2
    for data in new_data_list:
        assert data['number'] == 1
        assert data['word'].startswith('one')


def test_exclude_module(data_list):
    exclude_module = ExcludeFilter([{'number': 1}, {'word': 'four'}, {'number': 3}])
    new_data_list = exclude_module.filter(data_list)
    assert len(new_data_list) == 1
    data = new_data_list[0]
    assert data['number'] == 2


def test_sorting_module(data_list):
    sorting_module = SortingFilter(['number'])
    sorted_data_list = sorting_module.filter(data_list)
    correct_numbers_order = [1, 1, 2, 3, 4]
    received_numbers_order = [item.get('number') for item in sorted_data_list]
    assert correct_numbers_order == received_numbers_order
    sorting_module = SortingFilter(['word'])
    sorted_data_list = sorting_module.filter(data_list)
    correct_words_order = ['four', 'one', 'one_2', 'three', 'two']
    received_words_order = [item.get('word') for item in sorted_data_list]
    assert received_words_order == correct_words_order
