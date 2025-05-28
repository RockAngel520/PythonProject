import re


def search_string_in_transactions(transactions: list[dict], string: str) -> list[dict]:
    """Функция сортировки банковских операций по строке."""
    new_transactions = [transaction for transaction in transactions if re.search(string, transaction['description'], flags=re.IGNORECASE)]
    return new_transactions


# my_transactions = [
# {'id': 2177828.0, 'state': 'EXECUTED', 'date': '2022-04-14T15:14:21Z', 'amount': 24853.0, 'currency_name': 'Yuan Renminbi',
# 'currency_code': 'CNY', 'from': 'Счет 38577962752140632721', 'to': 'Счет 47657753885349826314',
# 'description': 'Перевод со счета на счет'},
#
# {'id': 4699552.0, 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z', 'amount': 23423.0, 'currency_name': 'Peso',
# 'currency_code': 'PHP', 'from': 'Discover 7269000803370165', 'to': 'American Express 1963030970727681',
# 'description': 'Перевод с карты на карту'}
# ]
# my_string = 'СЧЕТ'
#
#
# if __name__ == '__main__':
#     print(search_string_in_transactions(my_transactions, my_string))
