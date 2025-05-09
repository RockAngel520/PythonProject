import os
from dotenv import load_dotenv
import requests
# from utils import read_json_file

load_dotenv()
api_key = os.getenv('API_KEY')

def currency_conversions(transaction: dict) -> float | None:
    '''Функция, которая возвращает сумму транзакции в рублях'''
    try:
        if not transaction:
            print('В словаре нет данных')

        currency_data = transaction.get('operationAmount', {}).get('currency', {})
        if currency_data.get('code') == 'RUB':
            return transaction['operationAmount']['amount']

        currency = currency_data.get('code')
        amount = transaction['operationAmount'].get('amount')

        if not currency or not amount:
            print('Ошибка данных')

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": api_key}

        response = requests.get(url, headers=headers, timeout=10)

        return round(response.json()['result'], 2)

    except requests.exceptions.RequestException as e:
        print(f'Ошибка API: {e}')
    except (KeyError, TypeError) as e:
        print(f'Ошибка данных транзакции: {e}')
    except Exception as e:
        print(f'Неожиданная ошибка: {e}')

# if __name__ == '__main__':
#     print(currency_conversions(read_json_file('data/operations.json')[1]))
