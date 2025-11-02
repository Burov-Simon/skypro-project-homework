from typing import Any, Dict, List


def filter_by_state(list_dict: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция которая возвращает новый список словарей в соответствии с аргументом state (по умолчанию - EXECUTED)"""
    new_list_dict = []

    for sta in list_dict:
        if sta.get("state") == state:
            new_list_dict.append(sta)

    return new_list_dict


def sort_by_date(list_dict: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Функция сортировки списка словарей по дате (по умолчанию - убывание)"""
    sorted_list_dict = sorted(list_dict, key=lambda x: x.get("date", ""), reverse=descending)

    return sorted_list_dict
