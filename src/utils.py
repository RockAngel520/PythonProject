import json

def read_json_file(path: str) -> list[dict | None]:
    '''
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    '''
    try:
        with open(path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except:
         return []


if __name__ == '__main__':
    print(read_json_file('data/operations.json'))