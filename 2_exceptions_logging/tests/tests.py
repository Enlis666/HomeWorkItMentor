from calculate_average import calculate_average
from unittest.mock import Mock

def test_calc_average(list_data):
    func_mock = Mock()
    func_mock.side_effect(list_data)
    assert calculate_average(func_mock) == 3.0