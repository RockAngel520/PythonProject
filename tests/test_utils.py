from unittest.mock import Mock

import pytest

from src.utils import read_json_file


@pytest.fixture
def input_operations():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]


def test_read_json_file(input_operations):
    mock_transactions = Mock(return_value=input_operations)
    read_json_file = mock_transactions
    assert read_json_file() == input_operations
    read_json_file.assert_called_once_with()


def test_read_json_no_file():
    assert read_json_file("1") == []
