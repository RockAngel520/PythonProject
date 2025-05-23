import pandas as pd


def read_csv_file(path: str) -> list[dict | None]:
    """
    Функция, которая принимает на вход путь до CSV-файла
    и возвращает список словарей с данными о финансовых транзакциях
    """
    try:
        with open(path, "r", encoding="utf-8") as csv_file:
            df = pd.read_csv(csv_file, delimiter=";")
            return df.to_dict(orient="records")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Ошибка при чтении файла {path}: {str(e)}")
        return []


def read_excel_file(path: str) -> list[dict | None]:
    """
    Функция, которая принимает на вход путь до Excel-файла
    и возвращает список словарей с данными о финансовых транзакциях
    """
    try:
        with open(path, "rb") as excel_file:
            df = pd.read_excel(excel_file)
            return df.to_dict(orient="records")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Ошибка при чтении файла {path}: {str(e)}")
        return []


# if __name__ == '__main__':
#     print(read_excel_file('data/transactions_excel.xlsx'))
