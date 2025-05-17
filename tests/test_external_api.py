from unittest.mock import Mock, patch

import pytest

from src.external_api import currency_conversions


@pytest.fixture
def input_operations_in_rub():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def input_operations_in_usd():
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


def test_currency_conversions_rub(input_operations_in_rub):
    result = currency_conversions(input_operations_in_rub)
    assert result == "31957.58"


@patch("src.external_api.requests.get")
def test_currency_conversions_usd(mock_get, input_operations_in_usd):
    mock_response = Mock()
    mock_response.json.return_value = {"result": 7500.50}
    mock_get.return_value = mock_response

    result = currency_conversions(input_operations_in_usd)
    assert result == 7500.50


def test_currency_conversions_invalid_data():
    assert currency_conversions({}) is None
    assert currency_conversions({"operationAmount": {}}) is None
