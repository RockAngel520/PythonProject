from typing import Any, Dict, Generator, Iterable


def filter_by_currency(transactions: Iterable[Dict[str, Any]], currency: str) -> Generator[Dict[str, Any], None, None]:
    """Функция-генератор, которая фильтрует транзакции по валюте"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: Iterable[Dict[str, Any]]) -> Generator[Dict[str, Any], None, None]:
    """Функция-генератор, которая возвращает описание каждой операции по очереди из списка"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int = 0, end: int = 9999999999999999) -> Generator:
    """Функция-генератор, которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX из заданного диапазона"""
    if (
        not str(start).isdigit()
        or not str(end).isdigit()
        or start < 0
        or end < 0
        or start > 9999999999999999
        or end > 9999999999999999
    ):
        raise TypeError("Введите число в диапазоне от 0 до 9999999999999999")
    while start <= end:
        beginning_zero = 16 - len(str(start))
        number_card_without_spaces = "0" * beginning_zero + str(start)
        number_card = (
            f"{number_card_without_spaces[:4]} "
            f"{number_card_without_spaces[4:8]} "
            f"{number_card_without_spaces[8:12]} "
            f"{number_card_without_spaces[12:]}"
        )
        yield number_card
        start += 1
