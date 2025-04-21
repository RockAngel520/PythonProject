import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("card_or_account_number, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                              ("Счет 64686473678894779589", "Счет **9589"),
                                                              ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                                              ("Счет 35383033474447895560", "Счет **5560"),
                                                              ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                                                              ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                                                              ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                                                              ("Счет 73654108430135874305", "Счет **4305")
])
def test_mask_account_card(card_or_account_number, expected):
    assert mask_account_card(card_or_account_number) == expected

@pytest.mark.parametrize("wrong_card_or_account_number", [("Maestro 1596837705199",),
                                         ("Счет 45353830334744478560",),
                                         ("Счет 353adv0636248",),
                                         ("0400792289606",),
                                         ("Visa Gold 64686473678894779589",)
])
def test_wrong_account_card(wrong_card_or_account_number):
    with pytest.raises(AttributeError):
        mask_account_card(wrong_card_or_account_number)


def test_zero_account_card():
    with pytest.raises(IndexError):
        mask_account_card("")


@pytest.mark.parametrize("input_date, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                                                  ("2025-12-05T02:26:18.671407", "05.12.2025")
])
def test_get_date(input_date, expected):
    assert get_date(input_date) == expected


def test_zero_get_date():
    with pytest.raises(IndexError):
        get_date("")


@pytest.mark.parametrize("wrong_date", [("2026-03-11T02:26:18.671407",),
                                        ("2abcdT02:26:18.671407",),
                                        ("2023-15-11T02:26:18.671407",),
                                        ("2022-03-58T02:26:18.671407",),
                                        ("20240311T02:26:18.671407",)
])
def test_wrong_get_date(wrong_date):
    with pytest.raises(AttributeError):
        get_date(wrong_date)