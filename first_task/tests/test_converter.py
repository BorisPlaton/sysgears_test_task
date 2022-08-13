from pathlib import Path

import pytest

from first_task.converter import Converter
from first_task.file_handlers import InputDistanceData, JsonFilesHandler


@pytest.fixture
def path_to_source():
    return Path(__file__).resolve().parent / 'source'


@pytest.fixture
def converter(path_to_source):
    return Converter(JsonFilesHandler().get_units_data(path_to_source / 'units.json'))


def get_input_data(convert_from, convert_value, convert_to='m'):
    return InputDistanceData(
        convert_to=convert_to,
        distance={'unit': convert_from, 'value': convert_value}
    )


@pytest.mark.parametrize(
    'unit,value,base_value',
    [
        ('km', 2, 2000),
        ('cm', 54, 0.54),
        ('mm', 1000, 1),
        ('yd', 10, 9.144),
        ('ft', 100, 30.48),
    ]
)
def test_convert_from_unit_to_base(converter, unit, value, base_value):
    assert abs(converter.from_unit_to_base(unit, value) - base_value) < 0.5


@pytest.mark.parametrize(
    'unit,value,base_value',
    [
        ('km', 2, 2000),
        ('cm', 54, 0.54),
        ('mm', 1000, 1),
        ('yd', 10, 9.144),
        ('ft', 100, 30.48),
    ]
)
def test_convert_from_base_to_unit(converter, unit, value, base_value):
    assert abs(converter.from_base_to_unit(unit, base_value) - value) < 0.5


@pytest.mark.parametrize(
    'value',
    [
        4.0141,
        5.012,
        5.01232141_313,
    ]
)
def test_rounded_valued(value, converter):
    suffix = str(converter.get_rounded(value)).split('.')[1]
    assert len(suffix) == 2


@pytest.mark.parametrize(
    'unit_from, unit_to, value, converted_value',
    [
        ('km', 'm', 2, 2000),
        ('cm', 'yd', 150, 1.64),
        ('mm', 'ft', 320, 1.04),
        ('m', 'mm', 320, 320000),
        ('ft', 'yd', 14, 4.66),
    ]
)
def test_different_units_converting(converter, unit_from, unit_to, value, converted_value):
    input_data = get_input_data(unit_from, value, unit_to)
    assert abs(converter.get_converted_unit(input_data).get('value') - converted_value) < 0.5
    assert converter.get_converted_unit(input_data).get('unit') == unit_to
