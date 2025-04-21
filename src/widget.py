from src import masks


def mask_account_card(card_or_account_number: str) -> str:
    """Функция, которая определяет карта это или номер и возвращает маску"""
    if len(card_or_account_number) == 0:
        raise IndexError("Данные не введены")

    account_or_card_name_and_numder = card_or_account_number.split()
    if "Счет" in card_or_account_number and len(account_or_card_name_and_numder[-1]) == 20:
        account_or_card_name_and_numder[-1] = masks.get_mask_account(account_or_card_name_and_numder[-1])
    elif "Счет" not in card_or_account_number and len(account_or_card_name_and_numder[-1]) == 16:
        account_or_card_name_and_numder[-1] = masks.get_mask_card_number(account_or_card_name_and_numder[-1])
    else:
        raise AttributeError("Введены некорректные данные")

    return " ".join(account_or_card_name_and_numder)


def get_date(input_date: str) -> str:
    """Функция, которая преобразует дату в формат ДД.ММ.ГГГГ"""
    if len(input_date) == 0:
        raise IndexError("Данные не введены")
    if not input_date[8:10].isdigit() or not input_date[5:7].isdigit() or not input_date[0:4].isdigit():
        raise AttributeError("Введены некорректные данные")
    if int(input_date[8:10]) == 0 or int(input_date[8:10]) > 31 or int(input_date[5:7]) == 0 or int(input_date[5:7]) > 12 or int(input_date[0:4]) < 1900 or int(input_date[0:4]) > 2025:
        raise TypeError("Введена некорректная дата")

    output_date = f"{input_date[8:10]}.{input_date[5:7]}.{input_date[0:4]}"

    return output_date
