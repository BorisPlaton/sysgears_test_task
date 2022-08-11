from unittest import TestCase

from first_task.file_handlers import JsonFilesHandler


class TestJsonFileHandler(TestCase):

    def setUp(self) -> None:
        self.handler = JsonFilesHandler()

    def test_get_input_distance_data_with_json_files(self):
        data = self.handler.get_input_data('tests/source/valid_input.json')
        assert isinstance(data.get('distance'), dict)
        assert isinstance(data.get('distance').get('unit'), str)
        assert isinstance(data.get('distance').get('value'), float)
        assert isinstance(data.get('convert_to'), str)

        data = self.handler.get_input_data('tests/source/valid_input2.json')
        assert isinstance(data.get('distance'), dict)
        assert isinstance(data.get('distance').get('unit'), str)
        assert isinstance(data.get('distance').get('value'), int)
        assert isinstance(data.get('convert_to'), str)

    def test_get_units_data(self):
        data = self.handler.get_units_data('tests/source/units.json')
        assert isinstance(data.get('base_unit'), str)
        assert isinstance(data.get('available_units'), list)
        for data in data.get('available_units'):
            assert isinstance(data, dict)
