import pytest

from src.searches import search_string_in_transactions, count_categories


@pytest.fixture
def input_operations():
    return [
        {
            "id": 4699552.0,
            "state": "EXECUTED",
            "date": "2022-03-23T08:29:37Z",
            "amount": 23423.0,
            "currency_name": "Peso",
            "currency_code": "PHP",
            "from": "Discover 7269000803370165",
            "to": "American Express 1963030970727681",
            "description": "Перевод с карты на карту",
        },
        {
            'id': 2177828.0,
            'state': 'EXECUTED',
            'date': '2022-04-14T15:14:21Z',
            'amount': 24853.0,
            'currency_name': 'Yuan Renminbi',
            'currency_code': 'CNY',
            'from': 'Счет 38577962752140632721',
            'to': 'Счет 47657753885349826314',
            'description': 'Перевод со счета на счет'},
        {
            'id': 214410.0,
            'state': 'EXECUTED',
            'date': '2020-10-29T09:56:28Z',
            'amount': 34336.0,
            'currency_name': 'Krona',
            'currency_code': 'SEK',
            'from': 'Discover 6590095029387674',
            'to': 'Mastercard 0974688087552673',
            'description': 'Перевод с карты на карту'
        },
    ]


def test_search_string_in_transactions(input_operations):
    assert search_string_in_transactions(input_operations, 'счет') == [{'id': 2177828.0, 'state': 'EXECUTED', 'date': '2022-04-14T15:14:21Z', 'amount': 24853.0, 'currency_name': 'Yuan Renminbi',
'currency_code': 'CNY', 'from': 'Счет 38577962752140632721', 'to': 'Счет 47657753885349826314', 'description': 'Перевод со счета на счет'}]


def test_search_no_string_in_transactions(input_operations):
    assert search_string_in_transactions(input_operations, 'тест') == []


def test_search_string_in_wrong_transactions():
    with pytest.raises(TypeError):
        search_string_in_transactions([1], 'тест')


def test_count_categories(input_operations):
    assert count_categories(input_operations, ['Перевод с карты на карту', 'Перевод со счета на счет']) == {'Перевод с карты на карту': 2, 'Перевод со счета на счет': 1}


def test_count_empty_categories(input_operations):
    assert count_categories(input_operations, []) == {}


def test_empty_transactions_count_categories():
    assert count_categories([], ['Перевод с карты на карту', 'Перевод со счета на счет']) == {}


def test_count_categories_wrong_transactions():
    with pytest.raises(TypeError):
        search_string_in_transactions([1], ['Перевод с карты на карту', 'Перевод со счета на счет'])

