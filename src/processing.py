from typing import Dict, List


def filter_by_state(list_of_dict: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрация списка по ключу 'state'"""
    new_list_of_dict = []
    for dict_ in list_of_dict:
        if dict_.get("state") == state:
            new_list_of_dict.append(dict_)

    return new_list_of_dict


def sort_by_date(list_of_dict: List[Dict], reverse_date: bool = True) -> List[Dict]:
    """Функция сортировки по дате"""
    return sorted(list_of_dict, key=lambda date: date["date"], reverse=reverse_date)
