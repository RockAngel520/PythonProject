def get_mask_card_number(card_number: str) -> str:
    """Функция возвращающая маску введенного номера карты"""
    str_card_number = str(card_number) # перевод номера карты в строк

    if len(str_card_number) == 0:
        raise AssertionError("Номер карты не может быть пустым")
    if len(str_card_number) != 16:
        raise AssertionError("Номер карты должен состоять из 16 цифр")
    if not str_card_number.isdigit():
        raise AssertionError("Номер карты должен состоять только из цифр")

    mask_card_number = f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"

    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция возвращающая маску введенного номера счета"""
    str_account_number = str(account_number)  # перевод номера счета в строку

    if len(str_account_number) == 0:
        raise AssertionError("Номер счета не может быть пустым")
    if len(str_account_number) != 20:
        raise AssertionError("Номер счета должен состоять из 20 цифр")
    if not str_account_number.isdigit():
        raise AssertionError("Номер счет должен состоять только из цифр")

    mask_account_number = f"**{str_account_number[-4:]}"

    return mask_account_number
