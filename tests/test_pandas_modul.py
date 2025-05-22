from unittest.mock import Mock, patch, mock_open

import pytest

from src.pandas_modul import read_csv_file, read_excel_file


@pytest.fixture
def input_operations():
    return [
        {
            'id': 4699552.0,
            'state': 'EXECUTED',
            'date': '2022-03-23T08:29:37Z',
            'amount': 23423.0,
            'currency_name': 'Peso',
            'currency_code': 'PHP',
            'from': 'Discover 7269000803370165',
            'to': 'American Express 1963030970727681',
            'description': 'Перевод с карты на карту'
        }
    ]


def test_read_csv_file(input_operations):
    mock_transactions = Mock(return_value=input_operations)
    read_csv_file = mock_transactions
    assert read_csv_file() == input_operations
    read_csv_file.assert_called_once_with()


def test_read_excel_file(input_operations):
    mock_transactions = Mock(return_value=input_operations)
    read_excel_file = mock_transactions
    assert read_excel_file() == input_operations
    read_excel_file.assert_called_once_with()


def test_read_excel_no_file():
    assert read_excel_file("1") == []


def test_read_csv_no_file():
    assert read_csv_file("1") == []


def test_read_csv_success():
    csv_data = """id;state
650703;EXECUTED
593027;CANCELED"""

    mock_file = mock_open(read_data=csv_data)

    with patch('builtins.open', mock_file):
        result = read_csv_file('test_file.csv')

        assert len(result) == 2
        assert result[0] == {'id': 650703, 'state': 'EXECUTED'}
        assert result[1] == {'id': 593027, 'state': 'CANCELED'}
