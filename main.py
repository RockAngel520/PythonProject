from src.pandas_modul import read_csv_file, read_excel_file
from src.processing import filter_by_state, sort_by_date
from src.searches import search_string_in_transactions
from src.utils import read_json_file
from src.widget import get_date, mask_account_card


def main():
    """Основная функция, отвечающая за логику проекта и связывающая функции между собой"""

    print(
        """
Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
    )
    while True:  # Выбор пользователя из какого файла обработать транзакции
        choice = int(input())
        if choice == 1:
            print("Для обработки выбран JSON-файл.")
            input_transactions = read_json_file("data/operations.json")
            break
        elif choice == 2:
            print("Для обработки выбран CSV-файл.")
            input_transactions = read_csv_file("data/transactions.csv")
            break
        elif choice == 3:
            print("Для обработки выбран XLSX-файл.")
            input_transactions = read_excel_file("data/transactions_excel.xlsx")
            break
        else:
            print(
                """
Необходимо ввести цифру 1, 2 или 3:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
            )

    while True:  # Выбор статуса для фильтрации транзакций
        state = input(
            """
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

"""
        )
        if state.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_by_state(input_transactions, state.upper())
            break
        else:
            print(f'Статус операции "{state}" недоступен.')

    while True:  # Сортировка транзакций по дате
        need_sorted_by_date = input("Отсортировать операции по дате? Да/Нет\n")
        if need_sorted_by_date.lower() == "да":

            while True:  # Сортировка по возврастанию/убыванию даты
                sort_by_date_abc = input("Отсортировать по возрастанию или по убыванию?\n")
                if sort_by_date_abc.lower() == "по убыванию":
                    transactions = sort_by_date(transactions, True)
                    break
                elif sort_by_date_abc.lower() == "по возрастанию":
                    transactions = sort_by_date(transactions, False)
                    break

            break
        elif need_sorted_by_date.lower() == "нет":
            break

    while True:  # Фильтр по рублевым транзакциям
        need_filtered_by_rub = input("Выводить только рублевые транзакции? Да/Нет\n")
        if need_filtered_by_rub.lower() == "да":
            if choice == 1:
                transactions = [
                    transaction
                    for transaction in transactions
                    if transaction["operationAmount"]["currency"]["code"] == "RUB"
                ]
                break
            else:
                transactions = [transaction for transaction in transactions if transaction["currency_code"] == "RUB"]
                break
        elif need_filtered_by_rub.lower() == "нет":
            break

    while True:  # Фильтр по определенному слову в описании
        need_sort_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
        if need_sort_by_word.lower() == "да":
            word = input("Введите слово для фильтрации\n")
            transactions = search_string_in_transactions(transactions, word)
            break
        elif need_sort_by_word.lower() == "нет":
            break

    len_transactions = len(transactions)  # Подсчет транзакций и вывод на экран
    if len_transactions == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len_transactions}")
        for transaction in transactions:
            print("")
            print(get_date(transaction["date"]), transaction["description"])
            if transaction.get("from") is None:
                print(mask_account_card(transaction["to"]))
            else:
                print(f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}")
            if choice == 1:
                print(
                    f"Сумма: {transaction['operationAmount']['amount']} "
                    f"{transaction['operationAmount']['currency']['name']}"
                )
            else:
                print(f"Сумма: {transaction['amount']} {transaction['currency_name']}")


if __name__ == "__main__":
    main()
