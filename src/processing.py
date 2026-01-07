import re
from collections import Counter
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


def process_bank_search(list_dict: list[dict], search_string: str) -> list[dict]:
    """принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список словарей,
    у которых в описании есть данная строка."""
    try:
        new_list_dict = list()

        pattern = re.compile(search_string, re.IGNORECASE)
        for item in list_dict:
            key_value = item.get("description")
            if key_value and pattern.search(key_value):
                new_list_dict.append(item)
    except Exception as e:
        print(f"Внимание! Ошибка {e}! Введены не корректные данные!")
    return new_list_dict


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    categories_counter = Counter()
    for operation in data:
        description = operation.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                categories_counter[category] += 1
    return categories_counter
