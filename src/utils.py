import json
import logging

logging.basicConfig(
    filename="logs/utils.log",
    encoding="utf-8",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
)

read_json_file_logger = logging.getLogger("app.utils")
# read_json_file_logger = logging.getLogger('app.utils')
# file_handler = logging.FileHandler('logs/utils.log', 'w', encoding='utf-8')
# file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
# file_handler.setFormatter(file_formatter)
# read_json_file_logger.addHandler(file_handler)
# read_json_file_logger.setLevel(logging.DEBUG)


def read_json_file(path: str) -> list[dict | None]:
    """
    Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях
    """
    read_json_file_logger.info('Запуск функции "read_json_file"')
    try:
        with open(path, "r", encoding="utf-8") as json_file:
            read_json_file_logger.info(f"Успешное открытие файла {path}")
            read_json_file_logger.info('Успешное завершение работы функции "read_json_file"')
            return json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
        read_json_file_logger.error(f"Ошибка при чтении файла {path}: {str(e)}")
        print(f"Ошибка при чтении файла {path}: {str(e)}")
        return []


# if __name__ == '__main__':
#     print(read_json_file('data/operations.json'))
