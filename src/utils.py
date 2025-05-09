import json
import requests


API_KEY = 6TnEwuTZ6DS9llgpXGHy2QFvDQvZTwcfм

def read_json_file(path: str) -> list[dict | None]:
    '''
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    '''
    try:
        with open(path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except:
         return []





def currency_conversions(transaction: dict) -> float:
    '''Функция, которая возвращает сумму транзакции в рублях'''
    if transaction['operationAmount']['currency']['code'] == 'RUB':
        amount = transaction['operationAmount']['amount']
    else:
        pass

    return amount


if __name__ == '__main__':
    print(read_json_file('data/operations.json'))
    print(currency_conversions(read_json_file('data/operations.json')[1]))